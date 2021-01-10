from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
 
from keypad import numPadList, operatorList
from constant import constantMap, constantList, findConstant
from function import functionMap, functionList, findFunction

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.calcResult = 'result'

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(40)
        
        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    
    def buttonClicked(self):

        button = self.sender()
        key = button.text()

        if self.display.text() == self.calcResult:
            # 에러처리 후 또는 계산한 값 뒤에 상수가 오면 빈칸으로
            if self.display.text()[-1] == '다' or (key in constantList or key in numPadList) and (key != "="):
                self.display.setText('')
    
        if key == '=':
            try:
                self.calcResult = str(eval(self.display.text()))
            except (SyntaxError, TypeError):
                self.calcResult = '수식이 올바르지 않습니다'
            except ZeroDivisionError:
                self.calcResult = '0으로 나눌 수 없습니다'
            self.display.setText(self.calcResult)

        elif key == 'C':
            self.display.clear()

        elif key in constantList:
            # 상수는 문장의 처음, 연산자 다음에만 입력 가능
            if (self.display.text() != '') and (self.display.text()[-1] not in operatorList):
                self.display.clear()
            value = findConstant(key)
            self.calcResult = self.display.text() + value
            self.display.setText(self.calcResult)

        elif key in functionList:
            n = self.display.text()
            self.calcResult = findFunction(key)(n)
            self.display.setText(self.calcResult)
        
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())