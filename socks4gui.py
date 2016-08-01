#!/usr/bin/env python
"""
SOCKS4 Proxy

v1.0 socks4
	superkhung@vnsecurity.net
	a socks4 server based on twisted framework
	it can be use to log/modify network traffic


v2.0 socks4gui
	trichimtrich@gmail.com
	+ Add QtGui
	+ On-air content modify
	+ Log view in multiple formats
	+ User-defined encoder/decoder (python)
"""


#Core modules
from imp import load_source
from threading import Thread
from time import strftime

#Core QtGui, UI Script
from PyQt4 import QtGui
import formmain
import formrule

#Core Network
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.protocols.socks import SOCKSv4


#Setting
setport = 9999
setlog = "socks4.log"
sethexlen = 16
setdatalen = 1024
sethexfilter = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])

#Global variable
iscapture = False; bufcapture = [] #capturing status, log
isignore = True; arignore = [] #ignore mode
isreplace = True; arreplace = [] #replace mode
iscap = False; modcap = None #encoder/decoder
varObject = (0, 1) #view on sender/receiver
varType = (0, 1, 2) #view on mode (ignore/replace)


#Utilities func
def writeConsole(msg): #console log
	st = strftime("[%H:%M:%S %d/%m/%Y] ") + msg
	open(setlog, "ab+").write(st + "\n")
	formmain.txtConsole.append(st)
	formmain.txtConsole.verticalScrollBar().setValue(formmain.txtConsole.verticalScrollBar().maximum())

def addCapture(msg, ind, status=0): #list capturing
	iteminfo = QtGui.QListWidgetItem(msg)
	iteminfo.setWhatsThis(str(ind))
	if status == 1: iteminfo.setBackground(QtGui.QColor('red'))
	if status == 2: iteminfo.setBackground(QtGui.QColor('green'))
	formmain.lstCapture.addItem(iteminfo)

def addtxtData(txt, inEdit=0): #mix color in packet detail
	if inEdit == 1:
		formmain.txtData.setTextColor(QtGui.QColor('red'))
		formmain.txtData.insertPlainText(txt)
		formmain.txtData.setTextColor(QtGui.QColor('black'))
	else:
		formmain.txtData.insertPlainText(txt)
	
def parseRule():
	global arreplace, arignore
	tmpreplace = []
	tmpignore = []
	tbl = formmain.tblRule
	for i in range(tbl.rowCount()):
		if tbl.item(i, 0).text() == "True":
			if tbl.item(i, 1).text() == "Replace":
				tmpreplace.append((str(tbl.item(i, 2).text()), str(tbl.item(i, 3).text())))
			else:
				tmpignore.append(str(tbl.item(i, 2).text()))
	delreplace = arreplace
	delignore = arignore
	arreplace = tmpreplace
	arignore = tmpignore
	del delreplace
	del delignore
	writeConsole("Reparse rules\n" + "Replace: " + str(arreplace) + "\nIgnore: " + str(arignore) + "\n")

def getCSInfo(self): #node info (src/dest ip:port)
	peer = self.transport.getPeer()
	other_peer = self.otherConn.transport.getPeer()
	sip = peer.host
	sport = peer.port
	dip = other_peer.host
	dport = other_peer.port
	return sip, sport, dip, dport

def editData(data): #edit data stream
	ar = []
	if isignore:
		for st in arignore:
			if st in data:
				return 2, data, ar
	s = 0
	if isreplace:
		for st in arreplace:
			if st[0] in data:
				data = data.replace(st[0], st[1])
				s = 1
				ar.append(st)
	return s, data, ar


#Socks4 proxy twisted
class MSock4(SOCKSv4):
	def dataReceived(self, data):
		if not self.otherConn: return SOCKSv4.dataReceived(self, data)
		csinfo = getCSInfo(self)

		#decapsulation
		if iscap: data = modcap.deCap(0, csinfo, data)
		#replace/ignore (edit)
		status, data2, arst = editData(data)
		#encapsulation
		if iscap: data2 = modcap.enCap(0, csinfo, data2)

		#logging
		if 0 in varObject and status in varType:
			addCapture("[>] %s:%s - %s:%s" % csinfo, len(bufcapture), status)
		bufcapture.append(((0, csinfo), status, data[:setdatalen], arst))

		return SOCKSv4.dataReceived(self, data2)

	def write(self, data):
		if not self.otherConn: return SOCKSv4.write(self, data)
		csinfo = getCSInfo(self)

		#decapsulation
		if iscap: data = modcap.deCap(1, csinfo, data)
		#replace/ignore (edit)
		status, data2, arst = editData(data)
		#encapsulation
		if iscap: data2 = modcap.enCap(1, csinfo, data2)

		#logging
		if 1 in varObject and status in varType:
			addCapture("[<] %s:%s - %s:%s" % csinfo, len(bufcapture), status)
		bufcapture.append(((1, csinfo), status, data[:setdatalen], arst))

		return SOCKSv4.write(self, data2)


class FormRule(QtGui.QDialog, formrule.Ui_Dialog):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.optReplace.clicked.connect(self.optReplace_clicked)
		self.optIgnore.clicked.connect(self.optIgnore_clicked)

	def optReplace_clicked(self):
		self.txtReplace.setEnabled(True)

	def optIgnore_clicked(self):
		self.txtReplace.setEnabled(False)


class FormMain(QtGui.QMainWindow, formmain.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
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
		self.factory = Factory
		self.factory.protocol = MSock4


	#Widget events - Setting Tab
	def btnLog_clicked(self):
		global setlog
		fn = QtGui.QFileDialog.getSaveFileName(self, "Save log", filter='Log file (*.log);;All file (*.*)')
		if fn:
			setlog = fn
			self.txtSetLog.setText(fn)

	def txtSetPort_textChanged(self):
		global setport
		setport = int(self.txtSetPort.text())
		writeConsole("Change port to " + str(setport))

	def txtSetLog_textChanged(self):
		global setlog
		setlog = str(self.txtSetLog.text())
		writeConsole("Change log to " + setlog)

	def txtSetHexLen_textChanged(self):
		global sethexlen
		sethexlen = int(self.txtSetHexLen.text())
		writeConsole("Change HexLen to " + str(sethexlen))

	def txtSetDataLen_textChanged(self):
		global setdatalen
		setdatalen = int(self.txtSetDataLen.text())
		writeConsole("Change DataLen to " + str(setdatalen))

	#Widget events - Hijacking Tab
	def btnEncap_clicked(self):
		global modcap
		if iscapture:
			QtGui.QMessageBox.information(self, "Info", "Stop daemon first!"); return
		fn = QtGui.QFileDialog.getOpenFileName(self, "Open encap/decap module", filter='Python script (*.py);;All file (*.*)')
		if fn:
			try:
				modcap = load_source('', str(fn))
				if modcap.enCap.__class__.__name__ != "function" or modcap.deCap.__class__.__name__ != "function":
					modcap = None
			except: modcap = None
			if modcap == None:
				QtGui.QMessageBox.information(self, "Info", "Cannot load encap/decap module!")
			else:
				self.txtEncap.setText(fn)
				writeConsole("Loaded encap/decap module")

	def chkEncap_stateChanged(self):
		global iscap
		iscap = self.chkEncap.isChecked()
		if iscap: writeConsole("Capsule mode is ON")
		else: writeConsole("Capsule mode is OFF")
		if iscap == True and modcap == None:
			QtGui.QMessageBox.information(self, "Info", "Cannot load encap/decap module!")
			
	def chkReplace_stateChanged(self):
		global isreplace
		isreplace = self.chkReplace.isChecked()
		if isreplace:
			writeConsole("Replace mode is ON")
		else:
			writeConsole("Replace mode is OFF")

	def chkIgnore_stateChanged(self):
		global isignore
		isignore = self.chkIgnore.isChecked()
		if isignore:
			writeConsole("Ignore mode is ON")
		else:
			writeConsole("Ignore mode is OFF")

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

			if QtGui.QDialog.Rejected == formrule.exec_(): return
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
			QtGui.QMessageBox.information(self, "Info", "Please select a row!")

	def btnDelRule_clicked(self):
		ind = self.tblRule.currentRow()
		if ind>=0:
			self.tblRule.removeRow(ind)
			if ind<self.tblRule.rowCount():
				self.tblRule.selectRow(ind)
			parseRule()
		else:
			QtGui.QMessageBox.information(self, "Info", "Please select a row!")

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
			QtGui.QMessageBox.information(self, "Info", "Please select a row!")

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
			QtGui.QMessageBox.information(self, "Info", "Please select a row!")

	def btnAddRule_clicked(self):
		formrule = FormRule()
		if QtGui.QDialog.Rejected == formrule.exec_(): return
		ind = self.tblRule.rowCount()
		self.tblRule.insertRow(ind)
		self.tblRule.setItem(ind, 0, QtGui.QTableWidgetItem(str(formrule.chkEnabled.isChecked())))
		if formrule.optReplace.isChecked():
			self.tblRule.setItem(ind, 1, QtGui.QTableWidgetItem("Replace"))
			self.tblRule.setItem(ind, 3, QtGui.QTableWidgetItem(formrule.txtReplace.text()))
		else:
			self.tblRule.setItem(ind, 1, QtGui.QTableWidgetItem("Ignore"))
			self.tblRule.setItem(ind, 3, QtGui.QTableWidgetItem(""))
		self.tblRule.setItem(ind, 2, QtGui.QTableWidgetItem(formrule.txtMatch.text()))
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
		for i in xrange(len(bufcapture)):
			if bufcapture[i][0][0] in varObject and bufcapture[i][1] in varType:
				if bufcapture[i][0][0] == 0: #sender
					addCapture("[>] %s:%s - %s:%s" % bufcapture[i][0][1], i, bufcapture[i][1])
				else:
					addCapture("[<] %s:%s - %s:%s" % bufcapture[i][0][1], i, bufcapture[i][1])

	def btnSaveDetail_clicked(self):
		if self.lstCapture.currentRow()<0:
			QtGui.QMessageBox.information(self, "Info", "Please select a row!"); return
		fn = QtGui.QFileDialog.getSaveFileName(self, "Save raw packet", filter='Binary file (*.bin);;All file (*.*)')
		if fn:
			ind = int(self.lstCapture.currentItem().whatsThis())
			open(fn, 'wb').write(bufcapture[ind][2])

	def lstCapture_itemSelectionChanged(self):
		ind = self.lstCapture.currentRow()
		if ind<0: return
		ind = int(self.lstCapture.currentItem().whatsThis())
		if ind<0: return

		obj, status, data, arst = bufcapture[ind]

		self.txtData.clear()
		printmode = self.cmbDetailType.currentText()
		if printmode == "Raw data":
			self.txtData.insertPlainText(data)
		elif printmode == "Base64":
			self.txtData.insertPlainText(data.encode('base64'))
		elif printmode == "Hexdump":
			lines = []
			for c in xrange(0, len(data), sethexlen):
				chars = data[c:c + sethexlen]
				hex = ' '.join(['%02x' % ord(x) for x in chars])
				printable = ''.join([sethexfilter[ord(x)] for x in chars])
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
					for i in xrange(1, len(k)):
						e += [1]*len(c2); d += len(c1)
						e += c[d:d+len(k[i])]; d += len(k[i])
					data = c2.join(k)
					c = e
				
				if printmode == "Raw data":
					st = ""; inEdit = 0
					for i in xrange(len(data)):
						if inEdit != c[i]:
							addtxtData(st, inEdit)
							inEdit = c[i]; st = ""
						st += data[i]
					addtxtData(st, inEdit)

				else:
					for off in xrange(0, len(data), sethexlen):
						addtxtData("%08x:  " % off)

						linelen = sethexlen*3 + 2
						st = ""; inEdit = 0
						for i in xrange(len(data[off:off + sethexlen])):
							if inEdit != c[off+i]:
								addtxtData(st, inEdit); linelen -= len(st)
								inEdit = c[off+i]
								st = ""
							st += "%02x " % ord(data[off+i])
						addtxtData(st, inEdit); linelen -= len(st); addtxtData(' '*linelen)

						st = ""; inEdit = 0
						for i in xrange(len(data[off:off + sethexlen])):
							if inEdit != c[off+i]:
								addtxtData(st, inEdit)
								inEdit = c[off+i]
								st = ""
							st += sethexfilter[ord(data[off+i])]
						addtxtData(st, inEdit); addtxtData('\n')

	def btnListen_clicked(self):
		global iscapture
		if iscapture == False:
			reactor.listenTCP(setport, self.factory())
			writeConsole("Listen port: %s - Log file %s - Hex length %s - Data length %s" % (setport, setlog, sethexlen, setdatalen))
			Thread(target=reactor.run, args=(False,)).start()
			iscapture = True
			self.btnListen.setEnabled(not iscapture)
			self.btnStop.setEnabled(iscapture)
		else:
			QtGui.QMessageBox.information(self, "Info", "Already listening!")

	def btnStop_clicked(self):
		global iscapture
		if iscapture == True:
			reactor.stop()
			writeConsole("Stop daemon")
			iscapture = False
			self.btnListen.setEnabled(not iscapture)
			self.btnStop.setEnabled(iscapture)
		else:
			QtGui.QMessageBox.information(self, "Info", "Cannot stop!")

	def btnClearHistory_clicked(self):
		global bufcapture
		self.lstCapture.clear()
		self.txtData.clear()
		bufcapture = []
		writeConsole("History clear")

app = QtGui.QApplication([])
formmain = FormMain()
formmain.show()
app.exec_()

if iscapture == True: reactor.stop()