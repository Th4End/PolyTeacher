# Étape 1 : Utilisation de l'image Python officielle
FROM python:3.10

# Étape 2 : rajouter sa clée d'api gemini
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_API_KEY # votre clé API
# Étape 3 : Copier le fichier requirements.txt et installer les dépendances Python
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# # Étape 4 : Copier l'ensemble du code source de l'application
# COPY . /app
# WORKDIR /app

# Étape 5 : Exposer le port 8000 pour l'application Django
EXPOSE 8000

# Étape 6 : Lancer l'application avec la commande de développement Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
