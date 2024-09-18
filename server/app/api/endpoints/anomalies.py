from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd

# Define Pydantic models for data validation and serialization
class Anomaly(BaseModel):
    mmsi: int
    base_date_time: str  # Adjust the type based on your actual data format
    latitude: float
    longitude: float
    sog: float
    cog: float
    heading: float
    status: str
    vessel_type: str
    anomaly_type: str  # Describe the type of anomaly detected

class AnomalyResponse(BaseModel):
    anomalies: List[Anomaly]

# Create a FastAPI router
router = APIRouter()

@router.get("/", response_model=AnomalyResponse)
def get_anomalies():
    try:
        # Load anomalies from the CSV file
        anomalies_df = pd.read_csv('C:/Users/siddh/Downloads/AIS_2024_01_01/anomalies.csv')
        
        # Convert the dataframe to a list of dictionaries
        anomalies = anomalies_df.to_dict(orient='records')
        
        # Return the anomalies in the expected format
        return {"anomalies": anomalies}
    except Exception as e:
        # Handle errors and return a 500 status code with an error message
        raise HTTPException(status_code=500, detail=str(e))
