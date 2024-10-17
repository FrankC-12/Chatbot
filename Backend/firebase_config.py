import os
import json
import firebase_admin
from firebase_admin import credentials

# Lee las credenciales desde la variable de entorno
firebase_credentials_json = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_credentials_json:
    raise ValueError("Firebase credentials not found in environment variables")

# Carga las credenciales desde el JSON
firebase_credentials = json.loads(firebase_credentials_json)

cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)