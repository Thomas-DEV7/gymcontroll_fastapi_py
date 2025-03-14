from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db
from typing import List

router = APIRouter(
    prefix="/trainings",
    tags=["Trainings"]
)

# Create training
from app.utils import get_current_user

@router.post("/", response_model=schemas.TrainingOut)
def create_training(
    training: schemas.TrainingBase,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_training = models.Training(
        **training.dict(),
        user_id=current_user.id
    )
    
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training


# List trainings
@router.get("/", response_model=List[schemas.TrainingOut])
def get_trainings(db: Session = Depends(get_db)):
    trainings = db.query(models.Training).all()
    return trainings

# Get a single training by ID
@router.get("/{training_id}", response_model=schemas.TrainingOut)
def get_training(training_id: int, db: Session = Depends(get_db)):
    training = db.query(models.Training).filter(models.Training.id == training_id).first()
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training
