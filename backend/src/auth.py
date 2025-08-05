import requests
from fastapi import HTTPException

def verify_google_token(token:str):
    response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
    if response.status_code != 20:
        raise HTTPException(status_code=401,detail="Invalid Google token")
    return response.json()