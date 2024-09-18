import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

try:
    from app.api.routes import api_router
    print("Import successful")
except ImportError as e:
    print(f"Import failed: {e}")
