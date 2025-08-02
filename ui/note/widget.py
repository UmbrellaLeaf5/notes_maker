from PyQt6 import QtWidgets

from ui.note.form import Ui_NoteForm


class NoteWidget(QtWidgets.QWidget):
  __index: int

  def __init__(self, title: str = "", text: str = "", index: int = -1) -> None:
    super().__init__()

    self.__index = index

    self.ui = Ui_NoteForm()
    self.ui.setupUi(self)

    self.ui.titleLineEdit.setText(title)
    self.ui.textEdit.setText(text)

    self.ui.titleLineEdit.textChanged.connect(self.SetTitle)

  def SetTitle(self, title: str = "") -> None:
    self.ui.titleLineEdit.update()

    self.ui.titleLineEdit.setText(title)

  def SetText(self, text: str = "") -> None:
    self.ui.textEdit.update()

    self.ui.textEdit.setText(text)

  def SetIndex(self, index: int) -> None:
    self.__index = index

  def Title(self) -> str:
    self.ui.titleLineEdit.update()
    return self.ui.titleLineEdit.text()

  def Text(self) -> str:
    self.ui.textEdit.update()
    return self.ui.textEdit.toPlainText()

  def Index(self) -> int:
    return self.__index


if __name__ == "__main__":
  import sys

  app = QtWidgets.QApplication(sys.argv)
  note = NoteWidget()
  note.show()

  sys.exit(app.exec())
