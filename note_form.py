from PyQt6 import QtCore, QtWidgets


class Ui_NoteForm(object):
    def setupUi(self, NoteForm):
        NoteForm.setObjectName("NoteForm")
        NoteForm.resize(300, 400)

        self.verticalLayout = QtWidgets.QVBoxLayout(NoteForm)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalWidget = QtWidgets.QWidget(parent=NoteForm)
        self.horizontalWidget.setObjectName("horizontalWidget")

        self.titleLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.titleLayout.setObjectName("titleLayout")

        self.titleLabel = QtWidgets.QLabel(parent=self.horizontalWidget)
        self.titleLabel.setObjectName("titleLabel")

        self.titleLayout.addWidget(self.titleLabel)

        self.titleLineEdit = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        self.titleLineEdit.setObjectName("titleLineEdit")

        self.titleLayout.addWidget(self.titleLineEdit)

        self.verticalLayout.addWidget(self.horizontalWidget)

        self.textEdit = QtWidgets.QTextEdit(parent=NoteForm)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.footerWidget = QtWidgets.QWidget(parent=NoteForm)
        self.footerWidget.setObjectName("footerWidget")

        self.buttonsHorizontalLayout = QtWidgets.QHBoxLayout(self.footerWidget)
        self.buttonsHorizontalLayout.setObjectName("buttonsHorizontalLayout")

        self.savePushButton = QtWidgets.QPushButton(parent=self.footerWidget)
        self.savePushButton.setObjectName("savePushButton")

        self.buttonsHorizontalLayout.addWidget(self.savePushButton)

        self.deletePushButton = QtWidgets.QPushButton(parent=self.footerWidget)
        self.deletePushButton.setObjectName("deletePushButton")

        self.buttonsHorizontalLayout.addWidget(self.deletePushButton)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.buttonsHorizontalLayout.addItem(spacerItem)

        self.verticalLayout.addWidget(self.footerWidget)

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
            QLineEdit {
                background-color: #222222;
                border: none;
            }
            QTextEdit {
                background-color: #222222;
                border: none;
            }
        """
        NoteForm.setStyleSheet(stylesheet)

        self.retranslateUi(NoteForm)
        QtCore.QMetaObject.connectSlotsByName(NoteForm)

    def retranslateUi(self, NoteForm):
        _translate = QtCore.QCoreApplication.translate
        NoteForm.setWindowTitle(_translate("NoteForm", "Note"))
        self.titleLabel.setText(_translate("NoteForm", "Title:"))
        self.savePushButton.setText(_translate("NoteForm", "Save"))
        self.deletePushButton.setText(_translate("NoteForm", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoteForm = QtWidgets.QWidget()
    ui = Ui_NoteForm()
    ui.setupUi(NoteForm)
    NoteForm.show()
    sys.exit(app.exec())
