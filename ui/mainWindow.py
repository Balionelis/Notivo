from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QFrame, QLabel, QWidget, QMessageBox, QShortcut
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QKeySequence
from database.firebase import save_note, load_notes
from utils import load_banned_words
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.banned_words = load_banned_words()

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(244, 234, 224);")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.layout = QVBoxLayout(self.centralwidget)

        self.topname = QLabel("NOTIVO", self.centralwidget)
        self.topname.setFont(QtGui.QFont("Yu Gothic Medium", 36))
        self.layout.addWidget(self.topname, alignment=QtCore.Qt.AlignHCenter)

        self.refresh = QtWidgets.QPushButton("REFRESH", self.centralwidget)
        self.refresh.setStyleSheet("background-color: rgb(182, 141, 64);")
        self.refresh.clicked.connect(self.refresh_notes)
        self.layout.addWidget(self.refresh, alignment=QtCore.Qt.AlignHCenter)

        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setWidgetResizable(True)
        self.notes_container = QWidget()
        self.notes_layout = QVBoxLayout(self.notes_container)
        self.scroll_area.setWidget(self.notes_container)
        self.layout.addWidget(self.scroll_area)

        self.inputtext = QtWidgets.QLineEdit(self.centralwidget)
        self.inputtext.setFont(QtGui.QFont("Yu Gothic Medium", 12))
        self.inputtext.setStyleSheet("background-color: rgb(182, 141, 64);")
        self.inputtext.setPlaceholderText("Enter Text")
        self.layout.addWidget(self.inputtext, alignment=QtCore.Qt.AlignHCenter)
        
        self.inputtitle = QtWidgets.QLineEdit(self.centralwidget)
        self.inputtitle.setFont(QtGui.QFont("Yu Gothic Medium", 12))
        self.inputtitle.setStyleSheet("background-color: rgb(182, 141, 64);")
        self.inputtitle.setPlaceholderText("Enter Title")
        self.layout.addWidget(self.inputtitle, alignment=QtCore.Qt.AlignHCenter)

        self.submit = QtWidgets.QPushButton("SUBMIT", self.centralwidget)
        self.submit.setStyleSheet("background-color: rgb(182, 141, 64);")
        self.submit.clicked.connect(self.on_submit_click)
        self.layout.addWidget(self.submit, alignment=QtCore.Qt.AlignHCenter)

        self.label = QLabel("Enter text above", self.centralwidget)
        self.label.setFont(QtGui.QFont("Yu Gothic Medium", 14))
        self.layout.addWidget(self.label, alignment=QtCore.Qt.AlignHCenter)

        self.submit_shortcut = QShortcut(QKeySequence(QtCore.Qt.Key_Return), self)
        self.submit_shortcut.activated.connect(self.on_submit_click)

        self.refresh_notes()

    def on_submit_click(self):
        text = self.inputtext.text().strip().lower()
        title = self.inputtitle.text().strip().lower()

        if any(word in text or word in title for word in self.banned_words):
            self.show_popup("Your note contains prohibited words! \nPlease remove them before submitting.")
            return

        if text and title:
            self.submit.setEnabled(False)
            self.submit.setText("Please wait before submitting...")
            QTimer.singleShot(10000, self.enable_submit)

            note_id = save_note(title, text)
            self.label.setText(f"Note saved with ID {note_id}")
            self.inputtext.clear()
            self.inputtitle.clear()

            self.refresh_notes()
        else:
            self.label.setText("ERROR! Enter text and title")

    def enable_submit(self):
        self.submit.setEnabled(True)
        self.submit.setText("SUBMIT")

    def show_popup(self, message):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(message)
        popup.setIcon(QMessageBox.Warning)
        popup.exec_()

    def refresh_notes(self):
        for i in reversed(range(self.notes_layout.count())):
            widget = self.notes_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        notes = load_notes()
        for note in notes:
            self.add_note_widget(note["title"], note["content"])

    def add_note_widget(self, title, content):
        note_frame = QFrame(self.notes_container)
        note_frame.setStyleSheet("""
            QFrame {
                border: 2px solid #aaa;
                border-radius: 10px;
                background-color: #f9f9f9;
            }
        """)
        note_layout = QVBoxLayout(note_frame)

        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        note_layout.addWidget(title_label)

        content_label = QLabel(content, self)
        content_label.setWordWrap(True)
        note_layout.addWidget(content_label)

        self.notes_layout.addWidget(note_frame)

        self.notes_layout.addStretch()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
