from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PySide2.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Calculator')
        self.setFixedSize(260,320)
        self.layout=QGridLayout()
        self.setLayout(self.layout)

        col_nbr = 4
        self.line_edit=QLineEdit()
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setText('0')
        self.layout.addWidget(self.line_edit, 0, 0, 1, col_nbr)

        buttons_content = 'C CE 7 8 9 / 4 5 6 * 1 2 3 - 0 . = +'
        buttons_per_rows = [2, 4, 4, 4, 4]
        self.buttons=[]
        for button_content in buttons_content.split(' '):
            self.buttons.append(QPushButton(button_content))
        added_buttons=0
        for row,buttons_per_row in enumerate(buttons_per_rows):
            button_width=col_nbr/buttons_per_row
            for i in range(buttons_per_row):
                self.layout.addWidget(self.buttons[added_buttons],1+row,i*button_width,1,button_width)
                added_buttons+=1
        for i,button in enumerate(self.buttons):
            button.setFixedHeight(50)
            button.clicked.connect(self.clicked_event)

    def clicked_event(self):
        button=self.sender().text()
        line_edit_content=self.line_edit.text()
        if self.line_edit.text()=='0':
            if button.isnumeric() or button in '-+':
                self.line_edit.setText(button)
            elif button=='.':
                self.line_edit.setText('0.')
        else:
            if button=='C':
                self.line_edit.setText('0')
            elif button=='CE':
                self.line_edit.setText(line_edit_content[:-1] if len(line_edit_content)>1 else '0')
            elif button.isnumeric():
                self.line_edit.setText(line_edit_content+button)
            elif button in '-+*/.' and line_edit_content[-1] not in '-+*/.':
                self.line_edit.setText(line_edit_content + button)
            else:
                self.line_edit.setText(str(eval(line_edit_content)))

if __name__=='__main__':
    app=QApplication([])
    win=Window()
    win.show()
    app.exec_()