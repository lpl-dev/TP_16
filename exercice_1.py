from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
import random as rd

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setFixedSize(500,300)

        self.cycles=["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.label=QLabel('CSI')
        self.button=QPushButton('Changer le cycle')
        self.button.clicked.connect(self.changeCycle)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)

        self.show()

    def changeCycle(self):
        self.label.setText(rd.choice(self.cycles))

if __name__=='__main__':
    app=QApplication([])
    win=Window()
    app.exec_()