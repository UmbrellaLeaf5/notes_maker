from PyQt6 import QtWidgets

from note_form import Ui_NoteForm


class NoteWidget(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_NoteForm()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    note = NoteWidget()
    note.show()

    sys.exit(app.exec())
