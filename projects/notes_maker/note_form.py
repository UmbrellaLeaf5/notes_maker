# Form implementation generated from reading ui file 'note_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NoteForm(object):
    def setupUi(self, noteForm):
        noteForm.setObjectName("noteForm")
        noteForm.resize(500, 600)

        self.verticalLayout = QtWidgets.QVBoxLayout(noteForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=noteForm)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.titleLayout = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.titleLayout.setObjectName("titleLayout")
        self.titleLabel = QtWidgets.QLabel(parent=self.horizontalWidget_2)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLayout.addWidget(self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(parent=self.horizontalWidget_2)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.titleLayout.addWidget(self.titleLineEdit)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
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
