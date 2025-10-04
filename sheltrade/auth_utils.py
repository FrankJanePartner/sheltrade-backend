import os
import requests
from jose import jwt

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")  # Get this from Supabase > Project Settings > API

def verify_supabase_jwt(token):
    try:
        payload = jwt.decode(token, SUPABASE_JWT_SECRET, algorithms=["HS256"])
        return payload
    except Exception as e:
        print("JWT verification failed:", e)
        return None
