import google.generativeai as genai

# Configuration initiale de l'API
api_key = "AIzaSyDqDV3MkEtHqpefhNh__nE5HQjOPhBCXE0"  # Assurez-vous que cette clé est valide
genai.configure(api_key=api_key)

def translate(prompt):
    """
    Utilise le modèle Gemini pour traduire un texte en fonction du prompt donné.

    Args:
        prompt (str): Le texte et les instructions pour la traduction.

    Returns:
        str: Le texte traduit.

    Raises:
        ValueError: Si le modèle ne peut pas traiter la requête.
    """
    try:
        # Charger le modèle
        model = genai.GenerativeModel("gemini-1.5-flash")
        # Générer la traduction
        response = model.generate_content(prompt)
        return response.text  # Retourne le texte traduit
    except Exception as e:
        # Gérer les erreurs et renvoyer une exception descriptive
        raise ValueError(f"Erreur lors de la traduction avec Gemini : {e}")
