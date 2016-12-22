from dbhelper import DBHelper
import datetime
import math

dbh = DBHelper()
data = dbh.get_data()
print "here"
'''for datum in data:
#	if datum["properties"]["addressZipCode"] = str(19102):
	val = str(datum["properties"]["addressZipCode"])
	if val == "19104" :
		print datum["properties"]["addressZipCode"]

for datum in data:
	print datum["properties"]["trikesAvailable"]
'''

def query1(x,y,intime):
	Mindistance = 1000000000000000000
	for datum in data:
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))*100000000000
		if Distance < Mindistance:
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet= datum["properties"]["addressStreet"]
			val1 = (datum["properties"]["openTime"])
			val2 = (datum["properties"]["closeTime"])
			Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
			Opentime = datetime.datetime.strptime(val1, '%H:%M:%S')
			Closetime = datetime.datetime.strptime(val2, '%H:%M:%S')
			if (Currenttime > Opentime) and (Currenttime < Closetime): 
				status = "Open"
			else :
				status = "Closed"

	print Stationname + " at " + Stationstreet + " is " + status
	return

query1(39.94061,-75.14958,"23:51:00")

def query2(x,y):
	Mindistance = 100000
	for datum in data:
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if Distance < Mindistance:
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Opentime = (datum["properties"]["openTime"])
			Closetime = (datum["properties"]["closeTime"])
	print Stationname + " is open from " + str(Opentime) + " to " + str(Closetime)
	return

#query2(39.94295,-75.18034)

def query3(intime):
	for datum in data:
		val1 = (datum["properties"]["openTime"])
		val2 = (datum["properties"]["closeTime"])
		Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
		Opentime = datetime.datetime.strptime(val1, '%H:%M:%S')
		Closetime = datetime.datetime.strptime(val2, '%H:%M:%S')
		if (Currenttime > Opentime) and (Currenttime < Closetime):
			print datum["properties"]["name"]
			print datum["properties"]["addressStreet"]		
	return
    

#query3("00:04:00")


def query4(station):
	for datum in data:
		val1 = (datum["properties"]["name"])
		if val1 == station :
			print datum["properties"]["bikesAvailable"]
	return

#query4("38th & Lancaster")


def query5(x,y):
	Maxdistance = 10000
	for datum in data:
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if Distance < Maxdistance and str(datum["properties"]["isVirtual"]) == "True":
			a= datum["properties"]["name"]
	print a + " is the closest station which is virtual"
	return

#query5(39.94295,-75.18034)

def query6(x,y):
	for datum in data:
		Mindistance = 100000
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if (datum["properties"]["trikesAvailable"])>0 and Distance < Mindistance:
			a=datum["properties"]["name"]
			b=datum["properties"]["addressStreet"]
	print a + " at " + b 
	return

#query6(39.94295,-75.18034)
	

def query7(station):
	for datum in data:
		val1 = (datum["properties"]["name"])
		if val1 == station:
			if (datum["properties"]["docksAvailable"]>0):
				print "Yes you can leave your bike at " + station
			else :
				print "Sorry no docks available at the moment. Please wait for a while try another station"

	return

#query7("38th & Lancaster") returns negative value

def query8():
	print "Trikes are available at these stations - "
	for datum in data:
		if datum["properties"]["trikesAvailable"]>0 :
			print str(datum["properties"]["name"]) + " at " + str(datum["properties"]["addressStreet"])
	return

#query8()

def query9(station):
	count=0
	count1=0
	for datum in data:
		if str(datum["properties"]["name"])==station:
			if str(datum["properties"]["kioskPublicStatus"]) == "Active" :
				print "Yes. " + str(datum["properties"]["name"]) + " is public."
			else :
				print "No. " + str(datum["properties"]["name"]) + " is not public."

	return

#query9("38th & Lancaster")

def query10(x,y,intime):
 	Mindistance = 100000
	for datum in data:
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		t1 = (datum["properties"]["openTime"])
		t2 = (datum["properties"]["closeTime"])
		Opentime = datetime.datetime.strptime(t1, '%H:%M:%S')
		Closetime = datetime.datetime.strptime(t2, '%H:%M:%S')
		Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if Distance < Mindistance and ((Currenttime > Opentime) and (Currenttime < Closetime)) and datum["properties"]["docksAvailable"]>0:
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet=datum["properties"]["addressStreet"]
	print Stationname + " at " +  Stationstreet
	return

#query10(39.94061,-75.14958,"23:54:00")


def query12(station):
	for datum in data:
		if str(datum["properties"]["name"])==station:
			Opentime = (datum["properties"]["openTime"])
			print  str(datum["properties"]["name"]) + " opens at " + str(Opentime) 

	return

#query12("38th & Lancaster")


#40th and spruce

