# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# import json

# # Cargar las credenciales desde la variable de entorno
# firebase_credentials = os.environ.get("FIREBASE_CREDENTIALS")

# if firebase_credentials:
#     cred_dict = json.loads(firebase_credentials)
#     cred = credentials.Certificate(cred_dict)
#     firebase_admin.initialize_app(cred)
# else:
#     raise ValueError("Firebase credentials not found in environment variables")

# db = firestore.client()


import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Cargar la ruta de las credenciales desde la variable de entorno
firebase_credentials_path = os.environ.get("FIREBASE_CREDENTIALS")

if firebase_credentials_path and os.path.exists(firebase_credentials_path):
    # Leer las credenciales desde el archivo
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)
else:
    raise ValueError(f"Firebase credentials file {firebase_credentials_path} not found or path not set in environment variables")

# Inicializar Firestore
db = firestore.client()

# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# import json

# # Cargar las credenciales desde la variable de entorno
# firebase_credentials = os.environ.get("FIREBASE_CREDENTIALS")

# if firebase_credentials:
#     cred_dict = json.loads(firebase_credentials)
#     cred = credentials.Certificate(cred_dict)
#     firebase_admin.initialize_app(cred)
# else:
#     raise ValueError("Firebase credentials not found in environment variables")

# db = firestore.client()