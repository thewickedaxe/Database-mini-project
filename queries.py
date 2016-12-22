from dbhelper import DBHelper

dbh = DBHelper()
data = dbh.get_data()
print "here"
non_virtual_station = []
for datum in data:
#	if datum["properties"]["addressZipCode"] = str(19102):
	val = str(datum["properties"]["addressZipCode"])
	if val == "19104" :
		print datum["properties"]["addressZipCode"]
    