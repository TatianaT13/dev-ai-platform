from fastapi import Header, HTTPException
import os

API_KEY = os.getenv("API_KEY", "default_api_key")

def verify_api_key(x_api_key: str = Header(...)):
    print(f"Clé reçue: {x_api_key}, Clé attendue: {API_KEY}")  # Debug
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Clé API invalide")
    return True