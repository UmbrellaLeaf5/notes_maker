import re
import os

from PyQt6 import QtWidgets, QtGui

from mainwindow import Ui_MainWindow
from notewidget import NoteWidget


class Window(QtWidgets.QMainWindow):

    __notes_list: list[NoteWidget]
    __folder: str
    __untitled_counter: int

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__untitled_counter = 0
        self.__notes_list = []
        self.__folder = ""

        self.ui.newPushButton.clicked.connect(self.NewNote)
        self.ui.folderPushButton.clicked.connect(self.SelectFolder)

        self.ui.notesListWidget.itemDoubleClicked.connect(self.OpenNote)

        self.ui.notesListWidget.itemEntered.connect(self.DeleteNoteBySelection)

        self.ui.notesListWidget.itemSelectionChanged.connect(
            lambda: self.ui.deletePushButton.setEnabled(False))

    def NewNote(self, action_stub, need_open: bool = True, title: str = "", text: str = "") -> None:
        index = len(self.__notes_list)

        print("NEW: ", index, len(self.__notes_list))

        if (self.__folder == ""):
            self.SelectFolder()

        new_note = NoteWidget()

        self.__untitled_counter = self.MaxUntitledNoteNumber() + 1

        if (title == ""):
            title = "UntitledNote"

            if (self.__untitled_counter):
                title = f"UntitledNote_{self.__untitled_counter}"

        new_note.SetTitle(title)
        new_note.SetText(text)

        self.ui.notesListWidget.addItem(title)
        self.__notes_list.append(new_note)

        self.SaveNote(index)

        self.__notes_list[index].ui.deletePushButton.clicked.connect(lambda: self.DeleteNote(index))
        self.__notes_list[index].ui.savePushButton.clicked.connect(lambda: self.SaveNote(index))

        # открытие в конце
        if (need_open):
            self.__notes_list[index].show()

    def DeleteNoteBySelection(self, item: QtWidgets.QListWidgetItem) -> None:
        index = self.ui.notesListWidget.row(item)
        self.ui.deletePushButton.setEnabled(True)
        self.ui.deletePushButton.clicked.connect(lambda: self.DeleteNote(index))

    def DeleteNote(self, index: int = -1) -> None:
        print("DELETE: ", index, len(self.__notes_list))

        file = os.path.join(
            self.__folder, self.__notes_list[index].Title())
        os.remove(file + ".txt")

        self.ui.notesListWidget.takeItem(index)
        self.ui.notesListWidget.update()

        self.__notes_list[index].setVisible(False)

        self.__notes_list.pop(index)

    def OpenNote(self, item: QtWidgets.QListWidgetItem) -> None:
        index = self.ui.notesListWidget.row(item)

        print("OPEN: ", index, len(self.__notes_list))

        file_name = self.__notes_list[index].Title()

        os.makedirs(self.__folder, exist_ok=True)
        file_path = os.path.join(self.__folder, file_name)

        if (file_path[-4:] != ".txt"):
            file_path += ".txt"

        with open(file_path, 'r', encoding='utf-8') as file:
            self.__notes_list[index].SetText(file.read())

        # открытие в конце
        self.__notes_list[index].show()

    def SaveNote(self, index) -> None:
        print("SAVE: ", index, len(self.__notes_list))

        file_name = self.__notes_list[index].Title()

        os.makedirs(self.__folder, exist_ok=True)
        file_path = os.path.join(self.__folder, file_name)

        if (file_path[-4:] != ".txt"):
            file_path += ".txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.__notes_list[index].Text())

        # if (self.ui.notesListWidget.item(index).text() != self.__notes_list[index].Title()):
        #     self.ui.notesListWidget.item(index).setText(self.__notes_list[index].Title())
        #     os.remove(self.ui.notesListWidget.item(index).text() + ".txt")

    def SelectFolder(self) -> None:
        self.__folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select folder", "")

        if self.__folder:
            self.UpdateNotesList()

    def UpdateNotesList(self) -> None:
        self.ui.notesListWidget.clear()
        self.__notes_list.clear()

        try:
            files = os.listdir(self.__folder)
            txt_files = [f for f in files if f.endswith('.txt')]

            for txt_file in txt_files:
                file_path = os.path.join(self.__folder, txt_file)

                with open(file_path, 'r', encoding='utf-8') as file:
                    file_text = file.read()

                self.NewNote(0, False, txt_file[:-4], file_text)

        except:
            """"""

    def MaxUntitledNoteNumber(self):
        untitled_note_pattern = re.compile(r'UntitledNote_(\d+)\.txt')
        max_number = 0

        for filename in os.listdir(self.__folder):
            match = untitled_note_pattern.match(filename)
            if match:
                number = int(match.group(1))
                if number > max_number:
                    max_number = number

        return max_number


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    icon = QtGui.QIcon('icon.png')
    app.setWindowIcon(icon)

    window = Window()
    window.show()

    sys.exit(app.exec())
