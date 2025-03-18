from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import spacy
import os

app = FastAPI()

# Charger le modèle NLP de spaCy
nlp = spacy.load("fr_core_news_sm")

# Clé API temporaire (remplace ça par une gestion dynamique plus tard)
API_KEY = os.getenv("API_KEY", "dev-ai-secret-key")

class TextRequest(BaseModel):
    texte: str

def verifier_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Clé API invalide")

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API NLP de dev-ai.fr"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/analyse-texte")
def analyse_texte(request: TextRequest, api_key: str = Header(None)):
    verifier_api_key(api_key)
    
    doc = nlp(request.texte)
    tokens = [token.text for token in doc]
    entites = [{"texte": ent.text, "label": ent.label_} for ent in doc.ents]

    return {
        "tokens": tokens,
        "entites": entites
    }

@app.post("/detect-langue")
def detect_langue(request: TextRequest, api_key: str = Header(None)):
    verifier_api_key(api_key)
    
    doc = nlp(request.texte)
    return {"langue_detectee": doc.lang_}