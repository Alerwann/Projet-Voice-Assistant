# Image de base Python
FROM python:3.11-slim

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier tout le code
COPY . .

# Commande pour démarrer l'API
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8080"]