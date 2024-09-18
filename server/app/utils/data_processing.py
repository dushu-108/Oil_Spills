import requests

def fetch_ais_data(api_url: str, params: dict):
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

def detect_anomalies(data):
    anomalies = []
    for vessel in data['vessels']:
        if vessel['speed'] > some_threshold or vessel['course'] != expected_course:
            anomalies.append(vessel)
    return anomalies
