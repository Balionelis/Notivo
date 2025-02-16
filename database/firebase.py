import firebase_admin
from firebase_admin import credentials, db

# Load Firebase credentials
cred = credentials.Certificate("firebasenotivo.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://notivo250216-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Reference to the database
ref = db.reference('/')