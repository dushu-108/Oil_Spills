from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.VesselCreate)  # Updated to VesselCreate
def create_vessel(vessel: schemas.VesselCreate, db: Session = Depends(database.get_db)):
    return crud.create_vessel(db=db, vessel=vessel)

@router.get("/{vessel_id}", response_model=schemas.VesselCreate)  # Updated to VesselCreate
def read_vessel(vessel_id: int, db: Session = Depends(database.get_db)):
    db_vessel = crud.get_vessel(db=db, vessel_id=vessel_id)
    if db_vessel is None:
        raise HTTPException(status_code=404, detail="Vessel not found")
    return db_vessel
