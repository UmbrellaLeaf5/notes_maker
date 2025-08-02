from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow:
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(500, 600)

    self.horizontalWidget = QtWidgets.QWidget(parent=MainWindow)
    sizePolicy = QtWidgets.QSizePolicy(
      QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
    )

    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())

    self.horizontalWidget.setSizePolicy(sizePolicy)
    self.horizontalWidget.setObjectName("horizontalWidget")

    self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
    self.horizontalLayout.setObjectName("horizontalLayout")

    self.notesListWidget = QtWidgets.QListWidget(parent=self.horizontalWidget)
    self.notesListWidget.setObjectName("notesListWidget")
    self.horizontalLayout.addWidget(self.notesListWidget)

    self.verticalLayout = QtWidgets.QVBoxLayout()
    self.verticalLayout.setObjectName("verticalLayout")

    spacerItem = QtWidgets.QSpacerItem(
      20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
    )
    self.verticalLayout.addItem(spacerItem)

    self.newPushButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
    sizePolicy = QtWidgets.QSizePolicy(
      QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
    )

    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    sizePolicy.setHeightForWidth(self.newPushButton.sizePolicy().hasHeightForWidth())
    self.newPushButton.setSizePolicy(sizePolicy)

    self.newPushButton.setObjectName("newPushButton")
    self.verticalLayout.addWidget(self.newPushButton)

    self.folderPushButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
    sizePolicy = QtWidgets.QSizePolicy(
      QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
    )

    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    sizePolicy.setHeightForWidth(self.folderPushButton.sizePolicy().hasHeightForWidth())
    self.folderPushButton.setSizePolicy(sizePolicy)

    self.folderPushButton.setObjectName("folderPushButton")
    self.verticalLayout.addWidget(self.folderPushButton)

    self.deletePushButton = QtWidgets.QPushButton(parent=self.horizontalWidget)
    self.deletePushButton.setEnabled(False)
    sizePolicy = QtWidgets.QSizePolicy(
      QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
    )

    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)

    sizePolicy.setHeightForWidth(self.deletePushButton.sizePolicy().hasHeightForWidth())
    self.deletePushButton.setSizePolicy(sizePolicy)

    self.deletePushButton.setObjectName("deletePushButton")
    self.verticalLayout.addWidget(self.deletePushButton)
    self.horizontalLayout.addLayout(self.verticalLayout)
    MainWindow.setCentralWidget(self.horizontalWidget)

    stylesheet = """
            QWidget {
                background-color: #151515;
                color: #ffffff;
            }
            QPushButton {
                background-color: #333333;
            }
            QPushButton:disabled {
                background-color: #222222;
                color: #888888;
            }
            QPushButton:hover {
                background-color: #444444;
            }
            QListWidget {
                background-color: #222222;
                border: none;
            }
            QListWidget::item:hover {
                background-color: #333333;
            }
            QListWidget::item:selected {
                background-color: #444444;
                color: #ffffff;
            }
        """
    MainWindow.setStyleSheet(stylesheet)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "NotesMaker"))
    self.newPushButton.setText(_translate("MainWindow", "New"))
    self.folderPushButton.setText(_translate("MainWindow", "Folder"))
    self.deletePushButton.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
  import sys

  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec())
