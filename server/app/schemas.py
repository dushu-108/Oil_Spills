from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VesselBase(BaseModel):
    base_date_time: Optional[datetime] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    sog: Optional[float] = None
    cog: Optional[float] = None
    heading: Optional[int] = None
    vessel_name: Optional[str] = None
    imo: Optional[str] = None
    call_sign: Optional[str] = None
    vessel_type: Optional[str] = None
    status: Optional[str] = None
    length: Optional[float] = None
    width: Optional[float] = None
    draft: Optional[float] = None
    cargo: Optional[str] = None
    transceiver_class: Optional[str] = None

class VesselCreate(VesselBase):
    mmsi: int

class VesselUpdate(VesselBase):
    pass
