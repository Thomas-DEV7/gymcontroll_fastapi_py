from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, trainings, exercises, executions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GymControll API")

app.include_router(auth.router)
app.include_router(trainings.router)
app.include_router(exercises.router)
app.include_router(executions.router)
