# Notivo - Note Sharing Application

Notivo is a simple and intuitive note-sharing application where users can create, view, and manage their notes. This application allows users to submit notes with titles and content, ensuring that the majority of offensive or prohibited words are not included. The notes are stored remotely in a Firebase database for persistent storage. The app is built using **PyQt5** for the user interface.

<img src="https://i.imgur.com/OgmXaBG.png" width=50% height=50%>

---
## Features

- **Create Notes**: Users can submit notes with titles and content.
- **Refresh Notes**: Refresh to see the latest saved notes.
- **Prohibited Words Filter**: Ensures no offensive or banned words are submitted.
- **Submit Notes with Enter**: Notes can be submitted by pressing the "Enter" key.
- **Responsive UI**: Built with PyQt5, providing a user-friendly interface with a scrollable area for displaying notes.

---

## Prerequisites

Before running the project, make sure you have the following software installed:

- Python 3.x
- PyQt5
- Firebase (for database interaction)

You can install the required Python packages using `pip`:

```bash
pip install pyqt5
pip install firebase-admin
```

---

## Firebase Setup

1. Create a Firebase project if you don't have one.
2. Setup a **Realtime Database** in the build tab.
3. Download your **Firebase private key** and place it in the database folder and change the **YOURFILENAME** in the **firebase.py** file to your file name.
4. In the **firebase.py** file replace **YOURDATABASEURL** with your firebase project database url.
    ```
    cred = credentials.Certificate("database/YOURFILENAME.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'YOURDATABASEURL'
    })
    ```

---

## Usage

### 1. **Run the Application:**
After setting up, you can run the application by executing the main Python file:
    
    python main.py


### 2. **Submit Notes:**
- Enter a title and content for the note.
- Press the "Submit" button or hit the Enter key to submit your note.

### 3. **Refresh Notes:**
- Click the **REFRESH** button to load the most recent notes from the database.

---
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Balionelis/Notivo/blob/main/LICENSE) file for details.
