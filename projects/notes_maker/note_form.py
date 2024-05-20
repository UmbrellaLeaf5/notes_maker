from PyQt6 import QtCore, QtWidgets


class Ui_NoteForm(object):
    def setupUi(self, noteForm):
        noteForm.setObjectName("noteForm")
        noteForm.resize(300, 400)

        self.verticalLayout = QtWidgets.QVBoxLayout(noteForm)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalWidget = QtWidgets.QWidget(parent=noteForm)
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

        self.textEdit = QtWidgets.QTextEdit(parent=noteForm)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.footerWidget = QtWidgets.QWidget(parent=noteForm)
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

        self.retranslateUi(noteForm)
        QtCore.QMetaObject.connectSlotsByName(noteForm)

    def retranslateUi(self, noteForm):
        _translate = QtCore.QCoreApplication.translate
        noteForm.setWindowTitle(_translate("noteForm", "Note"))
        self.titleLabel.setText(_translate("noteForm", "Title:"))
        self.savePushButton.setText(_translate("noteForm", "Save"))
        self.deletePushButton.setText(_translate("noteForm", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    noteForm = QtWidgets.QWidget()
    ui = Ui_NoteForm()
    ui.setupUi(noteForm)
    noteForm.show()
    sys.exit(app.exec())
