from twisted.internet.protocol import Factory
from twisted.protocols.socks import SOCKSv4


class MSock4Factory(Factory):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def buildProtocol(self, addr):
        return MSock4(self.app)
        

#Socks4 proxy twisted
class MSock4(SOCKSv4):
    def __init__(self, app):
        super().__init__()
        self.app = app


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
