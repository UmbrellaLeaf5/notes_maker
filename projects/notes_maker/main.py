from PyQt6 import QtWidgets

from mainwindow import Ui_MainWindow

from note import NoteWidget


class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.newPushButton.clicked.connect(self.NewNote)

    def NewNote(self) -> None:
        self.note = NoteWidget()
        self.note.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec())
