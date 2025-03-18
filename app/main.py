from fastapi import FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import spacy
import os

# Initialisation de l'application FastAPI
app = FastAPI()

# Clé API pour authentification
API_KEY = "ma_clé_secrète"

# Chargement du modèle NLP avec gestion des erreurs
try:
    nlp = spacy.load("fr_core_news_sm")
except Exception as e:
    raise RuntimeError(f"Erreur lors du chargement du modèle NLP: {e}")

# Servir les fichiers statiques pour le frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Modèle de requête attendu
class TextRequest(BaseModel):
    text: str

@app.get("/")
def serve_home():
    """Retourne l'interface utilisateur HTML"""
    return FileResponse(os.path.join("frontend", "index.html"))

@app.post("/analyze")
def analyze_text(request: TextRequest, x_api_key: str = Header(None)):
    """Analyse NLP du texte avec nettoyage."""
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Clé API invalide")

    # Analyse NLP avec spaCy
    doc = nlp(request.text.strip())

    tokens = [token.text for token in doc if not token.is_space]
    lemmas = [token.lemma_ for token in doc if not token.is_space]
    pos_tags = [token.pos_ for token in doc if not token.is_space]

    return {
        "tokens": tokens,
        "lemmas": lemmas,
        "pos_tags": pos_tags
    }