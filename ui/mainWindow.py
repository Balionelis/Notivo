from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from database.firebase import save_note
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(244, 234, 224);")

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.topname = QtWidgets.QLabel("NOTIVO", self.centralwidget)
        self.topname.setGeometry(QtCore.QRect(310, 0, 181, 51))
        font = QtGui.QFont("Yu Gothic Medium", 36)
        self.topname.setFont(font)

        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(320, 410, 171, 41))
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setStyleSheet("background-color: rgb(182, 141, 64);")

        self.submit = QtWidgets.QPushButton("SUBMIT", self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(350, 470, 111, 31))
        self.submit.setStyleSheet("background-color: rgb(182, 141, 64);")

        self.label = QtWidgets.QLabel("Enter text above", self.centralwidget)
        self.label.setFont(QtGui.QFont("Yu Gothic Medium", 14))
        self.label.setGeometry(QtCore.QRect(320, 350, 200, 40))

        self.submit.clicked.connect(self.on_submit_click)

    def on_submit_click(self):
        text = self.input.text().strip()
        if text:
            self.submit.setEnabled(False)
            self.submit.setText("Please wait before submiting again...")
            QTimer.singleShot(2000, self.enable_submit)
            note_id = save_note(text)
            self.label.setText(f"Note saved with ID {note_id}")
            self.submit.adjustSize()
            self.submit.move(315, 470)
        else:
            self.label.setText("Enter something!")

    def enable_submit(self):
        self.submit.setEnabled(True)
        self.submit.setText("SUBMIT")

        self.label.adjustSize()


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
