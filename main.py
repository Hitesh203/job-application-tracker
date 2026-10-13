import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager
from database import Base, engine
import models

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("Database_url environment variable is not set")

engine = create_engine(
    database_url,
    pool_pre_ping= True,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

#create the application instance
app = FastAPI(
    title = "Job Application Tracker API",
    description = "An API to manage and track job applications.",
    version = "0.3.0",
    lifespan = lifespan,
)
# @app.get("/") registers an HTTP GET route for the root URL.
@app.get("/")
def root():
    return {
        "message":"Welcome to Job Application Tracker API"
    }

# @app.get("/health") registers a health-check route
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/health/db")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status":"healthy",
            "database":"connected",
        }
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )