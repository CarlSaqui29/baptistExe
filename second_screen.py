# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NOBLEWARRIOR29\Desktop\Open Hymn\second_screen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_second(object):
    def setupUi(self, UI_second):
        UI_second.setObjectName("UI_second")
        UI_second.resize(1219, 838)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source_image/ICO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UI_second.setWindowIcon(icon)
        UI_second.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(UI_second)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(90)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(130, 50, 0, 45)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 231, 47);")
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("image: url(:/source_image/bap.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(0, 50)
        self.horizontalLayout.setStretch(1, 5)
        UI_second.setCentralWidget(self.centralwidget)

        self.retranslateUi(UI_second)
        QtCore.QMetaObject.connectSlotsByName(UI_second)

    def retranslateUi(self, UI_second):
        _translate = QtCore.QCoreApplication.translate
        UI_second.setWindowTitle(_translate("UI_second", "Baptist Favorites"))
import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_second = QtWidgets.QMainWindow()
    ui = Ui_UI_second()
    ui.setupUi(UI_second)
    UI_second.show()
    sys.exit(app.exec_())
