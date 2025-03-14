import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("database/YOURFILENAME.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOURDATABASEURL'
})


def save_note(title, content, ip, country, localtime):
    ref = db.reference("notes")
    new_note = ref.push({"title": title, "content": content, "ip": ip, "country": country, "localtime": localtime})
    return new_note.key

def load_notes():
    ref = db.reference("notes")
    notes = ref.get()
    if notes:
        return [{"id": key, "title": note.get("title", "Untitled"), "content": note.get("content", "")} for key, note in notes.items()]
    return []