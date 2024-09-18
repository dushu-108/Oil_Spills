import sys
import os
import logging
import smtplib
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.api.routes import api_router
from app.database import get_db
from app.models import Vessel
from app.schemas import VesselCreate, VesselUpdate
from app.email_alert import send_alert_email

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add the root of the project to sys.path
print("PYTHONPATH:", sys.path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting up...")
    yield
    logging.info("Shutting down...")

# Create the FastAPI app instance with lifespan context
app = FastAPI(
    title="Oil Spill Detection System",
    description="API for detecting oil spills using satellite data and vessel tracking.",
    version="1.0.0",
    lifespan=lifespan
)

# Include CORS middleware (optional, but useful for cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routes
app.include_router(api_router)

# Function to simulate oil spill detection (replace with actual logic)
def detect_oil_spill():
    detected = True
    if detected:
        trigger_alert()
    return detected

# Function to send alert email when an oil spill is detected
def trigger_alert():
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    subject = "ALERT: Oil Spill Detected"
    body = "An oil spill has been detected. Immediate action is required."
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    try:
        send_alert_email(subject, body, recipient_email, sender_email, smtp_server, smtp_port, sender_password)
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# API route to detect oil spill (POST request)
@app.post("/detect-oil-spill")
async def detect_oil_spill_api():
    try:
        detected = detect_oil_spill()
        if detected:
            return {"message": "Oil spill detected and alert email sent!"}
        else:
            raise HTTPException(status_code=404, detail="No oil spill detected")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Error detecting oil spill")

# Root endpoint to check if the service is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Oil Spill Detection System"}

# Retrieve a list of vessels
@app.get("/vessels/")
def read_vessels(db: Session = Depends(get_db)):
    vessels = db.query(Vessel).all()
    return vessels

# Create a new vessel
@app.post("/vessels/")
def create_vessel(vessel: VesselCreate, db: Session = Depends(get_db)):
    # Validate the input data
    if not isinstance(vessel.mmsi, int):
        raise HTTPException(status_code=400, detail="Invalid MMSI")

    # Check if the vessel already exists
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == vessel.mmsi).first()
    if db_vessel:
        raise HTTPException(status_code=400, detail="Vessel with this MMSI already exists")

    # Create a new vessel instance
    new_vessel = Vessel(
        mmsi=vessel.mmsi,
        base_date_time=vessel.base_date_time,
        latitude=vessel.latitude,
        longitude=vessel.longitude,
        sog=vessel.sog,
        cog=vessel.cog,
        heading=vessel.heading,
        vessel_name=vessel.vessel_name,
        imo=vessel.imo,
        call_sign=vessel.call_sign,
        vessel_type=vessel.vessel_type,
        status=vessel.status,
        length=vessel.length,
        width=vessel.width,
        draft=vessel.draft,
        cargo=vessel.cargo,
        transceiver_class=vessel.transceiver_class
    )
   
    # Add the new vessel to the database
    db.add(new_vessel)
    db.commit()
    db.refresh(new_vessel)
    return new_vessel

# Update a vessel
@app.put("/vessels/{mmsi}")
def update_vessel(mmsi: int, vessel_update: VesselUpdate, db: Session = Depends(get_db)):
    # Query the database for the vessel to update
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == mmsi).first()
    if db_vessel is None:
        raise HTTPException(status_code=404, detail="Vessel not found")

    # Update the vessel's information
    for key, value in vessel_update.dict(exclude_unset=True).items():
        setattr(db_vessel, key, value)

    # Commit the changes to the database
    db.commit()
    db.refresh(db_vessel)
    return db_vessel

# Delete a vessel
@app.delete("/vessels/{mmsi}")
def delete_vessel(mmsi: int, db: Session = Depends(get_db)):
    # Query the database for the vessel to delete
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == mmsi).first()
    if db_vessel is None:
        raise HTTPException(status_code=404, detail="Vessel not found")

    # Delete the vessel from the database
    db.delete(db_vessel)
    db.commit()
    return {"message": "Vessel deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8023)
