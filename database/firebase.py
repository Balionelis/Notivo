import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("database/firebasenotivo.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://notivo250216-default-rtdb.europe-west1.firebasedatabase.app/'
})


def save_note(note_text):
    ref = db.reference("notes")
    new_note = ref.push({"text": note_text}) 
    return new_note.key
