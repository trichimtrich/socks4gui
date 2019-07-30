from PyQt5 import QtGui, QtWidgets
from .form import rule as formrule
from .form import main as formmain

from imp import load_source
from time import strftime

class Application(QtWidgets.QApplication):
    def __init__(self, *args):
        super().__init__(*args)

        self.settings = {
            "host": "0.0.0.0",
            "port": 9999,
            "logFile": "socks4.log",
            "hexWidth": 16,
            "maxData": 1024,
        }

        self.isIgnore = True
        self.arrIgnore = []

        self.isReplace = True
        self.arrReplace = []

        self.isCap = False
        self.modCap = None

        self.varObject = (0, 1)
        self.varType = (0, 1, 2)

        self.isCapture = False
        self.bufCapture = []


    def run(self):
        import qt5reactor
        qt5reactor.install()
        from twisted.internet import reactor
        from .proxy import MSock4Factory
        
        self.mainWindow = FormMain(self, reactor, MSock4Factory)
        self.mainWindow.show()

        reactor.run()

    
    #Utilities func
    def writeConsole(self, msg): #console log
        st = strftime("[%H:%M:%S %d/%m/%Y] ") + msg
        open(self.settings["logFile"], "a+").write(st + "\n")
        self.mainWindow.txtConsole.append(st)
        maximumScroll = self.mainWindow.txtConsole.verticalScrollBar().maximum()
        self.mainWindow.txtConsole.verticalScrollBar().setValue(maximumScroll)


    def addCapture(self, msg, ind, status=0): #list capturing
        itemInfo = QtWidgets.QListWidgetItem(msg)
        itemInfo.setWhatsThis(str(ind))
        if status == 1: itemInfo.setBackground(QtGui.QColor('red'))
        if status == 2: itemInfo.setBackground(QtGui.QColor('green'))
        self.mainWindow.lstCapture.addItem(itemInfo)

    def addtxtData(self, txt, inEdit=0): #mix color in packet detail
        if inEdit == 1:
            self.mainWindow.txtData.setTextColor(QtGui.QColor('red'))
            self.mainWindow.txtData.insertPlainText(txt)
            self.mainWindow.txtData.setTextColor(QtGui.QColor('black'))
        else:
            self.mainWindow.txtData.insertPlainText(txt)
        


class FormRule(QtWidgets.QDialog, formrule.Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.optReplace.clicked.connect(self.optReplace_clicked)
        self.optIgnore.clicked.connect(self.optIgnore_clicked)

    def optReplace_clicked(self):
        self.txtReplace.setEnabled(True)

    def optIgnore_clicked(self):
        self.txtReplace.setEnabled(False)


class FormMain(QtWidgets.QMainWindow, formmain.Ui_MainWindow):
    def __init__(self, app, reactor, factory):
        super().__init__()

        self.setupUi(self)

        #main button
        self.btnListen.clicked.connect(self.btnListen_clicked)
        self.btnStop.clicked.connect(self.btnStop_clicked)
        
        #tab capture
        self.lstCapture.itemSelectionChanged.connect(self.lstCapture_itemSelectionChanged)
        self.cmbViewObject.currentIndexChanged.connect(self.cmbViewObject_itemSelectionChanged)
        self.cmbViewType.currentIndexChanged.connect(self.cmbViewObject_itemSelectionChanged)
        self.btnClearHistory.clicked.connect(self.btnClearHistory_clicked)

        self.cmbDetailType.currentIndexChanged.connect(self.lstCapture_itemSelectionChanged)
        self.chkShowEdit.stateChanged.connect(self.lstCapture_itemSelectionChanged)
        self.btnSaveDetail.clicked.connect(self.btnSaveDetail_clicked)

        #tab hijack
        self.chkReplace.stateChanged.connect(self.chkReplace_stateChanged)
        self.chkIgnore.stateChanged.connect(self.chkIgnore_stateChanged)

        self.btnEncap.clicked.connect(self.btnEncap_clicked)
        self.chkEncap.stateChanged.connect(self.chkEncap_stateChanged)

        self.btnAddRule.clicked.connect(self.btnAddRule_clicked)
        self.btnDelRule.clicked.connect(self.btnDelRule_clicked)
        self.btnUpRule.clicked.connect(self.btnUpRule_clicked)
        self.btnDownRule.clicked.connect(self.btnDownRule_clicked)        
        self.tblRule.itemDoubleClicked.connect(self.tblRule_itemDoubleClicked)

        #tab setting
        self.txtSetPort.editingFinished.connect(self.txtSetPort_textChanged)
        self.txtSetLog.editingFinished.connect(self.txtSetLog_textChanged)
        self.btnLog.clicked.connect(self.btnLog_clicked)
        self.txtSetHexLen.editingFinished.connect(self.txtSetHexLen_textChanged)
        self.txtSetDataLen.editingFinished.connect(self.txtSetDataLen_textChanged)

        #twisted socks4
        self.app = app
        self.reactor = reactor
        self.factory = factory

    def closeEvent(self, event):
        self.app.quit()


    #Widget events - Setting Tab
    def btnLog_clicked(self):
        # global setlog
        # fn = QtWidgets.QFileDialog.getSaveFileName(self, "Save log", filter='Log file (*.log);;All file (*.*)')
        # if fn:
        #     setlog = fn
        #     self.txtSetLog.setText(fn)
        pass


    def txtSetPort_textChanged(self):
        newPort = int(self.txtSetPort.text())
        self.app.settings["port"] = newPort
        self.app.writeConsole("Change port to {}".format(newPort))


    def txtSetLog_textChanged(self):
        newLogFile = str(self.txtSetLog.text())
        self.app.settings["logFile"] = newLogFile
        self.app.writeConsole("Change log to {}".format(repr(newLogFile)))


    def txtSetHexLen_textChanged(self):
        newHexWidth = int(self.txtSetHexLen.text())
        self.app.settings["hexWidth"] = newHexWidth
        self.app.writeConsole("Change HexLen to {}".format(newHexWidth))

    def txtSetDataLen_textChanged(self):
        newMaxData = int(self.txtSetDataLen.text())
        self.app.settings["maxData"] = newMaxData
        self.app.writeConsole("Change DataLen to {}".format(newMaxData))


    #Widget events - Hijacking Tab
    def btnEncap_clicked(self):
        if self.app.isCapture:
            QtWidgets.QMessageBox.information(self, "Info", "Stop daemon first!"); return
        fn = QtWidgets.QFileDialog.getOpenFileName(self, "Open encap/decap module", filter='Python script (*.py);;All file (*.*)')
        if fn:
            try:
                mod = load_source('', str(fn))
                if mod.enCap.__class__.__name__ != "function" or mod.deCap.__class__.__name__ != "function":
                    mod = None
            except:
                mod = None

            self.app.modCap = mod

            if mod == None:
                QtWidgets.QMessageBox.information(self, "Info", "Cannot load encap/decap module!")
            else:
                self.txtEncap.setText(fn)
                self.app.writeConsole("Loaded encap/decap module")


    def chkEncap_stateChanged(self):
        isCap = self.chkEncap.isChecked()
        self.app.isCap = isCap
        if isCap:
            self.app.writeConsole("Capsule mode is ON")
        else:
            self.app.writeConsole("Capsule mode is OFF")

        if isCap and self.app.modCap == None:
            QtWidgets.QMessageBox.information(self, "Info", "Cannot load encap/decap module!")
            
    def chkReplace_stateChanged(self):
        isReplace = self.chkReplace.isChecked()
        self.app.isReplace = isReplace
        if isReplace:
            self.app.writeConsole("Replace mode is ON")
        else:
            self.app.writeConsole("Replace mode is OFF")

    def chkIgnore_stateChanged(self):
        isIgnore = self.chkIgnore.isChecked()
        self.app.isIgnore = isIgnore
        if isIgnore:
            self.app.writeConsole("Ignore mode is ON")
        else:
            self.app.writeConsole("Ignore mode is OFF")


    def tblRule_itemDoubleClicked(self):
        ind = self.tblRule.currentRow()
        if ind>=0:
            formrule = FormRule()
            formrule.chkEnabled.setChecked(self.tblRule.item(ind, 0).text() == "True")
            if self.tblRule.item(ind, 1).text() == "Replace":
                formrule.optReplace.setChecked(True)
            else:
                formrule.optIgnore.setChecked(True)
                formrule.txtReplace.setEnabled(False)
            formrule.txtMatch.setText(self.tblRule.item(ind, 2).text())
            formrule.txtReplace.setText(self.tblRule.item(ind, 3).text())

            if QtWidgets.QDialog.Rejected == formrule.exec_(): return
            self.tblRule.item(ind, 0).setText(str(formrule.chkEnabled.isChecked()))
            if formrule.optReplace.isChecked():
                self.tblRule.item(ind, 1).setText("Replace")
                self.tblRule.item(ind, 3).setText(formrule.txtReplace.text())
            else:
                self.tblRule.item(ind, 1).setText("Ignore")
                self.tblRule.item(ind, 3).setText("")
            self.tblRule.item(ind, 2).setText(formrule.txtMatch.text())
            parseRule()
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Please select a row!")


    def btnDelRule_clicked(self):
        ind = self.tblRule.currentRow()
        if ind>=0:
            self.tblRule.removeRow(ind)
            if ind<self.tblRule.rowCount():
                self.tblRule.selectRow(ind)
            parseRule()
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Please select a row!")


    def btnUpRule_clicked(self):
        ind = self.tblRule.currentRow()
        if ind>=0:
            if ind>0:
                ar = [self.tblRule.item(ind-1, x).text() for x in range(4)]
                for i in range(4): 
                    self.tblRule.item(ind-1, i).setText(self.tblRule.item(ind, i).text())
                    self.tblRule.item(ind, i).setText(ar[i])
                self.tblRule.selectRow(ind-1)
                parseRule()
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Please select a row!")


    def btnDownRule_clicked(self):
        ind = self.tblRule.currentRow()
        if ind>=0 and ind<=self.tblRule.rowCount()-1:
            if ind<self.tblRule.rowCount()-1:
                ar = [self.tblRule.item(ind, x).text() for x in range(4)]
                for i in range(4): 
                    self.tblRule.item(ind, i).setText(self.tblRule.item(ind+1, i).text())
                    self.tblRule.item(ind+1, i).setText(ar[i])
                self.tblRule.selectRow(ind+1)
                parseRule()
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Please select a row!")


    def btnAddRule_clicked(self):
        formrule = FormRule()
        if QtWidgets.QDialog.Rejected == formrule.exec_(): return
        ind = self.tblRule.rowCount()
        self.tblRule.insertRow(ind)
        self.tblRule.setItem(ind, 0, QtWidgets.QTableWidgetItem(str(formrule.chkEnabled.isChecked())))
        if formrule.optReplace.isChecked():
            self.tblRule.setItem(ind, 1, QtWidgets.QTableWidgetItem("Replace"))
            self.tblRule.setItem(ind, 3, QtWidgets.QTableWidgetItem(formrule.txtReplace.text()))
        else:
            self.tblRule.setItem(ind, 1, QtWidgets.QTableWidgetItem("Ignore"))
            self.tblRule.setItem(ind, 3, QtWidgets.QTableWidgetItem(""))
        self.tblRule.setItem(ind, 2, QtWidgets.QTableWidgetItem(formrule.txtMatch.text()))
        parseRule()
        

    #Widgets events - Capturing tab
    def cmbViewObject_itemSelectionChanged(self):
        global varObject, varType

        st = self.cmbViewObject.currentText()
        if st == "All": varObject = (0, 1)
        elif st == "From Sender": varObject = (0,)
        else: varObject = (1,)
        
        st = self.cmbViewType.currentText()
        if st == "All": varType = (0, 1, 2)
        elif st == "Edited Packet": varType = (1,)
        else: varType = (2,)

        self.lstCapture.clear()
        self.txtData.clear()
        for i in range(len(bufcapture)):
            if bufcapture[i][0][0] in varObject and bufcapture[i][1] in varType:
                if bufcapture[i][0][0] == 0: #sender
                    addCapture("[>] %s:%s - %s:%s" % bufcapture[i][0][1], i, bufcapture[i][1])
                else:
                    addCapture("[<] %s:%s - %s:%s" % bufcapture[i][0][1], i, bufcapture[i][1])

    def btnSaveDetail_clicked(self):
        if self.lstCapture.currentRow()<0:
            QtWidgets.QMessageBox.information(self, "Info", "Please select a row!"); return
        fn = QtWidgets.QFileDialog.getSaveFileName(self, "Save raw packet", filter='Binary file (*.bin);;All file (*.*)')
        if fn:
            ind = int(self.lstCapture.currentItem().whatsThis())
            open(fn, 'wb').write(bufcapture[ind][2])

    def lstCapture_itemSelectionChanged(self):
        ind = self.lstCapture.currentRow()
        
        if ind < 0:
            return

        ind = int(self.lstCapture.currentItem().whatsThis())
        
        if ind < 0:
            return

        obj, status, data, arst = self.app.bufCapture[ind]

        self.txtData.clear()
        printmode = self.cmbDetailType.currentText()
        if printmode == "Raw data":
            self.txtData.insertPlainText(data)
        elif printmode == "Base64":
            self.txtData.insertPlainText(data.encode('base64'))
        elif printmode == "Hexdump":
            lines = []
            sethexlen = self.app.settings["hexWidth"]
            sethexfilter = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
            for c in range(0, len(data), sethexlen):
                chars = data[c:c + sethexlen]
                hex = ' '.join(['%02x' % x for x in chars])
                printable = ''.join([sethexfilter[x] for x in chars])
                lines.append('%08x:  %-*s  %s\n' % (c, sethexlen * 3, hex, printable))
            self.txtData.insertPlainText(''.join(lines))

        if status == 1 and self.chkShowEdit.isChecked():
            self.txtData.insertHtml("<br><b>" + "-"*32 + "</b><br><br>")
            if printmode == "Base64":
                for st in arst:
                    data = data.replace(st[0], st[1])
                self.txtData.insertPlainText(data.encode('base64'))
            else:
                c = [0]*len(data)
                for c1, c2 in arst:
                    k = data.split(c1)
                    e = c[:len(k[0])]
                    d = len(k[0])
                    for i in range(1, len(k)):
                        e += [1]*len(c2); d += len(c1)
                        e += c[d:d+len(k[i])]; d += len(k[i])
                    data = c2.join(k)
                    c = e
                
                if printmode == "Raw data":
                    st = ""; inEdit = 0
                    for i in range(len(data)):
                        if inEdit != c[i]:
                            addtxtData(st, inEdit)
                            inEdit = c[i]; st = ""
                        st += data[i]
                    addtxtData(st, inEdit)

                else:
                    for off in range(0, len(data), sethexlen):
                        addtxtData("%08x:  " % off)

                        linelen = sethexlen*3 + 2
                        st = ""; inEdit = 0
                        for i in range(len(data[off:off + sethexlen])):
                            if inEdit != c[off+i]:
                                addtxtData(st, inEdit); linelen -= len(st)
                                inEdit = c[off+i]
                                st = ""
                            st += "%02x " % ord(data[off+i])
                        addtxtData(st, inEdit); linelen -= len(st); addtxtData(' '*linelen)

                        st = ""; inEdit = 0
                        for i in range(len(data[off:off + sethexlen])):
                            if inEdit != c[off+i]:
                                addtxtData(st, inEdit)
                                inEdit = c[off+i]
                                st = ""
                            st += sethexfilter[ord(data[off+i])]
                        addtxtData(st, inEdit); addtxtData('\n')


    def btnListen_clicked(self):
        if self.app.isCapture == False:
            port = self.app.settings["port"]
            host = self.app.settings["host"]
            logFile = self.app.settings["logFile"]
            hexWidth = self.app.settings["hexWidth"]
            maxData = self.app.settings["maxData"]

            factory = self.factory(self.app)

            from OpenSSL import crypto
            from twisted.internet import ssl
            pem_priv = open("/Users/dangmt/Desktop/share/weirdsocket/cert/web.weirdsocket.com.key", "rb").read()
            pem_cert = open("/Users/dangmt/Desktop/share/weirdsocket/cert/web.weirdsocket.com.crt", "rb").read()

            priv = ssl.KeyPair.load(pem_priv, format=crypto.FILETYPE_PEM)
            cert = ssl.PrivateCertificate.load(pem_cert, priv, format=crypto.FILETYPE_PEM)
            factory.options = cert.options()

            self.listener = self.reactor.listenTCP(port, factory, interface=host)
            self.app.writeConsole("Listen port: {} - Log file {} - Hex length {} - Data length {}".format(port, repr(logFile), hexWidth, maxData))
            self.app.isCapture = True
            self.btnListen.setEnabled(False)
            self.btnStop.setEnabled(True)
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Already listening!")

    def btnStop_clicked(self):
        if self.app.isCapture == True:
            self.listener.stopListening()
            self.app.writeConsole("Stop daemon")
            self.app.isCapture = False
            self.btnListen.setEnabled(True)
            self.btnStop.setEnabled(False)
        else:
            QtWidgets.QMessageBox.information(self, "Info", "Cannot stop!")

    def btnClearHistory_clicked(self):
        self.lstCapture.clear()
        self.txtData.clear()
        self.app.bufCapture = []
        self.app.writeConsole("History clear")

