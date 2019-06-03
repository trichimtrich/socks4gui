# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rule.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 141)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkEnabled = QtWidgets.QCheckBox(Dialog)
        self.chkEnabled.setChecked(True)
        self.chkEnabled.setObjectName("chkEnabled")
        self.horizontalLayout.addWidget(self.chkEnabled)
        self.optReplace = QtWidgets.QRadioButton(Dialog)
        self.optReplace.setChecked(True)
        self.optReplace.setObjectName("optReplace")
        self.horizontalLayout.addWidget(self.optReplace)
        self.optIgnore = QtWidgets.QRadioButton(Dialog)
        self.optIgnore.setObjectName("optIgnore")
        self.horizontalLayout.addWidget(self.optIgnore)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtMatch = QtWidgets.QLineEdit(Dialog)
        self.txtMatch.setObjectName("txtMatch")
        self.verticalLayout_2.addWidget(self.txtMatch)
        self.txtReplace = QtWidgets.QLineEdit(Dialog)
        self.txtReplace.setObjectName("txtReplace")
        self.verticalLayout_2.addWidget(self.txtReplace)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.btnBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.verticalLayout_3.addWidget(self.btnBox)

        self.retranslateUi(Dialog)
        self.btnBox.accepted.connect(Dialog.accept)
        self.btnBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.chkEnabled.setText(_translate("Dialog", "Enabled"))
        self.optReplace.setText(_translate("Dialog", "Replace mode"))
        self.optIgnore.setText(_translate("Dialog", "Ignore mode"))
        self.label.setText(_translate("Dialog", "Match string"))
        self.label_2.setText(_translate("Dialog", "Replace string"))


