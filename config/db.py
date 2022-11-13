from pymongo import MongoClient
from configparser import ConfigParser

config=ConfigParser()
config.read('config\config.ini')


client = MongoClient(config['database']['mongo'])

db=client.task_manager

collection_name = db['tasks']
