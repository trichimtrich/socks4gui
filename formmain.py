# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formmain.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(684, 535)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("socks4gui.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnListen = QtGui.QPushButton(self.centralwidget)
        self.btnListen.setObjectName(_fromUtf8("btnListen"))
        self.horizontalLayout.addWidget(self.btnListen)
        self.btnStop = QtGui.QPushButton(self.centralwidget)
        self.btnStop.setEnabled(False)
        self.btnStop.setCheckable(False)
        self.btnStop.setChecked(False)
        self.btnStop.setFlat(False)
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabCapture = QtGui.QWidget()
        self.tabCapture.setObjectName(_fromUtf8("tabCapture"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tabCapture)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lstCapture = QtGui.QListWidget(self.tabCapture)
        self.lstCapture.setObjectName(_fromUtf8("lstCapture"))
        self.verticalLayout_2.addWidget(self.lstCapture)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmbViewObject = QtGui.QComboBox(self.tabCapture)
        self.cmbViewObject.setObjectName(_fromUtf8("cmbViewObject"))
        self.cmbViewObject.addItem(_fromUtf8(""))
        self.cmbViewObject.addItem(_fromUtf8(""))
        self.cmbViewObject.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbViewObject)
        self.cmbViewType = QtGui.QComboBox(self.tabCapture)
        self.cmbViewType.setObjectName(_fromUtf8("cmbViewType"))
        self.cmbViewType.addItem(_fromUtf8(""))
        self.cmbViewType.addItem(_fromUtf8(""))
        self.cmbViewType.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbViewType)
        self.btnClearHistory = QtGui.QPushButton(self.tabCapture)
        self.btnClearHistory.setObjectName(_fromUtf8("btnClearHistory"))
        self.horizontalLayout_2.addWidget(self.btnClearHistory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.txtData = QtGui.QTextEdit(self.tabCapture)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.txtData.setFont(font)
        self.txtData.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.txtData.setReadOnly(True)
        self.txtData.setAcceptRichText(True)
        self.txtData.setObjectName(_fromUtf8("txtData"))
        self.verticalLayout_3.addWidget(self.txtData)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cmbDetailType = QtGui.QComboBox(self.tabCapture)
        self.cmbDetailType.setObjectName(_fromUtf8("cmbDetailType"))
        self.cmbDetailType.addItem(_fromUtf8(""))
        self.cmbDetailType.addItem(_fromUtf8(""))
        self.cmbDetailType.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cmbDetailType)
        self.chkShowEdit = QtGui.QCheckBox(self.tabCapture)
        self.chkShowEdit.setChecked(True)
        self.chkShowEdit.setObjectName(_fromUtf8("chkShowEdit"))
        self.horizontalLayout_3.addWidget(self.chkShowEdit)
        self.btnSaveDetail = QtGui.QPushButton(self.tabCapture)
        self.btnSaveDetail.setObjectName(_fromUtf8("btnSaveDetail"))
        self.horizontalLayout_3.addWidget(self.btnSaveDetail)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tabCapture, _fromUtf8(""))
        self.tabHijack = QtGui.QWidget()
        self.tabHijack.setObjectName(_fromUtf8("tabHijack"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabHijack)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.chkReplace = QtGui.QCheckBox(self.tabHijack)
        self.chkReplace.setChecked(True)
        self.chkReplace.setObjectName(_fromUtf8("chkReplace"))
        self.horizontalLayout_5.addWidget(self.chkReplace)
        self.chkIgnore = QtGui.QCheckBox(self.tabHijack)
        self.chkIgnore.setChecked(True)
        self.chkIgnore.setObjectName(_fromUtf8("chkIgnore"))
        self.horizontalLayout_5.addWidget(self.chkIgnore)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.chkEncap = QtGui.QCheckBox(self.tabHijack)
        self.chkEncap.setObjectName(_fromUtf8("chkEncap"))
        self.horizontalLayout_7.addWidget(self.chkEncap)
        self.txtEncap = QtGui.QLineEdit(self.tabHijack)
        self.txtEncap.setObjectName(_fromUtf8("txtEncap"))
        self.horizontalLayout_7.addWidget(self.txtEncap)
        self.btnEncap = QtGui.QPushButton(self.tabHijack)
        self.btnEncap.setObjectName(_fromUtf8("btnEncap"))
        self.horizontalLayout_7.addWidget(self.btnEncap)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tblRule = QtGui.QTableWidget(self.tabHijack)
        self.tblRule.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblRule.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblRule.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblRule.setObjectName(_fromUtf8("tblRule"))
        self.tblRule.setColumnCount(4)
        self.tblRule.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblRule.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tblRule)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btnAddRule = QtGui.QPushButton(self.tabHijack)
        self.btnAddRule.setObjectName(_fromUtf8("btnAddRule"))
        self.horizontalLayout_6.addWidget(self.btnAddRule)
        self.btnUpRule = QtGui.QPushButton(self.tabHijack)
        self.btnUpRule.setObjectName(_fromUtf8("btnUpRule"))
        self.horizontalLayout_6.addWidget(self.btnUpRule)
        self.btnDownRule = QtGui.QPushButton(self.tabHijack)
        self.btnDownRule.setObjectName(_fromUtf8("btnDownRule"))
        self.horizontalLayout_6.addWidget(self.btnDownRule)
        self.btnDelRule = QtGui.QPushButton(self.tabHijack)
        self.btnDelRule.setObjectName(_fromUtf8("btnDelRule"))
        self.horizontalLayout_6.addWidget(self.btnDelRule)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tabHijack, _fromUtf8(""))
        self.tabSetting = QtGui.QWidget()
        self.tabSetting.setObjectName(_fromUtf8("tabSetting"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabSetting)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(self.tabSetting)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.txtSetPort = QtGui.QLineEdit(self.tabSetting)
        self.txtSetPort.setObjectName(_fromUtf8("txtSetPort"))
        self.horizontalLayout_8.addWidget(self.txtSetPort)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_2 = QtGui.QLabel(self.tabSetting)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_9.addWidget(self.label_2)
        self.txtSetLog = QtGui.QLineEdit(self.tabSetting)
        self.txtSetLog.setObjectName(_fromUtf8("txtSetLog"))
        self.horizontalLayout_9.addWidget(self.txtSetLog)
        self.btnLog = QtGui.QPushButton(self.tabSetting)
        self.btnLog.setObjectName(_fromUtf8("btnLog"))
        self.horizontalLayout_9.addWidget(self.btnLog)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_3 = QtGui.QLabel(self.tabSetting)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_10.addWidget(self.label_3)
        self.txtSetHexLen = QtGui.QLineEdit(self.tabSetting)
        self.txtSetHexLen.setObjectName(_fromUtf8("txtSetHexLen"))
        self.horizontalLayout_10.addWidget(self.txtSetHexLen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_4 = QtGui.QLabel(self.tabSetting)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.txtSetDataLen = QtGui.QLineEdit(self.tabSetting)
        self.txtSetDataLen.setObjectName(_fromUtf8("txtSetDataLen"))
        self.horizontalLayout_11.addWidget(self.txtSetDataLen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tabSetting, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.txtConsole = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtConsole.sizePolicy().hasHeightForWidth())
        self.txtConsole.setSizePolicy(sizePolicy)
        self.txtConsole.setReadOnly(True)
        self.txtConsole.setObjectName(_fromUtf8("txtConsole"))
        self.verticalLayout_4.addWidget(self.txtConsole)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Socks4GUI - trichimtrich", None))
        self.btnListen.setText(_translate("MainWindow", "Listen", None))
        self.btnStop.setText(_translate("MainWindow", "Stop", None))
        self.cmbViewObject.setItemText(0, _translate("MainWindow", "All", None))
        self.cmbViewObject.setItemText(1, _translate("MainWindow", "From Sender", None))
        self.cmbViewObject.setItemText(2, _translate("MainWindow", "From Receiver", None))
        self.cmbViewType.setItemText(0, _translate("MainWindow", "All", None))
        self.cmbViewType.setItemText(1, _translate("MainWindow", "Edited Packet", None))
        self.cmbViewType.setItemText(2, _translate("MainWindow", "Ignored Packet", None))
        self.btnClearHistory.setText(_translate("MainWindow", "Clear", None))
        self.txtData.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.cmbDetailType.setItemText(0, _translate("MainWindow", "Hexdump", None))
        self.cmbDetailType.setItemText(1, _translate("MainWindow", "Raw data", None))
        self.cmbDetailType.setItemText(2, _translate("MainWindow", "Base64", None))
        self.chkShowEdit.setText(_translate("MainWindow", "Show Edit", None))
        self.btnSaveDetail.setText(_translate("MainWindow", "Save Raw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCapture), _translate("MainWindow", "Capturing", None))
        self.chkReplace.setText(_translate("MainWindow", "Enable Replace Mode", None))
        self.chkIgnore.setText(_translate("MainWindow", "Enable Ignore Mode", None))
        self.chkEncap.setText(_translate("MainWindow", "Enable Encap/Decap", None))
        self.btnEncap.setText(_translate("MainWindow", "Browse", None))
        item = self.tblRule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "isEnabled", None))
        item = self.tblRule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type", None))
        item = self.tblRule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Match String", None))
        item = self.tblRule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Replace String", None))
        self.btnAddRule.setText(_translate("MainWindow", "Add", None))
        self.btnUpRule.setText(_translate("MainWindow", "Up", None))
        self.btnDownRule.setText(_translate("MainWindow", "Down", None))
        self.btnDelRule.setText(_translate("MainWindow", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHijack), _translate("MainWindow", "Hijacking", None))
        self.label.setText(_translate("MainWindow", "Port:", None))
        self.txtSetPort.setText(_translate("MainWindow", "9999", None))
        self.label_2.setText(_translate("MainWindow", "Logfile:", None))
        self.txtSetLog.setText(_translate("MainWindow", "socks4.log", None))
        self.btnLog.setText(_translate("MainWindow", "Browse", None))
        self.label_3.setText(_translate("MainWindow", "Hexdump width:", None))
        self.txtSetHexLen.setText(_translate("MainWindow", "16", None))
        self.label_4.setText(_translate("MainWindow", "Data length:", None))
        self.txtSetDataLen.setText(_translate("MainWindow", "1024", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), _translate("MainWindow", "Setting", None))

