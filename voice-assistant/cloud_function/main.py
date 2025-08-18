import sys
import os
import json


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logique.menu_handler import generate_voice_response

def voice_assistant_handler(request):
    """
    Point d'entrée de la Cloud Function
    Reçoit les requêtes Google Assistant
    """
    # Parser le JSON reçu de Google Assistant
    request_json = request.get_json()

    # Vérifier que la requête contient bien les données
    if not request_json:
        return {"fulfillmentText": "Erreur: pas de données reçues"}

    # Extraire l'intent de la requête
    intent = request_json.get("intent")

    if not intent:
        return {"fulfillmentText": "Désolé je n'ai pas compris votre demande"}

    response=generate_voice_response(day=None)

    # différents choix de réponses
    if intent == "repas_midi":
        return {"fulfillmentText":response['midi']}
    elif intent == "repas_soir":
        return {"fulfillmentText": response["soir"]}
    elif intent == "rendezvous":
        return {"fulfillmentText": response["rendez-vous"]}
    elif intent == "global":
        return {"fulfillmentText": response["global"]}
    else:
        return {"message": "Intent non reconnu"}