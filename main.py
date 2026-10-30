from fastapi import FastAPI

app = FastAPI(title="AWS Git Deployment Demo")


@app.get("/")
def home():
    return {"message": "Hello from GitHub deployed to AWS! - Modified"}


@app.get("/health")
def health():
    return {"status": "healthy", "environment": "AWS EC2"}


@app.get("/employees")
def get_employees():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]