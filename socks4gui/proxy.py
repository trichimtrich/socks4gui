from twisted.internet.protocol import Factory
from twisted.protocols.socks import SOCKSv4, SOCKSv4Outgoing
from twisted.internet import protocol, reactor
from twisted.internet.threads import deferToThread
import socket

class MySOCKSv4Outgoing(SOCKSv4Outgoing):
    def __init__(self, socks):
        self.socks = socks
        self.isSSL = False


    def checkSSLCallback(self, result):
        try:
            self.isSSL = result
            if result:
                self.transport.startTLS(self.socks.factory.options)
                self.socks.transport.startTLS(self.socks.factory.options)
            self.transport.socket.setblocking(0)
            self.socks.transport.socket.setblocking(0)
            self.transport.resumeProducing()
            self.socks.transport.resumeProducing()
        except Exception as ex:
            print(ex)


    def checkSSL(self):
        try:
            data = self.socks.transport.socket.recv(4096, socket.MSG_PEEK)
            if data.startswith(b"\x16\x03"):
                return True
        except Exception as ex:
            print(ex)
        return False


    def connectionMade(self):
        super().connectionMade()
        # ssl context switch if needed?
        self.transport.pauseProducing()
        self.socks.transport.pauseProducing()
        self.transport.socket.setblocking(1)
        self.socks.transport.socket.setblocking(1)
        d = deferToThread(self.checkSSL)
        d.addCallback(self.checkSSLCallback)




class MSock4Factory(Factory):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def buildProtocol(self, addr):
        return MSock4(self.app, self)
        

#Socks4 proxy twisted
class MSock4(SOCKSv4):
    def __init__(self, app, factory):
        super().__init__()
        self.app = app
        self.factory = factory

    def connectClass(self, host, port, klass, *args):
        if klass == SOCKSv4Outgoing:
            return protocol.ClientCreator(reactor, MySOCKSv4Outgoing, *args).connectTCP(host, port)
        else:
            return super().connectClass(host, port, klass, *args)


    def editData(self, data): #edit data stream
        ar = []
        if self.app.isIgnore:
            for st in self.app.arrIgnore:
                if st in data:
                    return 2, data, ar
        s = 0
        if self.app.isReplace:
            for st in self.app.arrReplace:
                if st[0] in data:
                    data = data.replace(st[0], st[1])
                    s = 1
                    ar.append(st)
        return s, data, ar


    def getCSInfo(self): #node info (src/dest ip:port)
        peer = self.transport.getPeer()
        other_peer = self.otherConn.transport.getPeer()
        sip = peer.host
        sport = peer.port
        dip = other_peer.host
        dport = other_peer.port
        return sip, sport, dip, dport


    def dataReceived(self, data):
        if not self.otherConn:
            return super().dataReceived(data)

        csinfo = self.getCSInfo()

        #decapsulation
        # if filters.isCap: data = filters.modCap.deCap(0, csinfo, data)

        #replace/ignore (edit)
        status, data2, arst = self.editData(data)

        #encapsulation
        # if filters.isCap: data2 = filters.modCap.enCap(0, csinfo, data2)

        #logging
        if 0 in self.app.varObject and status in self.app.varType:
            self.app.addCapture("[>] %s:%s - %s:%s" % csinfo, len(self.app.bufCapture), status)

        self.app.bufCapture.append(((0, csinfo), status, data[:self.app.settings["maxData"]], arst))

        return super().dataReceived(data2)

    def write(self, data):
        if not self.otherConn:
            return super().write(data)

        csinfo = self.getCSInfo()

        #decapsulation
        # if filters.isCap: data = filters.modCap.deCap(1, csinfo, data)

        #replace/ignore (edit)
        status, data2, arst = self.editData(data)

        #encapsulation
        # if filters.isCap: data2 = filters.modCap.enCap(1, csinfo, data2)

        #logging
        if 1 in self.app.varObject and status in self.app.varType:
            self.app.addCapture("[<] %s:%s - %s:%s" % csinfo, len(self.app.bufCapture), status)
        self.app.bufCapture.append(((1, csinfo), status, data[:self.app.settings["maxData"]], arst))

        return super().write(data)
