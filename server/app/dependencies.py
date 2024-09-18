from .database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

# Optional wrapper function if you prefer adding layers of abstraction for dependencies
def get_database(db: Session = Depends(get_db)):
    return db

