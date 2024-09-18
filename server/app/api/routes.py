# app/api/routes.py
from fastapi import APIRouter
from .endpoints import vessels, satellite, anomalies
 # Correct import path for your endpoints

api_router = APIRouter()

api_router.include_router(vessels.router, prefix="/vessels", tags=["vessels"])
api_router.include_router(satellite.router, prefix="/satellite", tags=["satellite"])
api_router.include_router(anomalies.router, prefix="/anomalies", tags=["anomalies"])

