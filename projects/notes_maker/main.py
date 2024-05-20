import os

from PyQt6 import QtWidgets, QtGui

from mainwindow import Ui_MainWindow
from notewidget import NoteWidget


class Window(QtWidgets.QMainWindow):

    __notes_list: list[NoteWidget]
    __folder: str

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__notes_list = []
        self.__folder = ""

        self.ui.newPushButton.clicked.connect(self.NewNote)
        self.ui.folderPushButton.clicked.connect(self.SelectFolder)

        self.ui.notesListWidget.itemDoubleClicked.connect(self.OpenNote)

        self.ui.notesListWidget.itemClicked.connect(self.ConnectDeleteBySelection)

        self.ui.notesListWidget.itemSelectionChanged.connect(
            lambda: self.ui.deletePushButton.setEnabled(False))

    def NewNote(self, action_stub, need_open: bool = True, title: str = "", text: str = "") -> None:
        # если не установлена папка, спрашиваем её
        if (self.__folder == ""):
            self.SelectFolder()

        # если название не было передано, то это новая метка
        if (title == ""):
            title = "UntitledNote"
            print(self.MaxUntitledNoteNumber())

            if (self.MaxUntitledNoteNumber() >= 0):
                title = f"UntitledNote_{self.MaxUntitledNoteNumber() + 1}"

        new_note = NoteWidget(title, text, len(self.__notes_list))

        # print("NEW: ", new_note.Index(), len(self.__notes_list))

        new_note.SetTitle(title)
        new_note.SetText(text)

        self.ui.notesListWidget.addItem(title)
        self.__notes_list.append(new_note)

        self.SaveNote(new_note.Index())

        self.__notes_list[new_note.Index()].ui.deletePushButton.clicked.connect(
            lambda: self.DeleteNote(new_note.Index()))

        self.__notes_list[new_note.Index()].ui.savePushButton.clicked.connect(
            lambda: self.SaveNote(new_note.Index()))

        # открытие в конце
        if (need_open):
            self.__notes_list[new_note.Index()].show()

    def ConnectDeleteBySelection(self, item: QtWidgets.QListWidgetItem) -> None:
        if (self.ui.deletePushButton.receivers(self.ui.deletePushButton.clicked)):
            self.ui.deletePushButton.clicked.disconnect()

        self.ui.deletePushButton.setEnabled(True)
        # print("SELECTION: ", self.ui.notesListWidget.row(item), len(self.__notes_list))

        self.ui.deletePushButton.clicked.connect(
            lambda: self.DeleteNote(self.ui.notesListWidget.row(item)))

    def DeleteNote(self, index: int = -1) -> None:
        # print("DELETE: ", index, len(self.__notes_list))

        file = os.path.join(
            self.__folder, self.__notes_list[index].Title())
        os.remove(file + ".txt")

        self.ui.notesListWidget.takeItem(index)
        self.ui.notesListWidget.update()

        self.__notes_list[index].setVisible(False)
        self.__notes_list.pop(index)

        for i in range(len(self.__notes_list)):
            self.__notes_list[i].SetIndex(i)

    def OpenNote(self, item: QtWidgets.QListWidgetItem) -> None:
        index = self.ui.notesListWidget.row(item)

        # print("OPEN: ", index, len(self.__notes_list))

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
        # print("SAVE: ", index, len(self.__notes_list))

        file_name = self.__notes_list[index].Title()

        os.makedirs(self.__folder, exist_ok=True)
        file_path = os.path.join(self.__folder, file_name)

        if (file_path[-4:] != ".txt"):
            file_path += ".txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(self.__notes_list[index].Text())

        if (self.ui.notesListWidget.item(index).text() != self.__notes_list[index].Title()):
            file_path = os.path.join(
                self.__folder, self.ui.notesListWidget.item(index).text() + ".txt")
            os.remove(file_path)
            self.ui.notesListWidget.item(index).setText(self.__notes_list[index].Title())

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
            pass  # yeah, nothing, lol

    def MaxUntitledNoteNumber(self):
        note_files = [f for f in os.listdir(self.__folder) if f.startswith(
            "UntitledNote") and f.endswith(".txt")]

        if not note_files:
            return -1

        if len(note_files) == 1 and note_files[0] == "UntitledNote.txt":
            return 0

        # извлекаем номера из файлов и находим максимальный
        numbers = []
        for f in note_files:
            if "_" in f:
                try:
                    num = int(f.split("_")[1].split(".")[0])
                    numbers.append(num)
                except (IndexError, ValueError):
                    pass

        return max(numbers)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    icon = QtGui.QIcon('icon.png')
    app.setWindowIcon(icon)

    window = Window()
    window.show()

    sys.exit(app.exec())
