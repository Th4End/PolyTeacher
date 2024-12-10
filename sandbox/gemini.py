import google.generativeai as genai

try:
    api_key = "AIzaSyDFLzQgss7hiZkouMA7eXkuDjqRiVdnZBc"  # Remplacez par une clé API valide
    genai.configure(api_key=api_key)

    # Sélectionnez un modèle valide
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(str(input()))
    print(response.text)
except EOFError:
    print(False)
