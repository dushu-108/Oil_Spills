from sqlalchemy.orm import Session
from .models import Vessel
from .schemas import VesselCreate, VesselUpdate

# Create a new vessel record
def create_vessel(db: Session, vessel: VesselCreate):
    db_vessel = Vessel(
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
    db.add(db_vessel)
    db.commit()
    db.refresh(db_vessel)
    return db_vessel

# Retrieve a vessel by its MMSI
def get_vessel(db: Session, mmsi: int):
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == mmsi).first()
    if db_vessel is None:
        raise ValueError(f"Vessel with MMSI {mmsi} not found")
    return db_vessel

# Retrieve all vessels (optionally, with filters)
def get_vessels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vessel).offset(skip).limit(limit).all()

# Update a vessel's data using MMSI
def update_vessel(db: Session, mmsi: int, vessel_update: VesselUpdate):
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == mmsi).first()
    if db_vessel:
        for key, value in vessel_update.dict(exclude_unset=True).items():
            setattr(db_vessel, key, value)
        db.commit()
        db.refresh(db_vessel)
        return db_vessel
    else:
        raise ValueError(f"Vessel with MMSI {mmsi} not found")

# Delete a vessel by its MMSI
def delete_vessel(db: Session, mmsi: int):
    db_vessel = db.query(Vessel).filter(Vessel.mmsi == mmsi).first()
    if db_vessel:
        db.delete(db_vessel)
        db.commit()
        return db_vessel
    else:
        raise ValueError(f"Vessel with MMSI {mmsi} not found")
