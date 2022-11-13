from fastapi import FastAPI
from routes.taskRoutes import task
app=FastAPI()
app.include_router(task)

