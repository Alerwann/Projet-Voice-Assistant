from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.menu_handler import generate_voice_response
from config.settings import APP_NAME,APP_VERSION,AUTHOR

app=FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="API pour assistant vocal avec données CSV")

@app.get("/")
def say_hello():
    return {"message":'hello'}