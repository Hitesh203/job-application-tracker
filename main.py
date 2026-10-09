from fastapi import FastAPI
#create the application instance
app = FastAPI(
    title = "Job Application Tracker API",
    description = "An API to manage and track job applications.",
    version = "0.1.0",
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