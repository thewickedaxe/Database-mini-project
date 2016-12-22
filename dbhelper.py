from pymongo import MongoClient

class DBHelper:
    """
    This class helps the main program interface with the database
    """
    def __init__(self):
        """
        Constructor
        """
        self.mongo_client = MongoClient("mongodb://bike:bike@ds127988.mlab.com:27988/database415")
        self.db = self.mongo_client["database415"]
        self.stations = self.db["BikeStations"]
    
    def get_data(self):
        """
        Reads data from the database as a Pymongo cursor and returns it
        """
        return self.stations.find()
