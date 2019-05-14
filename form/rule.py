# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formrule.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(461, 141)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.chkEnabled = QtGui.QCheckBox(Dialog)
        self.chkEnabled.setChecked(True)
        self.chkEnabled.setObjectName(_fromUtf8("chkEnabled"))
        self.horizontalLayout.addWidget(self.chkEnabled)
        self.optReplace = QtGui.QRadioButton(Dialog)
        self.optReplace.setChecked(True)
        self.optReplace.setObjectName(_fromUtf8("optReplace"))
        self.horizontalLayout.addWidget(self.optReplace)
        self.optIgnore = QtGui.QRadioButton(Dialog)
        self.optIgnore.setObjectName(_fromUtf8("optIgnore"))
        self.horizontalLayout.addWidget(self.optIgnore)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.txtMatch = QtGui.QLineEdit(Dialog)
        self.txtMatch.setObjectName(_fromUtf8("txtMatch"))
        self.verticalLayout_2.addWidget(self.txtMatch)
        self.txtReplace = QtGui.QLineEdit(Dialog)
        self.txtReplace.setObjectName(_fromUtf8("txtReplace"))
        self.verticalLayout_2.addWidget(self.txtReplace)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.btnBox = QtGui.QDialogButtonBox(Dialog)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout_3.addWidget(self.btnBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.btnBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.chkEnabled.setText(_translate("Dialog", "Enabled", None))
        self.optReplace.setText(_translate("Dialog", "Replace mode", None))
        self.optIgnore.setText(_translate("Dialog", "Ignore mode", None))
        self.label.setText(_translate("Dialog", "Match string", None))
        self.label_2.setText(_translate("Dialog", "Replace string", None))

