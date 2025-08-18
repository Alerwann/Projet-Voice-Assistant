from logique.csv_reader import get_all_information

def generate_voice_response(day=None):
    """
    Génère les phrases réponse selon le jour.
    Si l'utilisateur ne donne pas de date, donne les informations d'aujourd'hui

    Args:
       day(str): un jour précis demandé par l'utilisateur.
       day a comme valeur par défaut None

    Returns :
        response_to_say{str,str,str,str} ->
           exemple {'midi': midi_meal,
                 'soir': evening_meal,
                 'rendez-vous': meeting,
                 "global": resume_complet}
    """
    infos = get_all_information(day)

    midi_meal = f"Pour le midi, tu manges {infos['midi']}"
    evening_meal = f"Pour le soir, tu manges {infos['soir']}"
    meeting = f"Tu as {infos['rendez-vous']}"
    resume_complet = f'{midi_meal}. {evening_meal}.{meeting}'

    response_to_say={'midi': midi_meal,
                     'soir': evening_meal,
                     'rendez-vous': meeting, 
                     "global": resume_complet}

    return response_to_say
