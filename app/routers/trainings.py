from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database, utils

router = APIRouter(
    prefix="/trainings",
    tags=["Trainings"]
)

@router.post("/", response_model=schemas.TrainingOut)
def create_training(
    training: schemas.TrainingCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(utils.get_current_user)
):
    # Lógica para criar o treino
    db_training = models.Training(
        name=training.name,
        description=training.description,
        owner_id=current_user.id
    )
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training
