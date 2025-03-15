from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class TrainingBase(BaseModel):
    title: str
    description: Optional[str] = None

class TrainingCreate(TrainingBase):
    pass

class TrainingOut(TrainingBase):
    id: int
    owner: UserOut

    class Config:
        from_attributes = True

class ExerciseBase(BaseModel):
    name: str
    description: Optional[str] = None

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseOut(ExerciseBase):
    id: int
    training_id: int

    class Config:
        from_attributes = True

class ExecutionBase(BaseModel):
    weight: int
    repetitions: int

class ExecutionCreate(ExecutionBase):
    pass

class ExecutionOut(ExecutionBase):
    id: int
    exercise_id: int
    date: datetime

    class Config:
        from_attributes = True
