from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dataclasses import dataclass

from src.scripts.main import run_once_for_block

app = FastAPI()


@dataclass
class ResponseModel():
    is_completed: bool


@app.get("/")
def health_check():
    return "ok"


@app.post("/rss", response_model=ResponseModel)
def run_rss_to_slac():
    print(f"Starting /rss")
    
    run_once_for_block()
    return ResponseModel(True)