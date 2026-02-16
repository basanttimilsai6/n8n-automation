from fastapi import FastAPI
from git import Repo
import os
from pathlib import Path
app = FastAPI()

path = Path(__file__)




@app.post("/update")
def update_code(data: dict):
    print(path)
    return {"status": "Code updated and pushed"}