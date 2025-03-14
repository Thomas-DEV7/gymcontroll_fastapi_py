from fastapi import FastAPI
from app.routers import auth, trainings, exercises, executions

app = FastAPI(title="GymControll API")

# Routers
app.include_router(auth.router)
app.include_router(trainings.router)
app.include_router(exercises.router)
app.include_router(executions.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to GymControll API"}
