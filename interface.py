import sys

from PyQt5.QtGui import QPixmap, QBrush, QPalette
from PyQt5.QtWidgets import QTextEdit, QRadioButton, QButtonGroup, QAction, QVBoxLayout, QWidget, QApplication, \
    QHBoxLayout, QPushButton, QMainWindow, QLabel, QLineEdit

word = None
global hpp
globals()['interface'] = True
if globals().get("processor") is not None:
    global processor
else:
    import processor


class bottom_collection:
    w = None
    b = None

    @classmethod
    def fw(cls):
        cls.w = "fr"

    @classmethod
    def iw(cls):
        cls.w = "ic"

    @classmethod
    def fcw(cls):
        cls.w = 'fc'

    @classmethod
    def ib(cls):
        cls.b = 'i'

    @classmethod
    def sb(cls):
        cls.b = 'f'

    @classmethod
    def lb(cls):
        cls.b = 'r'


class Example1(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        cb = QRadioButton('Finite radius', self)
        cb2 = QRadioButton('Infinite conductivity fracture', self)
        cb3 = QRadioButton('Finite conductivity fracture', self)
        cb.clicked.connect(bottom_collection.fw)
        cb2.clicked.connect(bottom_collection.iw)
        cb3.clicked.connect(bottom_collection.fcw)
        '''cb.move(10, 20)
        cb2.move(10,35)
        cb3.move(10,50)'''
        cb5 = QRadioButton('Infinite', self)
        cb6 = QRadioButton('Single fault', self)
        cb7 = QRadioButton('Circle', self)
        cb5.clicked.connect(bottom_collection.ib)
        cb.clicked.connect(bottom_collection.sb)
        '''cb5.move(10,410)
        cb6.move(10,425)
        cb7.move(10,440)'''
        group1 = QButtonGroup(self)
        group2 = QButtonGroup(self)
        group1.addButton(cb)
        group1.addButton(cb2)
        group1.addButton(cb3)
        group2.addButton(cb5)
        group2.addButton(cb6)
        group2.addButton(cb7)
        setattr(self, 'h1', QPushButton("Generate", self))
        setattr(self, 'h2', QPushButton("Cancel", self))
        self.text = QTextEdit()
        '''self.h1.move(0,470)
        self.h2.move(405,470)'''
        l2 = QLabel("Well Model", self)
        l3 = QLabel("Boundary Model", self)
        '''l2.move(10,8)
        l3.move(10,398)'''
        self.layout.addWidget(l2)
        self.layout.addWidget(cb)
        self.layout.addWidget(cb2)
        self.layout.addWidget(cb3)
        self.layout.addWidget(l3)
        self.layout.addWidget(cb5)
        self.layout.addWidget(cb6)
        self.layout.addWidget(cb7)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.h1)
        self.layout.addWidget(self.h2)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Well test analysis software')
        self.hide()

class Example2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        self.pixmap = QPixmap(r"./bin/fig.png")

        lbl = QLabel(self)
        lbl.setPixmap(self.pixmap)
        setattr(self, 'bt1', QPushButton("Tracing point", self))
        setattr(self, 'bt2', QPushButton("Refresh", self))
        hbox.addWidget(lbl)
        hbox.addWidget(self.bt1)
        hbox.addWidget(self.bt2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)

        self.setWindowTitle('Image')
        self.hide()

    def load(self):
        self.pixmap.load(r"./bin/fig.png")



class Example3(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 100)
        self.line = QLineEdit()
        self.layout = QVBoxLayout()
        setattr(self, 'bt4', QPushButton("Yes", self))
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.bt4)
        self.setLayout(self.layout)
        self.setWindowTitle("Path")
        self.bt4.clicked.connect(self.hide)
        self.bt4.clicked.connect(self.send)
        self.hide()

    def send(self):
        global word
        word = self.line.text()
        processor.text_inner(word)
        return word


class WindowClass(QMainWindow):

    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.menubar = self.menuBar()  # 获取窗体的菜单栏

        self.file = self.menubar.addMenu("Files")
        self.file2 = self.menubar.addMenu("Others")
        self.save = QAction("Open", self)
        self.save.setShortcut("Ctrl+F")
        self.file.addAction(self.save)

        self.save1 = QAction("Generate", self)
        self.save1.setShortcut("Ctrl+A")
        self.file.addAction(self.save1)
        self.save2 = QAction("Help", self)
        self.save2.setShortcut("Ctrl+B")
        self.file2.addAction(self.save2)
        self.save3 = QAction("About", self)
        self.save3.setShortcut("Ctrl+C")
        self.file2.addAction(self.save3)
        self.save4 = QAction("Close", self)
        self.save4.setShortcut("Ctrl+D")
        self.file2.addAction(self.save4)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        window_pale = QPalette()
        window_pale.setBrush(self.backgroundRole(), QBrush(QPixmap(r"./bin/MainUI.png")))
        self.setPalette(window_pale)
        self.setWindowTitle("Menu Demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowClass()
    ex.show()
    ex1 = Example1()
    ex2 = Example2()
    ex3 = Example3()
    t1 = ex.save1

    t1.triggered.connect(ex1.show)
    t2 = ex.save
    t2.triggered.connect(ex3.show)
    b1 = ex3.bt4
    b1.clicked.connect(ex2.show)
    ex2.bt2.clicked.connect(ex2.load)
    b2 = ex1.h2
    b2.clicked.connect(ex1.hide)
    h = ex1.h1
    h.clicked.connect(ex2.show)
    sys.exit(app.exec_())
