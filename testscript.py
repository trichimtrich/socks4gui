'''
require functions: enCap, deCap

input : obj, csinfo, data
	+ obj in [0, 1] (data from sender/receiver)
	+ csinfo : node info (src/dest ip:port) = (srcip, srcport, destip, destport)
	+ data : string

output : data (in string)

'''


def enCap(obj, csinfo, data):
	if obj == 0: #sender -> receiver
		print "[+] Encapsulation " + "%s:%s --> %s:%s" % csinfo + " - Raw data length = %s" % len(data)
	else:
		print "[+] Encapsulation " + "%s:%s <-- %s:%s" % csinfo + " - Raw data length = %s" % len(data)
	return data

def deCap(obj, csinfo, data):
	if obj == 0: #sender <- receiver
		print "[+] Decapsulation " + "%s:%s --> %s:%s" % csinfo + " - Raw data length = %s" % len(data)
	else:
		print "[+] Decapsulation " + "%s:%s <-- %s:%s" % csinfo + " - Raw data length = %s" % len(data)
	return data
