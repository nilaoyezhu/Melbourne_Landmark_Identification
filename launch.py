#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import os, sys
from PyQt4.QtGui import *
filename = "test_photos/9929959995_6e31b94d8b_o.jpg"
# Create an PyQT4 application object.
app = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
window = QWidget()

# Set window size.
window.resize(480, 320)

# Set window title
window.setWindowTitle("Melbourne Landmark Identification")

# Get filename using QFileDialog
def browse():
    #global filename
    # print file contents
    # with open(filename, 'r') as file:

    label1 = QLabel(window)
    filename = QFileDialog.getOpenFileName(window, 'Open File', '/')
    pixmap = QPixmap(filename)
    label1.setPixmap(pixmap)
    window.resize(pixmap.width() + 150, pixmap.height() + 100)
    vbox = QVBoxLayout(window)
    vbox.addWidget(label1)
    buttonCommand = "python -m scripts.label_image --graph tf_files/retrained_graph.pb --image " + str(filename)
    os.system(buttonCommand)

def calculate():
    #global filename

    recordtext = open('record.txt','r')
    finaltext = recordtext.readlines()[1].upper()
    QMessageBox.about(window, "Landmark similarity", finaltext)

# Add buttons
button1 = QPushButton('Select a photo!', window)

button1.clicked.connect(browse)
button1.resize(button1.sizeHint())
button1.move(10, 10)

button2 = QPushButton('Which landmark?', window)

button2.clicked.connect(calculate)
button2.resize(button2.sizeHint())
button2.move(210, 10)

# Show window
window.show()

sys.exit(app.exec_())
