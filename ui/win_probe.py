# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cytu/usr/src/py/mycis/designer/win_probe.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win_probe(object):
    def setupUi(self, win_probe):
        win_probe.setObjectName(_fromUtf8("win_probe"))
        win_probe.setEnabled(True)
        win_probe.resize(1026, 688)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(8)
        win_probe.setFont(font)
        win_probe.setWindowTitle(_fromUtf8(""))
        win_probe.setStyleSheet(_fromUtf8("font: 50 8pt \"Microsoft JhengHei\";"))
        self.centralwidget = QtGui.QWidget(win_probe)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        win_probe.setCentralWidget(self.centralwidget)
        self.mnb = QtGui.QMenuBar(win_probe)
        self.mnb.setGeometry(QtCore.QRect(0, 0, 1026, 33))
        self.mnb.setObjectName(_fromUtf8("mnb"))
        self.mnu = QtGui.QMenu(self.mnb)
        self.mnu.setObjectName(_fromUtf8("mnu"))
        win_probe.setMenuBar(self.mnb)
        self.tb = QtGui.QToolBar(win_probe)
        self.tb.setEnabled(True)
        self.tb.setIconSize(QtCore.QSize(48, 48))
        self.tb.setObjectName(_fromUtf8("tb"))
        win_probe.addToolBar(QtCore.Qt.TopToolBarArea, self.tb)
        self.act_add_fav = QtGui.QAction(win_probe)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/favorites.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_add_fav.setIcon(icon)
        self.act_add_fav.setObjectName(_fromUtf8("act_add_fav"))
        self.act_search = QtGui.QAction(win_probe)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_search.setIcon(icon1)
        self.act_search.setObjectName(_fromUtf8("act_search"))
        self.act_printf = QtGui.QAction(win_probe)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_printf.setIcon(icon2)
        self.act_printf.setObjectName(_fromUtf8("act_printf"))
        self.act_done = QtGui.QAction(win_probe)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_done.setIcon(icon3)
        self.act_done.setObjectName(_fromUtf8("act_done"))
        self.act_redo = QtGui.QAction(win_probe)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/edit_redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_redo.setIcon(icon4)
        self.act_redo.setObjectName(_fromUtf8("act_redo"))
        self.act_undo = QtGui.QAction(win_probe)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/edit_undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_undo.setIcon(icon5)
        self.act_undo.setObjectName(_fromUtf8("act_undo"))
        self.act_ic = QtGui.QAction(win_probe)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/text-x-vcard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ic.setIcon(icon6)
        self.act_ic.setObjectName(_fromUtf8("act_ic"))
        self.act_fav = QtGui.QAction(win_probe)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/folder_bookmarks.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_fav.setIcon(icon7)
        self.act_fav.setObjectName(_fromUtf8("act_fav"))
        self.act_reserve = QtGui.QAction(win_probe)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/1day.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_reserve.setIcon(icon8)
        self.act_reserve.setObjectName(_fromUtf8("act_reserve"))
        self.act_refer = QtGui.QAction(win_probe)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/res/img/go_jump_today.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_refer.setIcon(icon9)
        self.act_refer.setObjectName(_fromUtf8("act_refer"))
        self.mnu.addAction(self.act_add_fav)
        self.mnu.addAction(self.act_fav)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_search)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_printf)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_ic)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_redo)
        self.mnu.addAction(self.act_undo)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_reserve)
        self.mnu.addAction(self.act_refer)
        self.mnu.addSeparator()
        self.mnu.addAction(self.act_done)
        self.mnu.addSeparator()
        self.mnb.addAction(self.mnu.menuAction())
        self.tb.addAction(self.act_add_fav)
        self.tb.addAction(self.act_fav)
        self.tb.addSeparator()
        self.tb.addAction(self.act_ic)
        self.tb.addSeparator()
        self.tb.addAction(self.act_search)
        self.tb.addSeparator()
        self.tb.addAction(self.act_printf)
        self.tb.addSeparator()
        self.tb.addAction(self.act_undo)
        self.tb.addAction(self.act_redo)
        self.tb.addSeparator()
        self.tb.addAction(self.act_reserve)
        self.tb.addAction(self.act_refer)
        self.tb.addSeparator()
        self.tb.addAction(self.act_done)
        self.tb.addSeparator()

        self.retranslateUi(win_probe)
        QtCore.QMetaObject.connectSlotsByName(win_probe)

    def retranslateUi(self, win_probe):
        self.mnu.setTitle(_translate("win_probe", "工作(&W)", None))
        self.tb.setWindowTitle(_translate("win_probe", "tb", None))
        self.act_add_fav.setText(_translate("win_probe", "加入範本", None))
        self.act_add_fav.setShortcut(_translate("win_probe", "Ctrl+E", None))
        self.act_search.setText(_translate("win_probe", "搜尋", None))
        self.act_search.setShortcut(_translate("win_probe", "Ctrl+F", None))
        self.act_printf.setText(_translate("win_probe", "列印", None))
        self.act_printf.setShortcut(_translate("win_probe", "Ctrl+P", None))
        self.act_done.setText(_translate("win_probe", "完成", None))
        self.act_done.setShortcut(_translate("win_probe", "Ctrl+X", None))
        self.act_redo.setText(_translate("win_probe", "Redo", None))
        self.act_undo.setText(_translate("win_probe", "Undo", None))
        self.act_ic.setText(_translate("win_probe", "IC卡", None))
        self.act_fav.setText(_translate("win_probe", "範本", None))
        self.act_reserve.setText(_translate("win_probe", "約診", None))
        self.act_refer.setText(_translate("win_probe", "轉診", None))

import mycis_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win_probe = QtGui.QMainWindow()
    ui = Ui_win_probe()
    ui.setupUi(win_probe)
    win_probe.show()
    sys.exit(app.exec_())
