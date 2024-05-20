from PyQt6 import QtWidgets, QtGui

from mainwindow import Ui_MainWindow

from note import NoteWidget


class Window(QtWidgets.QMainWindow):

    __notes_list: list[NoteWidget]
    __folder: str
    __untitled_counter: int
    __current_index: int = 0

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__untitled_counter = 0
        self.__notes_list = []
        self.__folder = ""

        self.ui.newPushButton.clicked.connect(self.NewNote)
        self.ui.folderPushButton.clicked.connect(self.SelectFolder)
        self.ui.deletePushButton.clicked.connect(self.DeleteNote)

        self.ui.notesListWidget.itemDoubleClicked.connect(self.OpenNote)

        self.ui.notesListWidget.itemClicked.connect(self.DeleteNoteBySelection)

        self.ui.notesListWidget.itemSelectionChanged.connect(
            lambda: self.ui.deletePushButton.setEnabled(False))

    def NewNote(self, action_stub, need_open: bool = True, title: str = "") -> None:
        self.__current_index = -1

        self.__notes_list.append(NoteWidget())

        self.__notes_list[self.__current_index].ui.deletePushButton.clicked.connect(self.DeleteNote)

        if (need_open):
            self.__notes_list[self.__current_index].show()

        if (title == ""):
            title = "UntitledNote"

            if (self.__untitled_counter):
                title = f"UntitledNote_{self.__untitled_counter}"

        self.ui.notesListWidget.addItem(title)
        self.__notes_list[self.__current_index].ui.titleLineEdit.setText(title)

        if (self.__folder == ""):
            self.SelectFolder()

        self.SaveNote()

        self.__untitled_counter += 1

    def DeleteNote(self) -> None:
        self.ui.notesListWidget.takeItem(self.__current_index)

        import os
        file = os.path.join(
            self.__folder, self.__notes_list[self.__current_index].ui.titleLineEdit.text())
        os.remove(file + ".txt")

        self.__notes_list.pop(self.__current_index)

    def OpenNote(self, item: QtWidgets.QListWidgetItem):
        self.__current_index = self.ui.notesListWidget.row(item)
        self.__notes_list[self.__current_index].show()

        self.__notes_list[self.__current_index].ui.deletePushButton.clicked.connect(self.DeleteNote)
        self.__notes_list[self.__current_index].ui.savePushButton.clicked.connect(self.SaveNote)

    def SaveNote(self):
        file_name = self.__notes_list[self.__current_index].ui.titleLineEdit.text()

        import os
        os.makedirs(self.__folder, exist_ok=True)

        file_path = os.path.join(self.__folder, file_name)

        if (file_path[-4:] != ".txt"):
            file_path += ".txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.__notes_list[self.__current_index].ui.textEdit.toPlainText())

    def SelectFolder(self):
        self.__folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select folder", "")

        if self.__folder:
            self.UpdateNotesList()

    def DeleteNoteBySelection(self, item: QtWidgets.QListWidgetItem):
        self.__current_index = self.ui.notesListWidget.row(item)
        self.ui.deletePushButton.setEnabled(True)

    def UpdateNotesList(self):
        self.ui.notesListWidget.clear()
        self.__notes_list.clear()

        import os
        files = os.listdir(self.__folder)

        txt_files = [f for f in files if f.endswith('.txt')]

        for txt_file in txt_files:
            self.NewNote(0, False, txt_file[:-4])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    icon = QtGui.QIcon('icon.png')
    app.setWindowIcon(icon)

    window = Window()
    window.show()

    sys.exit(app.exec())
