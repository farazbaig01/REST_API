from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status" : "online", "message": "Python API is running!"}

@app.get("/healthy")
def health_check():
    return {"status": "healthy"}
