from fastapi import FastAPI
import spacy

app = FastAPI()

# Charger le modèle NLP français
nlp = spacy.load("fr_core_news_sm")

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API NLP de dev-ai.fr"}

@app.post("/analyze_sentiment/")
def analyze_sentiment(text: str):
    doc = nlp(text)
    return {"text": text, "sentiment": "positif" if "bien" in text else "négatif"}

@app.post("/extract_entities/")
def extract_entities(text: str):
    doc = nlp(text)
    return {"entities": [{"text": ent.text, "label": ent.label_} for ent in doc.ents]}