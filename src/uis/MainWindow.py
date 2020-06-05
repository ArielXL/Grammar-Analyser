﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1350, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Qt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGrammar = QtWidgets.QWidget()
        self.tabGrammar.setObjectName("tabGrammar")
        self.gridLayout = QtWidgets.QGridLayout(self.tabGrammar)
        self.gridLayout.setObjectName("gridLayout")
        self.textEditGrammar = QtWidgets.QPlainTextEdit(self.tabGrammar)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textEditGrammar.setFont(font)
        self.textEditGrammar.setPlainText("")
        self.textEditGrammar.setObjectName("textEditGrammar")
        self.gridLayout.addWidget(self.textEditGrammar, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabGrammar, "")
        self.tabResults = QtWidgets.QWidget()
        self.tabResults.setObjectName("tabResults")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabResults)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textResults = QtWebEngineWidgets.QWebEngineView(self.tabResults)
        self.textResults.setUrl(QtCore.QUrl("about:blank"))
        self.textResults.setObjectName("textResults")
        self.gridLayout_2.addWidget(self.textResults, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabResults, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        self.menuAnalisis = QtWidgets.QMenu(self.menubar)
        self.menuAnalisis.setObjectName("menuAnalisis")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewGrammar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/selection-input.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewGrammar.setIcon(icon1)
        self.actionNewGrammar.setObjectName("actionNewGrammar")
        self.actionSaveGrammar = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveGrammar.setIcon(icon2)
        self.actionSaveGrammar.setObjectName("actionSaveGrammar")
        self.actionLoadGrammar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/blue-folder-horizontal-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadGrammar.setIcon(icon3)
        self.actionLoadGrammar.setObjectName("actionLoadGrammar")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/cross-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp_2 = QtWidgets.QAction(MainWindow)
        self.actionHelp_2.setIcon(icon5)
        self.actionHelp_2.setObjectName("actionHelp_2")
        self.actionAboutGrammarAnalyser = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/lifebuoy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutGrammarAnalyser.setIcon(icon6)
        self.actionAboutGrammarAnalyser.setObjectName("actionAboutGrammarAnalyser")
        self.actionSaveGrammarAs = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/disk--pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveGrammarAs.setIcon(icon7)
        self.actionSaveGrammarAs.setObjectName("actionSaveGrammarAs")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyse.setIcon(icon8)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.actionAnalyse.setFont(font)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.actionQuickAnalyse = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/controlx2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuickAnalyse.setIcon(icon9)
        self.actionQuickAnalyse.setObjectName("actionQuickAnalyse")
        self.actionAnalyse_2 = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyse_2.setIcon(icon10)
        self.actionAnalyse_2.setObjectName("actionAnalyse_2")
        self.actionQuickAnalyse_2 = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/controlx2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuickAnalyse_2.setIcon(icon11)
        self.actionQuickAnalyse_2.setObjectName("actionQuickAnalyse_2")
        self.actionAboutAuthors = QtWidgets.QAction(MainWindow)
        self.actionAboutAuthors.setIcon(icon6)
        self.actionAboutAuthors.setObjectName("actionAboutAuthors")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNewGrammar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoadGrammar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveGrammar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAcerca_de.addAction(self.actionAboutAuthors)
        self.menuAcerca_de.addAction(self.actionAboutGrammarAnalyser)
        self.menuAnalisis.addAction(self.actionAnalyse_2)
        self.menuAnalisis.addAction(self.actionQuickAnalyse_2)
        self.menuAyuda.addAction(self.actionHelp_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalisis.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analizador de Gramáticas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGrammar), _translate("MainWindow", "Gramática"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResults), _translate("MainWindow", "Resultados"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de"))
        self.menuAnalisis.setTitle(_translate("MainWindow", "Análisis"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNewGrammar.setText(_translate("MainWindow", "Nueva gramática"))
        self.actionNewGrammar.setStatusTip(_translate("MainWindow", "Nueva Gramática"))
        self.actionNewGrammar.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSaveGrammar.setText(_translate("MainWindow", "Guardar gramática"))
        self.actionSaveGrammar.setStatusTip(_translate("MainWindow", "Guardar Gramática"))
        self.actionSaveGrammar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoadGrammar.setText(_translate("MainWindow", "Cargar gramática"))
        self.actionLoadGrammar.setStatusTip(_translate("MainWindow", "Cargar Gramática"))
        self.actionLoadGrammar.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Salir"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionHelp.setText(_translate("MainWindow", "Ayuda"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "¿Cómo usar?"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionHelp_2.setText(_translate("MainWindow", "Ayuda"))
        self.actionHelp_2.setShortcut(_translate("MainWindow", "F1"))
        self.actionAboutGrammarAnalyser.setText(_translate("MainWindow", "Acerca de Analizador de Gramáticas"))
        self.actionSaveGrammarAs.setText(_translate("MainWindow", "Guardar gramática como ..."))
        self.actionSaveGrammarAs.setStatusTip(_translate("MainWindow", "Guardar Gramática Como"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setToolTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setStatusTip(_translate("MainWindow", "Analizar"))
        self.actionAnalyse.setShortcut(_translate("MainWindow", "F5"))
        self.actionQuickAnalyse.setText(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setToolTip(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setStatusTip(_translate("MainWindow", "Análisis rápido"))
        self.actionQuickAnalyse.setShortcut(_translate("MainWindow", "F9"))
        self.actionAnalyse_2.setText(_translate("MainWindow", "Análisis de la gramática"))
        self.actionAnalyse_2.setShortcut(_translate("MainWindow", "F5"))
        self.actionQuickAnalyse_2.setText(_translate("MainWindow", "Análisis rápido de la gramática"))
        self.actionQuickAnalyse_2.setShortcut(_translate("MainWindow", "F9"))
        self.actionAboutAuthors.setText(_translate("MainWindow", "Acerca de los Autores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())