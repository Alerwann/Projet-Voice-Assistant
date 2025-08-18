from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.menu_handler import generate_voice_response
from config.settings import APP_NAME,APP_VERSION,AUTHOR

class GoogleRequest(BaseModel):
    intent:str

app=FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="API pour assistant vocal avec données CSV")

@app.get("/")
# """route de teste"""
def say_hello():
    return {"message":'hello'}


@app.post("/webhook")
# recupere la demande de gogole et envoie la réponse adapté
def get_type_request(request: GoogleRequest):
    response=generate_voice_response(day=None)

    # différents choix de réponses
    if request.intent == "repas_midi":
        return {"fulfillmentText":response['midi']}
    elif request.intent == "repas_soir":
        return {"fulfillmentText": response["soir"]}
    elif request.intent == "rendezvous":
        return {"fulfillmentText": response["rendez-vous"]}
    elif request.intent == "global":
        return {"fulfillmentText": response["global"]}
    else:
        return {"message": "Intent non reconnu"}


