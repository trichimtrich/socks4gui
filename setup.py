
from PyQt5 import QtGui, QtWidgets


from twisted.internet import protocol, endpoints



def f(s):
    print("ok {}".format(s))

class hi(protocol.Protocol):
    def __init__(self, x):
        super().__init__()
        self.x = x
        return super().__init__()

    def dataReceived(self, data):
        print(">Recv[{}]: {}".format(self.x, data))
        self.transport.write(data)
        global xxx, reactor
        if data.startswith(b"cc"):
            reactor.callLater(3.5, f, "hihi")
            # xxx.stopListening()
            # print("Stop")


class hiFactory(protocol.Factory):
    def __init__(self, x):
        self.x = x
        return super().__init__()

    def buildProtocol(self, addr):
        return hi(self.x)



# print("test run")
# xxx = reactor.listenTCP(9998, hiFactory(0), interface="localhost")
# reactor.listenTCP(9999, hiFactory(1), interface="localhost")
# # x.startListening()

# import qt5reactor
# qt5reactor.install()

import main

class ffff(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, app, reactor):
        super().__init__()
        self.setupUi(self)

        self.btnListen.clicked.connect(self.btnListen_clicked)

        self.app = app
        self.reactor = reactor

    def btnListen_clicked(self):
        print("Listen")
        self.reactor.listenTCP(9999, hiFactory(0))

    def closeEvent(self, event):
        print("Quit everything!")
        self.app.quit()
        

app = QtWidgets.QApplication([])

import qt5reactor
qt5reactor.install()

from twisted.internet import reactor

formmain = ffff(app, reactor)
formmain.show()

# app.exec_()
reactor.run()
print("zz")