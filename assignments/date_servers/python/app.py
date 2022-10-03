from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/timestamp")
def read_root():
    return {"datetime": datetime.now().isoformat()}