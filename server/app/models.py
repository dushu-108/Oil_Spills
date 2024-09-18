from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vessel(Base):
    __tablename__ = 'vessels'
    
    id = Column(Integer, primary_key=True, index=True)
    mmsi = Column(String, index=True)
    base_date_time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    sog = Column(Float)
    cog = Column(Float)
    heading = Column(Integer)
    vessel_name = Column(String, nullable=True)
    imo = Column(String, nullable=True)
    call_sign = Column(String, nullable=True)
    vessel_type = Column(String, nullable=True)
    status = Column(String, nullable=True)
    length = Column(Float, nullable=True)
    width = Column(Float, nullable=True)
    draft = Column(Float, nullable=True)
    cargo = Column(String, nullable=True)
    transceiver_class = Column(String, nullable=True)
