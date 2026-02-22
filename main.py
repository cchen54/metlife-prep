from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from the MetLife Cary Hub", "version": "1.1.0"}

@app.get("/status")
def get_status():
    return {"status": "System Healthy", "version": "1.0.0"}