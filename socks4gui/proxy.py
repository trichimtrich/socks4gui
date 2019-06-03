from . import settings
from . import filters
from . import core

from twisted.internet.protocol import Factory
from twisted.protocols.socks import SOCKSv4


class MSock4Factory(Factory):
    def __init__(self):
        return super().__init__()

    def buildProtocol(self, addr):
        return MSock4()
        

#Socks4 proxy twisted
class MSock4(SOCKSv4):
    def __init__(form):
        super().__init__()
        self.form = form


    def editData(self, data): #edit data stream
        ar = []
        if filters.isIgnore:
            for st in filters.arrIgnore:
                if st in data:
                    return 2, data, ar
        s = 0
        if filters.isReplace:
            for st in filters.arrReplace:
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
        if filters.isCap:
            data = filters.modCap.deCap(0, csinfo, data)

        #replace/ignore (edit)
        status, data2, arst = self.editData(data)

        #encapsulation
        if filters.isCap:
            data2 = filters.modCap.enCap(0, csinfo, data2)

        #logging
        if 0 in filters.varObject and status in filters.varType:
            self.form.addCapture("[>] %s:%s - %s:%s" % csinfo, len(core.arrCapture), status)

        core.arrCapture.append(((0, csinfo), status, data[:settings.DATA_LEN], arst))

        return super().dataReceived(data2)

    def write(self, data):
        if not self.otherConn:
            return super().write(data)

        csinfo = self.getCSInfo()

        #decapsulation
        if filters.isCap:
            data = filters.modCap.deCap(1, csinfo, data)

        #replace/ignore (edit)
        status, data2, arst = self.editData(data)

        #encapsulation
        if filters.isCap:
            data2 = filters.modCap.enCap(1, csinfo, data2)

        #logging
        if 1 in filters.varObject and status in filters.varType:
            self.form.addCapture("[<] %s:%s - %s:%s" % csinfo, len(core.arrCapture), status)
        core.arrCapture.append(((1, csinfo), status, data[:settings.DATA_LEN], arst))

        return super().write(data)
