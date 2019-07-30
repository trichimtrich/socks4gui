from struct import pack, unpack
# ! > network endian (big-endian)
# < = default - little endian
import socket
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory, ClientCreator


class Socksv5Outgoing(Protocol):
	def __init__(self, socks):
		self.socks = socks

	def connectionMade(self):
		# print "DKM DUOC ROI"
		peer = self.transport.getPeer()
		self.socks.otherConn = self
		self.socks.write(b"\x05\x00\x00\x01\x00\x00\x00\x00\x00\x00")

	def connectionLost(self, reason):
		self.transport.loseConnection()

	def dataReceived(self, data):
		self.socks.write(data)

	def write(self, data):
		self.transport.write(data)



class Socksv5(Protocol):
	def __init__(self, reactor=reactor):
		self.reactor = reactor
		self.dataStage = 0 #connect
		self.data = b""
		self.remoteAddr = ""
		self.remotePort = 0

	def connectionMade(self):
		# print "[CONNECT]", self.transport.getPeer()
		self.connectStage = 1
		self.otherConn = None

	def connectionLost(self, reason):
		if self.otherConn:
			self.otherConn.connectionLost(reason)
		self.transport.loseConnection()


	def dataReceived(self, data):
		# print "[RECV] Total %d bytes" % len(data)
		# print repr(data)

		if self.otherConn:
			self.otherConn.write(data)
			return

		self.data = self.data + data

		if self.dataStage == 0:
			self.doStage0()
		elif self.dataStage == 1:
			self.doStage1()
		else:
			self.write(b"day la response , fack you !\n")

	def doStage0(self): #first connect/authen
		data = self.data

		ver, nMethod  = unpack("!BB", data[:2]) 
		if ver != 0x5: return True

		data = data[2:]
		methods = unpack("!%dB" % nMethod, data[:nMethod])

		data = data[nMethod:]

		#set lai buffer sau khi da parse het roi
		self.data = data

		#reply lai method no authen / authen = user-pass
		self.write(b"\x05\x00")

		#change state
		self.dataStage = 1

		return True


	def doStage1(self): #first request
		data = self.data

		ver, command, rsv, addType = unpack("!BBBB", data[:4])
		if (ver != 0x5) or (command not in (1,2,3)) or (addType not in (1,3,4)): 
			return True #cai wtf ko dung dinh dang, break ngay

		data = data[4:]
		#lay cai address ra da - ipv4 / domain / ipv6
		if addType == 1: #ipv4
			#error check addr
			self.remoteAddr = socket.inet_ntoa(data[:4])
			data = data[4:]

		#error check port
		self.remotePort, = unpack("!H", data[:2])
		data = data[2:]

		# print "-- REMOTE (%s:%d)" % (self.remoteAddr, self.remotePort)

		if command == 0x1:
			pass
			#tao connect cai di

		self.data = data

		#d = self.connectClass(server, port, SOCKSv4Outgoing, self)
		ClientCreator(reactor, Socksv5Outgoing, self).connectTCP(self.remoteAddr, self.remotePort)

		#reply lai ne
		#self.write("\x05\x00\x00\x01\x00\x00\x00\x00\x00\x00")			

		#change state cai ne
		self.dataStage = 2

		return True



	def write(self, data):
		# print "[SEND] Total %d bytes" % len(data)
		# print repr(data)
		self.transport.write(data)
