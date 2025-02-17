import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("database/firebasenotivo.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://notivo250216-default-rtdb.europe-west1.firebasedatabase.app/'
})


def save_note(title, content):
    ref = db.reference("notes")
    new_note = ref.push({"title": title, "content": content})
    return new_note.key

def load_notes():
    ref = db.reference("notes")
    notes = ref.get()
    if notes:
        return [{"id": key, "title": note.get("title", "Untitled"), "content": note.get("content", "")} for key, note in notes.items()]
    return []