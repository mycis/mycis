# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

os.chdir(os.path.dirname(__file__))

class stackedExample(QWidget):

    def __init__(self):
        super(stackedExample, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.setIconSize(QSize(48, 48))
        self.leftlist.setViewMode(QListView.IconMode)
        for (i, j) in [('./res/img/ekg.png',  u'院所基本資料'), 
                ('./res/img/kcall.png',  u'看診畫面行為'),
                ('./res/img/ivbag.png',  u'測試正常狀況'),]:
            self.leftlist.addItem(QListWidgetItem(QIcon(i), j))
	
        dlg = QFontDialog()
        dlg.setOption(QFontDialog.NoButtons)
        self.stack1 = dlg 
        self.stack2 = QWidget()
        self.stack3 = QWidget()
                
        #self.stack1UI()
        self.stack2UI()
        self.stack3UI()
                
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
                
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10,10)
        self.setWindowTitle('StackedWidget demo')
        self.show()
            
    #def stack1UI(self):
    #    layout = QFormLayout()
    #    layout.addRow('Name',QLineEdit())
    #    layout.addRow('Address',QLineEdit())
    #    #self.setTabText(0,'Contact Details')
    #    self.stack1.setLayout(layout)
        
    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('Male'))
        sex.addWidget(QRadioButton('Female'))
        layout.addRow(QLabel('Sex'), sex)
        layout.addRow('Date of Birth', QLineEdit())
                
        self.stack2.setLayout(layout)
            
    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('subjects'))
        layout.addWidget(QCheckBox('Physics'))
        layout.addWidget(QCheckBox('Maths'))
        self.stack3.setLayout(layout)
            
    def display(self,i):
        self.stack.setCurrentIndex(i)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec_())
