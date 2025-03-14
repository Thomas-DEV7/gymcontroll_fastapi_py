from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class TrainingBase(BaseModel):
    name: str
    description: Optional[str] = None

class TrainingOut(TrainingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class ExerciseBase(BaseModel):
    name: str
    description: Optional[str] = None

class ExerciseOut(ExerciseBase):
    id: int
    training_id: int

    class Config:
        orm_mode = True

class ExecutionBase(BaseModel):
    weight: float
    repetitions: int

class ExecutionOut(ExecutionBase):
    id: int
    exercise_id: int
    execution_date: datetime

    class Config:
        orm_mode = True
