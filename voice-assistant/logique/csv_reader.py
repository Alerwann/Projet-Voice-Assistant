import locale
import sys
import os
import csv
import datetime as dt


locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.settings import CSV_PATH

def download_planning_csv():
    """
    Importe le fichier cvs du planning de la semaine

    Utilise CSV pour le traitement du fichier et convertir chaque ligne en dict

    Returns:
        list[Dict|str,str]] contenant les infos de chaque jour: Menu du midi, Menu du soir, Rendez-vous, Crème du soir, Mot doux

    Raises:
        FileNotFoundError: Si le fichier CSV n'existe pas
    """
    planning = []
    with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            planning.append(dict(row))  # Convertir en dict normal
    return planning


def get_daily_information(day_name):
    """
    Récupère les informations de planning pour un jour donné.

     Args:
         day_name (str): Nom du jour de la semaine (ex: "lundi")

     Returns :

         Dict[str, str]: Dictionnaire contenant les infos du jour
         ou dictionnaire vide si pas trouvé
    """
    planning = download_planning_csv()
    for jour in planning:
        if jour["Jour"].lower() == day_name.lower():
            return jour
    return {}

def get_all_information(day=None):
    """
    Récupère toutes les informations pour un jour donné.

    Args:
        day (str, optional): Jour spécifique, sinon aujourd'hui

    Returns:
        dict: Toutes les informations du jour formatées

    Example:
        >>> get_all_information()
        {
            'jour': 'lundi',
            'midi': 'pâtes carbonara',
            'soir': 'salade de quinoa',
            'rendezvous': 'médecin 14h'
        }
    """

    if day is None:
        current_day = dt.date.today().strftime("%A").lower()
    else:
        current_day = day.lower()

    daily_planning = get_daily_information(current_day)

    midi = daily_planning.get("Menu du midi", "").strip() or "Pas de repas"
    evening = daily_planning.get("Menu du soir", "").strip() or "Pas de repas "
    meeting = daily_planning.get("Rendez-vous", "").strip() or "aucun rendez-vous"

    message={
        'jour' : current_day,
        'midi' : midi,
        'soir' : evening,
        'rendez-vous': meeting
        }

    return message


    

