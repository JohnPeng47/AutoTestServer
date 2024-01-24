from pymongo import MongoClient
from config import settings
from logging import getLogger

logger = getLogger("base")

class DBConnection:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self, host=settings.DB_HOST, port=settings.DB_PORT, username=None, password=None):
        if not DBConnection._is_initialized:
            self._initialized = True
            self.host = host
            self.port = port
            self.username = username
            self.password = password
            self.client = None
            self.db = None
            self.connected = False

            DBConnection._is_initialized = True
            
            self.connect(settings.DB)

    def connect(self, database):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[database]

            if self.username and self.password:
                self.db.authenticate(self.username, self.password)

            self.connected = True
            print(f"Connected to database '{database}'")
        except Exception as e:
            print(f"Failed to connect to database: {e}")

    def disconnect(self):
        try:
            self.client.close()
            print("Disconnected from database")
        except Exception as e:
            print(f"Failed to disconnect from database: {e}")

    def get_collection(self, collection):
        if self.connected:
            return self.db[collection]
        else:
            print("Not connected to any database")