from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, database
from typing import List

router = APIRouter(
    prefix="/executions",
    tags=["Executions"]
)

# Create execution
@router.post("/", response_model=schemas.ExecutionOut)
def create_execution(execution: schemas.ExecutionBase, db: Session = Depends(database.get_db)):
    db_execution = models.Execution(**execution.dict(), exercise_id=1)  # 🚨 Troque pelo exercise_id real ou auth
    db.add(db_execution)
    db.commit()
    db.refresh(db_execution)
    return db_execution

# List executions
@router.get("/", response_model=List[schemas.ExecutionOut])
def get_executions(db: Session = Depends(database.get_db)):
    executions = db.query(models.Execution).all()
    return executions
