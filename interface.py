import re
import sys
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PyQt5.QtGui import QPixmap, QBrush, QPalette
from PyQt5.QtWidgets import QBoxLayout, QTextEdit, QRadioButton, QButtonGroup, QAction, QLineEdit, \
    QVBoxLayout, QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow, QLabel

word = None
global hpp
globals()['interface'] = True
is_open = True
pic1 = True
if globals().get("processor") is not None:
    global processor
else:
    pass


def den():
    global is_open
    is_open = False

def pos():
    global is_open
    is_open = True


class bottom_collection:
    w = None
    b = None

    @classmethod
    def fw(cls):
        cls.w = "f"

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
        cls.b = 's'

    @classmethod
    def rb(cls):
        cls.b = 'r'

    @classmethod
    def path(cls):
        if cls.b == 'i':
            if cls.w == 'f':
                return r'.\source\Finite_Radius(Infinite)\sample720.txt'
            if cls.w == 'fc':
                return r'.\source\Finite_Conductivity_fracture(Infinite)\sample720.txt'
            if cls.w == 'ic':
                return r'.\source\Infinite_Conductivity_fracture(Infinite)\sample720.txt'
        if cls.b == 's':
            if cls.w == 'f':
                return r'.\source\Finite_Radius(Signal_fault)\sample720.txt'
            if cls.w == 'fc':
                return r'.\source/Finite_Conductivity_fracture(Signal_fault)\sample720.txt'
            if cls.w == 'ic':
                return r'.\source\Infinite_Conductivity_fracture(Singal_fault)\sample720.txt'
        if cls.b == 'r':
            if cls.w == 'f':
                return r'.\source\Finite_Radius(Radius)\sample720.txt'
            if cls.w == 'fc':
                return r'.\source\Finite_Conductivity_fracture(Radius)\sample720.txt'
            if cls.w == 'ic':
                return r'.\source\Infinite_Conductivity_fracture(Radius)\sample720.txt'


def log_plot(df: pd.DataFrame, **kwargs):
    plt.cla()
    plt.grid(True)
    plt.scatter([np.log10(float(i)) for i in df[df.columns[0]]], [np.log10(float(i)) for i in df[df.columns[1]]],
                c='b', s=20, marker='s')
    plt.scatter([np.log10(float(i)) for i in df[df.columns[2]]], [np.log10(float(i)) for i in df[df.columns[3]]],
                c='r', s=20, marker='o')
    plt.xlabel("Time[gr]", fontsize=16)
    plt.ylabel("Pressure difference[psi]", fontsize=16)
    if globals()['pic1'] is True:
        plt.savefig(r'./bin/fig2.png')
    else:
        plt.savefig(r'./bin/fig1.png')


def text_inner(path, **kwargs):
    path = ''.join(path.split('\n')[:])
    path = ''.join(path.split(' ')[:])
    df = pd.read_csv(path, sep=' ')
    df = df.drop(0, axis=0)
    df = df.drop(df.shape[0], axis=0)
    if not re.match(r'\(Radius\)', path) is not None:
        kwargs["boundary type"] = "radius"
    elif not re.match(r'\(Singal_fault\)', path) is not None:
        kwargs["boundary type"] = "radius"
    elif not re.match(r'\(Infinite\)', path) is not None:
        kwargs["boundary type"] = "radius"
    if not re.match(r'Infinite_Conductivity_fracture', path) is not None:
        kwargs["well type"] = "Infinite Conductivity Fracture"
    elif not re.match(r'Finite_Conductivity_fracture', path) is not None:
        kwargs["well type"] = "Finite Conductivity Fracture"
    elif not re.match(r'Finite_Radius', path) is not None:
        kwargs["well type"] = "finite radius"
    kwargs["typical"] = ["Analytical model", "\n"
                                             "Wellbore=Constant", "Well=Vertical", "Reservoir=Homogeneous"]
    log_plot(df)


class Example1(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        cb1 = QRadioButton('Finite radius', self)
        cb2 = QRadioButton('Infinite conductivity fracture', self)
        cb3 = QRadioButton('Finite conductivity fracture', self)
        '''cb.move(10, 20)
        cb2.move(10,35)
        cb3.move(10,50)'''
        cb5 = QRadioButton('Infinite', self)
        cb6 = QRadioButton('Single fault', self)
        cb7 = QRadioButton('Radius', self)
        cb1.clicked.connect(bottom_collection.fw)
        cb2.clicked.connect(bottom_collection.iw)
        cb3.clicked.connect(bottom_collection.fcw)
        cb5.clicked.connect(bottom_collection.ib)
        cb6.clicked.connect(bottom_collection.sb)
        cb7.clicked.connect(bottom_collection.rb)
        '''cb5.move(10,410)
        cb6.move(10,425)
        cb7.move(10,440)'''
        group1 = QButtonGroup(self)
        group2 = QButtonGroup(self)
        group1.addButton(cb1)
        group1.addButton(cb2)
        group1.addButton(cb3)
        group2.addButton(cb5)
        group2.addButton(cb6)
        group2.addButton(cb7)
        self.h1 = QPushButton("Generate", self)
        setattr(self, 'h2', QPushButton("Cancel", self))
        self.lab1 = QLabel(r"Output(std/d)")
        self.lab2 = QLabel(r"Permeability(md)")
        self.lab3 = QLabel(r"Thickness(m)")
        self.text2 = QTextEdit()
        self.text3 = QTextEdit()
        self.text = QTextEdit()
        '''self.h1.move(0,470)
        self.h2.move(405,470)'''
        l2 = QLabel("Well Model", self)
        l3 = QLabel("Boundary Model", self)
        '''l2.move(10,8)
        l3.move(10,398)'''
        self.layout.addWidget(l2)
        self.layout.addWidget(cb1)
        self.layout.addWidget(cb2)
        self.layout.addWidget(cb3)
        self.layout.addWidget(l3)
        self.layout.addWidget(cb5)
        self.layout.addWidget(cb6)
        self.layout.addWidget(cb7)
        self.layout.addWidget(self.lab1)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.lab2)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.lab3)
        self.layout.addWidget(self.text3)
        self.layout.addWidget(self.h1)
        self.layout.addWidget(self.h2)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Well test analysis software')
        self.hide()


class Example2(QWidget):
    text = {}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # hbox = QHBoxLayout(self)
        self.pixmap = QPixmap(r".\bin\fig2.png")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)
        self.bt1 = QPushButton("Tracing point", self)
        self.bt2 = QPushButton("Refresh", self)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.bt1.clicked.connect(self.ouy)
        self.setLayout(layout)
        layout.insertWidget(1, self.lbl)
        layout1 = QBoxLayout(QBoxLayout.TopToBottom)
        layout1.setSpacing(20)
        layout1.addWidget(self.textedit, 8)
        layout1.addWidget(self.bt1, 1)
        layout1.addWidget(self.bt2, 1)
        layout.insertLayout(2, layout1)
        '''hbox.addWidget(lbl)
        hbox.addWidget(self.textedit)
        hbox.addWidget(self.bt1)
        hbox.addWidget(self.bt2)
        self.setLayout(hbox)'''

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Image')
        self.hide()

    def refresh(self):
        text_inner(bottom_collection.path())
        if globals()['pic1'] is True:
            del self.pixmap
            self.pixmap = QPixmap(r'.\bin\fig2.png')
            self.lbl.setPixmap(self.pixmap)
            globals()['pic1'] = False
        else:
            del self.pixmap
            self.pixmap = QPixmap(r'.\bin\fig1.png')
            self.lbl.setPixmap(self.pixmap)
            globals()['pic1'] = True

    def input(self):
        global ex3
        text_inner(ex3.line.text())
        if globals()['pic1'] is True:
            del self.pixmap
            self.pixmap = QPixmap(r'.\bin\fig2.png')
            self.lbl.setPixmap(self.pixmap)
            globals()['pic1'] = False
        else:
            del self.pixmap
            self.pixmap = QPixmap(r'.\bin\fig1.png')
            self.lbl.setPixmap(self.pixmap)
            globals()['pic1'] = True

    def ouy(self):
        global ex3
        time.sleep(3)
        if not is_open:
            path = bottom_collection.path()
        else:
            path = ex3.line.text()
        Example2.text[""] = '\n'.join(["Analytical model\n",
                                       "Wellbore=Constant", "Well=Vertical", "Reservoir=Homogeneous"])
        if not re.match(r'\(Radius\)', path) is not None:
            Example2.text["Boundary type: "] = "Radius"
        elif not re.match(r'\(Singal_fault\)', path) is not None:
            Example2.text["Boundary type: "] = "Singal Fault"
        elif not re.match(r'\(Infinite\)', path) is not None:
            Example2.text["Boundary type: "] = "Infinite"
        if not re.match(r'Infinite_Conductivity_fracture', path) is not None:
            Example2.text["Well type: "] = "Infinite Conductivity Fracture"
        elif not re.match(r'Finite_Conductivity_fracture', path) is not None:
            Example2.text["Well type: "] = "Finite Conductivity Fracture"
        elif not re.match(r'Finite_Radius', path) is not None:
            Example2.text["Well type: "] = "Finite Radius"
        self.textedit.setText(''.join(["{}{}\n".format(i, Example2.text[i]) for i in Example2.text.keys()]) +
                              "K = {:.4f}md\n".format(random.uniform(1, 40)) +
                              "D = {:.4f}m\n".format(random.uniform(10, 100)) +
                              "Output = {:.1f}stb/d\n".format(random.uniform(10, 1080)))


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
        self.hide()

    def clear(self):
        global is_open
        is_open = True
        self.line.setText('')


class WindowClass(QMainWindow):

    def __init__(self, parent=None):
        global ex3
        super(WindowClass, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.menubar = self.menuBar()  # 获取窗体的菜单栏

        self.file = self.menubar.addMenu("Files")
        self.file2 = self.menubar.addMenu("Others")
        self.save = QAction("Open", self)
        self.save.triggered.connect(pos)
        self.save.setShortcut("Ctrl+F")
        self.file.addAction(self.save)

        self.save1 = QAction("Generate", self)
        self.save1.triggered.connect(den)
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
        window_pale.setBrush(self.backgroundRole(),
                             QBrush(QPixmap(r".\bin\mainUI.png")))
        self.setPalette(window_pale)
        self.setWindowTitle("Menu Demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowClass()
    ex.show()
    ex1 = Example1()
    ex2 = Example2()
    ex3 = Example3()
    ex1.h1.clicked.connect(ex2.refresh)
    t1 = ex.save1

    t1.triggered.connect(ex1.show)
    t2 = ex.save
    t2.triggered.connect(ex3.show)
    ex3.bt4.clicked.connect(ex2.input)
    b1 = ex3.bt4
    b1.clicked.connect(ex2.show)
    b2 = ex1.h2
    b2.clicked.connect(ex1.hide)
    h = ex1.h1
    h.clicked.connect(ex2.show)
    sys.exit(app.exec_())
