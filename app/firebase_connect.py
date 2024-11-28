
# import firebase_admin
# from firebase_admin import credentials, firestore
# import os
# import json
# from dotenv import load_dotenv
# load_dotenv() 

# firebase_key_contents = os.getenv('FIREBASE_KEY_CONTENTS')
# if not firebase_key_contents:
#     raise ValueError("The FIREBASE_KEY_CONTENTS environment variable is not set.")
# try:
#     firebase_key_dict = json.loads(firebase_key_contents)
# except json.JSONDecodeError as e:
#     raise ValueError("The FIREBASE_KEY_CONTENTS environment variable is not a valid JSON.") from e

# cred = credentials.Certificate(firebase_key_dict)
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# def get_firestore_client():
#     """Returns the Firestore client instance."""
#     return db

import firebase_admin
from firebase_admin import credentials, firestore
import json

# Path to your Firebase service account JSON file
firebase_key_path = r'C:\Users\mohammed afrik\Desktop\Todo\todo\app\firebase_key.json'


# Load the credentials from the JSON file
cred = credentials.Certificate(firebase_key_path)

# Initialize the Firebase admin app with the credentials
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

def get_firestore_client():
    """Returns the Firestore client instance."""
    return db

