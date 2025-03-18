from fastapi import APIRouter
import spacy

nlp = spacy.load("fr_core_news_sm")

nlp_endpoint = APIRouter()

@nlp_endpoint.post("/analyze")
async def analyze_text(text: str):
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}