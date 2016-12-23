from dbhelper import DBHelper
import datetime
import math

# Query for Is the closest bike station open?
# x,y are the GPS coordinates, while time is the current time.
def query1(x,y,intime):	
	dbh = DBHelper()
	data = dbh.get_data()
	Mindistance = 10000000
	e=0
# Iterates over the database one object at a time.
	for datum in data:
		# Val1 stores the value of x coordinate and Val2 stores the value of y coordinate
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		# Calculates the euclidian distance
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		# Check for the closest station
		if Distance < Mindistance:
			e=1
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet= datum["properties"]["addressStreet"]
			# Val1 and Val 2 are assigned the opening and closing times of the station respectively
			val1 = (datum["properties"]["openTime"])
			val2 = (datum["properties"]["closeTime"])
			# Converting the input into a time object with the required fields, such that it can be compared.
			Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
			Opentime = datetime.datetime.strptime(val1, '%H:%M:%S')
			Closetime = datetime.datetime.strptime(val2, '%H:%M:%S')
			#Checks if station is open
			if (Currenttime > Opentime) and (Currenttime < Closetime): 
				status = "Open"
			else :
				status = "Closed"
	if e == 1 :
		print Stationname + " at " + Stationstreet + " is " + status
	else :
		print "There are no stations in your vicinity"
	return
#Sample query
#query1(-75.15993,39.94517,"23:51:00")

# Till what time is the closet bike station open?
# x and y are the GPS coordinates
def query2(x,y):
	dbh = DBHelper()
	data = dbh.get_data()
	Mindistance = 100000
	e=0
	# Iterates over the database one object at a time.
	for datum in data:
		# Val1 stores the value of x coordinate and Val2 stores the value of y coordinate
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		# Retrieves the timing details of the closest station
		if Distance < Mindistance:
			e=1
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Opentime = (datum["properties"]["openTime"])
			Closetime = (datum["properties"]["closeTime"])
	if e == 1:
		print Stationname + " is open from " + str(Opentime) + " to " + str(Closetime)
	else :
		print "There are no stations in your vicinity"
	return

#query2(39.94295,-75.18034)


#1.	Where can I get a bike at this time?
# Takes in time as an input and returns the list of stations open
def query3(intime):
	dbh = DBHelper()
	data = dbh.get_data()
	for datum in data:
		# Val1 and Val 2 are assigned the opening and closing times of the station respectively
		val1 = (datum["properties"]["openTime"])
		val2 = (datum["properties"]["closeTime"])
		# Converting the input into a time object with the required fields, such that it can be compared.
		Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
		Opentime = datetime.datetime.strptime(val1, '%H:%M:%S')
		Closetime = datetime.datetime.strptime(val2, '%H:%M:%S')
		# Checks if station is open
		if (Currenttime > Opentime) and (Currenttime < Closetime):
			print datum["properties"]["name"]
			print datum["properties"]["addressStreet"]		
	return
    

#query3("00:04:00")

# How many bikes are available at _____ station? 
# Takes in the name of the station as input and returns the number of bikes
def query4(station):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	for datum in data:
		val1 = (datum["properties"]["name"])
		if station.lower() in val1.lower():
			e=1
			print val1
			print "Bikes available: " + str(datum["properties"]["bikesAvailable"]) + "\n"
	if e==0:
		print "Please enter a valid station name"
	return

#query4("38th & Lancaster")

#Are there any virtual stations nearby for me to book a ride?
# Input x and y coordinates. Outputs the closest virtual station
def query5(x,y):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	Maxdistance = 10000
	for datum in data:
		# Val1 and Val 2 are assigned the opening and closing times of the station respectively
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		# Calculates Euclidian Distance
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		# Checks for the closest virtual station
		if Distance < Maxdistance and str(datum["properties"]["isVirtual"]) == "True":
			e=1
			a= datum["properties"]["name"]
	if e==1:
		print a + " is the closest station which is virtual"
	else :
		print " No virtual stations in the vicinity"
	return

#query5(-75.15993,39.94517)

#Which is the closest station that has a trike?
# Input GPS coordinates. Outputs the closest station name and address which has a trike
def query6(x,y):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	for datum in data:
		Mindistance = 100000
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		#Calculates euclidian distance
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		#Checks for the closest stations that have a trike
		if (datum["properties"]["trikesAvailable"])>0 and Distance < Mindistance:
			e=1
			a=datum["properties"]["name"]
			b=datum["properties"]["addressStreet"]
	if e==1:
		print a + " at " + b 
	else :
		print" No trikes available in the vicinity" 
	return

#query6(-75.15993,39.94517)
	
# Can I drop of a trike at _____ station?
# Input a station name. Outputs a yes or no.
def query7(station):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	for datum in data:
		val1 = str(datum["properties"]["name"])
		# Checks for the particular station
		if station.lower() in val1.lower():
			e=1
			if (datum["properties"]["docksAvailable"]>0):
				print "Yes you can leave your bike at " + str(datum["properties"]["name"])
				return				
	if e==0:
		print "Sorry no docks available at the moment near that place. Please wait for a while try another station"
	return

#query7("38th & Lancaster")

#Which stations have trikes?
# Input not needed, Outputs a list of all stations that have trikes.
def query8():
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	print "Trikes are available at these stations - "
	for datum in data:
		if datum["properties"]["trikesAvailable"]>0 :
			e=1
			print str(datum["properties"]["name"]) + " at " + str(datum["properties"]["addressStreet"])
	if e==0:
		print "No trikes available. Sorry"
	return

#query8()

#Is _____ station a public station?
# Input a stations name. Outputs if the station is available for public use>
def query9(station):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	for datum in data:
		if station.lower() in str(datum["properties"]["name"]).lower():
			e=1
			if str(datum["properties"]["kioskPublicStatus"]) == "Active" :
				print "Yes. " + str(datum["properties"]["name"]) + " is public."
			else :
				print "No. " + str(datum["properties"]["name"]) + " is not public."
	if e==0:
		print "Please enter a valid station name"
	return

#query9("38th & Lancaster")

# Where can I leave a bike?
# Input the GPS coordinates and the current time. 
def query10(x,y,intime):
	dbh = DBHelper()
	data = dbh.get_data()
 	Mindistance = 100000
 	e=0
	for datum in data:
		# Val1 stores the value of x coordinate and Val2 stores the value of y coordinate
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		# T1 stores the opening time and T2 stores the value of the closetime coordinate
		t1 = (datum["properties"]["openTime"])
		t2 = (datum["properties"]["closeTime"])
		Opentime = datetime.datetime.strptime(t1, '%H:%M:%S')
		Closetime = datetime.datetime.strptime(t2, '%H:%M:%S')
		Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
		# Calculates the euclidian distance
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		# Checks for the station closest to the person with open docks and open at the time.
		if Distance < Mindistance and ((Currenttime > Opentime) and (Currenttime < Closetime)) and datum["properties"]["docksAvailable"]>0:
			e=1
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet=datum["properties"]["addressStreet"]
	if e==1:
		print Stationname + " at " +  Stationstreet
	else :
		print("Sorry. But no stations are open at this time in your vicinity")
	return

#query10(-75.17747,39.94218,"23:54:00")


#Can I leave my bike at the closest station?
# Inputs x, y and current time. Returns a yes or a no.
def query11(x,y,intime):
	dbh = DBHelper()
	data = dbh.get_data()
	Mindistance = 100000
	e=0
	for datum in data:
		# Val1 stores the value of x coordinate and Val2 stores the value of y coordinate
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		# T1 stores the opening time and T2 stores the value of the closetime coordinate
		t1 = (datum["properties"]["openTime"])
		t2 = (datum["properties"]["closeTime"])
		# Converting the input into a time object with the required fields, such that it can be compared.
		Opentime = datetime.datetime.strptime(t1, '%H:%M:%S')
		Closetime = datetime.datetime.strptime(t2, '%H:%M:%S')
		Currenttime = datetime.datetime.strptime(intime, '%H:%M:%S')
		# Calculates euclidian distance
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if Distance < Mindistance:
			e=1
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet=datum["properties"]["addressStreet"]
			# Checks if the station is open or not
			if ((Currenttime > Opentime) and (Currenttime < Closetime)) and datum["properties"]["docksAvailable"]>0:
				status="Yes, you can leave your bike at "
			else:
				status="No, you cannot leave your bike at "
	if e==1:
		print status + Stationname + " at " +  Stationstreet
	else : 
		print "Sorry. But no stations are open at this time in your vicinity"
	return

#query11(-75.17747,39.94218,"23:54:00")

# What time does _____ station open?
# Inputs station name. Returns the opening time
def query12(station):
	dbh = DBHelper()
	data = dbh.get_data()
	e=0
	for datum in data:
		if station.lower() in str(datum["properties"]["name"]).lower():
			e=1
			Opentime = (datum["properties"]["openTime"])
			print  str(datum["properties"]["name"]) + " opens at " + str(Opentime) 
	if e==0:
		print "Please enter a valid station name "
	return

#query12("38th & Lancaster")

#What are the events stations?
#Input nothing. Outputs a list of event based stations
def query13():
	dbh = DBHelper()
	data = dbh.get_data()
	for datum in data:
		if str(datum["properties"]["isEventBased"]) == "True":
			print str(datum["properties"]["name"])
	return

#query13()

#When and where in the bike stations are the events scheduled?
#Input nothing. Outputs the list of Events.
def query14():
	dbh = DBHelper()
	data = dbh.get_data()
	for datum in data:
		if str(datum["properties"]["isEventBased"]) == "True":
			print str(datum["properties"]["name"]) + " hosts an event from " + str(datum["properties"]["eventStart"]) + " to " + str(datum["properties"]["eventEnd"])
	return

#query14()

#Which is the closest station which has more than 5 bikes?
# Input as the GPS coordinates and number of bikes. Returns the closest station.
def query15(x,y,n):
	dbh = DBHelper()
	data = dbh.get_data()
	Mindistance = 100000
	e=0
	for datum in data:
		# Val1 and Val2 stores the value of GPS coordinates.
		val1 = (datum["geometry"]["coordinates"][0])
		val2 = (datum["geometry"]["coordinates"][1])
		# Calculates the Euclidian Distance.
		Distance = math.sqrt((x-val1)*(x-val1) + (y-val2)*(y-val2))
		if Distance < Mindistance and datum["properties"]["bikesAvailable"]> n:
			e=1
			Mindistance = Distance
			Stationname= datum["properties"]["name"]
			Stationstreet=datum["properties"]["addressStreet"]
	if e==1:
		print str(Stationname) + " at " +  str(Stationstreet)
	else :
		print "No stations in the vicinity with " + str(n) + " bikes."
	return

#query15(-75.19701,39.96046,7)
