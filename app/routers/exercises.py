from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)

# Create exercise
@router.post("/", response_model=schemas.ExerciseOut)
def create_exercise(exercise: schemas.ExerciseBase, db: Session = Depends(database.get_db)):
    db_exercise = models.Exercise(**exercise.dict(), training_id=1)  # 🚨 Troque pelo training_id real ou auth
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

# List exercises
@router.get("/", response_model=List[schemas.ExerciseOut])
def get_exercises(db: Session = Depends(database.get_db)):
    exercises = db.query(models.Exercise).all()
    return exercises
