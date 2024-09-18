import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api.routes import api_router  # Adjust based on your setup

print("Import successful")
