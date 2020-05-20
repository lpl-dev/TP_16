from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QTextEdit

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('IHM')
        self.setMinimumSize(250,100)

        self.clic_number=[0,0,0]

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.ihms=[]
        self.ihm1_components=[QLabel('IMH1\n--------'),QPushButton('Fermer la fenêtre')]
        self.ihm1_components[1].clicked.connect(self.closeWindow)
        self.ihms.append(self.ihm1_components)

        self.ihm2_components=[QLabel('IMH2\n--------'),QPushButton('Changer le texte du bouton !')]
        self.ihm2_components[1].clicked.connect(self.changeButtonText)
        self.ihms.append(self.ihm2_components)

        self.ihm3_components = [QLabel('IMH3\n--------'), QPushButton('Changer le texte du champ de texte !'), QTextEdit()]
        self.ihm3_components[1].clicked.connect(self.changeTextContent)
        self.ihms.append(self.ihm3_components)

        self.ihm4_components = [QLabel('IMH4\n--------'), QPushButton('Changer le texte du bouton et du champ de texte !'), QTextEdit()]
        self.ihm4_components[1].clicked.connect(self.changeButtonAndTextContent)
        self.ihms.append(self.ihm4_components)

        for ihm in self.ihms:
            for component in ihm:
                self.main_layout.addWidget(component)

        self.show()

    def closeWindow(self):
        self.close()

    def changeButtonText(self):
        self.clic_number[0]+=1
        self.ihm2_components[1].setText(f'Clic {self.clic_number[0]}')

    def changeTextContent(self):
        self.clic_number[1] += 1
        self.ihm3_components[2].setText(f'Clic {self.clic_number[1]}')

    def changeButtonAndTextContent(self):
        self.clic_number[2] += 1
        self.ihm4_components[1].setText(f'Clic {self.clic_number[2]}')
        self.ihm4_components[2].setText(f'Clic {self.clic_number[2]}')


if __name__=='__main__':
    app=QApplication([])
    win=Window()
    app.exec_()