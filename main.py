from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from PyQt5 import QtGui
import pygame
pygame.mixer.init()
def click():
    new_num = str(randint(1,4))
    if new_num == '1':
        pygame.mixer.music.load('yes.mp3')
        pygame.mixer.music.play()
        t.setText('Yes')
    elif new_num == '2':
        pygame.mixer.music.load('abc.mp3')
        pygame.mixer.music.play()
        t.setText('Hohoho!')

    elif new_num == '3':
        pygame.mixer.music.load('ugh.mp3')
        pygame.mixer.music.play()
        t.setText('Beee!')
    else:
        pygame.mixer.music.load('no.mp3')
        pygame.mixer.music.play()
        t.setText('No')
app = QApplication([])
win = QWidget()
win.setStyleSheet('0,0,0')
win.show()
win.resize(200,150)
app.setWindowIcon(QtGui.QIcon('A.jpg'))
win.setWindowTitle('Ben')
button = QPushButton('Нажми')
win.setStyleSheet('background-color:lightgreen')
button.setStyleSheet('background-color:#1f732a;border: 5px double powderblue;padding:5px;border-radius:10px')

v_l = QVBoxLayout()

button.clicked.connect(click)
title = QLabel('Talking Ben')
t = QLabel('...')
v_l.addWidget(title,alignment = Qt.AlignCenter)
v_l.addWidget(t,alignment = Qt.AlignCenter)
v_l.addWidget(button,alignment = Qt.AlignCenter)
win.setLayout(v_l)








app.exec()