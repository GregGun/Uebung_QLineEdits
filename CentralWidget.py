from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextBrowser


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.deziLabel = QLabel("Zahlen im Dezimalsystem zwischen 0 und 9999", self)
        self.deziLineEdit = QLineEdit(self)
        self.deziLineEdit.setInputMask("9000")

        self.hexaLabel = QLabel("Sechsstellige Hexadezimalwerte", self)
        self.hexaLineEdit = QLineEdit(self)
        self.hexaLineEdit.setInputMask("HHHHHH")

        self.binLabel = QLabel("Binärzahlen, zwischen 2^2 und 2^10", self)
        self.binLineEdit = QLineEdit(self)
        self.binLineEdit.setInputMask("BBBbbbbbbb")

        self.buchstabenLabel = QLabel("Nur Buchstaben (a-z, A-Z)", self)
        self.buchstabenLineEdit = QLineEdit(self)
        self.buchstabenLineEdit.setMaxLength(-1)

        self.grokleiLabel = QLabel("Eingabe von Groß- und Kleinbuchstaben, welcher in Großbuchstaben umgewandelt wird", self)
        self.grokleiLineEdit = QLineEdit(self)
        self.grokleiLineEdit.setInputMask(">A")


        self.text_browser = QTextBrowser()

        self.deziLineEdit.textEdited.connect(self.text_edited)
        self.deziLineEdit.inputRejected.connect(self.text_rejected)
        self.deziLineEdit.editingFinished.connect(self.text_finished)

        layout = QGridLayout(self)
        layout.addWidget(self.deziLabel, 1, 1)
        layout.addWidget(self.deziLineEdit, 1, 2)
        layout.addWidget(self.hexaLabel, 2, 1)
        layout.addWidget(self.hexaLineEdit, 2, 2)
        layout.addWidget(self.binLabel, 3, 1)
        layout.addWidget(self.binLineEdit, 3, 2)
        layout.addWidget(self.buchstabenLabel, 4, 1)
        layout.addWidget(self.buchstabenLineEdit, 4, 2)
        layout.addWidget(self.grokleiLabel, 5, 1)
        layout.addWidget(self.grokleiLineEdit, 5, 2)
        layout.addWidget(self.text_browser, 6, 1, 6, 2)

    @pyqtSlot(str)
    def text_edited(self, text_from_signal):
        self.text_browser.append(text_from_signal + "\t(edited event)")

    @pyqtSlot()
    def text_rejected(self):
        self.text_browser.append("\t(input rejected)")

    @pyqtSlot()
    def text_finished(self):
        self.text_browser.append("\t(finished text")
        text = self.deziLineEdit.text()

