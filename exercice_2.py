from PySide2.QtWidgets import QWidget, QApplication, QHBoxLayout, QProgressBar, QSlider

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('IHM')
        self.setMinimumSize(250,100)

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.progressBar=QProgressBar()
        self.slider=QSlider()
        self.slider.valueChanged.connect(self.updateValue)

        self.main_layout.addWidget(self.progressBar)
        self.main_layout.addWidget(self.slider)

        self.show()

    def updateValue(self):
        self.progressBar.setValue(self.slider.value())


if __name__=='__main__':
    app=QApplication([])
    win=Window()
    app.exec_()