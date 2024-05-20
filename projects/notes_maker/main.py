from PyQt6 import QtWidgets

from mainwindow import Ui_MainWindow

from note import NoteWidget


class Window(QtWidgets.QMainWindow):

    __notes_list: list[NoteWidget]

    __untitled_counter: int

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__untitled_counter = 0
        self.__notes_list = []

        self.ui.newPushButton.clicked.connect(self.NewNote)

    def NewNote(self) -> None:
        self.__notes_list.append(NoteWidget())
        self.__notes_list[-1].show()

        self.__notes_list[-1].ui.deletePushButton.clicked.connect(self.DeleteNote)

        if (self.__untitled_counter == 0):
            self.ui.notesListWidget.addItem(f"UntitledNote")
        else:
            self.ui.notesListWidget.addItem(f"UntitledNote_{self.__untitled_counter}")

        self.__untitled_counter += 1

    def DeleteNote(self, index: int = -1) -> None:
        self.__notes_list.pop(index)
        self.ui.notesListWidget.takeItem(index)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec())
