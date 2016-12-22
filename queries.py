from dbhelper import DBHelper
import datetime

dbh = DBHelper()
data = dbh.get_data()
print "here"
non_virtual_station = []
'''for datum in data:
#	if datum["properties"]["addressZipCode"] = str(19102):
	val = str(datum["properties"]["addressZipCode"])
	if val == "19104" :
		print datum["properties"]["addressZipCode"]
'''


def query3(intime):
	for datum in data:
		val1 = (datum["properties"]["openTime"])
		val2 = (datum["properties"]["closeTime"])
		time1 = datetime.datetime.strptime(intime, '%H:%M:%S')
		time2 = datetime.datetime.strptime(val1, '%H:%M:%S')
		time3 = datetime.datetime.strptime(val2, '%H:%M:%S')
		if (time1 > time2) and (time1 < time3):
			print datum["properties"]["name"]
			print datum["properties"]["addressStreet"]		
	return
    

query3("23:59:00")


def query4():
	for datum in data:
		val1 = (datum["properties"]["name"])
		if val1 == "penn" :
			print datum["properties"]["name"]
			print datum["properties"]["addressStreet"]	
	return

#query4()
