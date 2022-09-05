from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



'''db_config.py'''
# from db_configs.db_config import *



# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



'''.env'''
# from dotenv import load_dotenv
# import os



# load_dotenv()
# env_path = ('C:/dushu_pitona/my_super_project/db_configs/.env')
# load_dotenv(dotenv_path=env_path)

# DB_USERNAME = os.getenv('DB_USERNAME')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')
# DB_NAME = os.getenv('DB_NAME')

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



'''db_config.yaml'''
# import yaml
# from yaml import Loader



# yaml_db_config = open('db_configs/db_config.yaml', 'r')
# db_config = yaml.load(yaml_db_config, Loader=Loader)

# DB_USERNAME = db_config['DB_USERNAME']
# DB_PASSWORD = db_config['DB_PASSWORD']
# DB_HOST = db_config['DB_HOST']
# DB_PORT = db_config['DB_PORT']
# DB_NAME = db_config['DB_NAME']

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



'''db_config.json'''
# import json



# with open('db_configs/db_config.json', 'r') as json_file:
# 	json_data = json.load(json_file)

# 	DB_USERNAME = json_data['DB_USERNAME']
# 	DB_PASSWORD = json_data['DB_PASSWORD']
# 	DB_HOST = json_data['DB_HOST']
# 	DB_PORT = json_data['DB_PORT']
# 	DB_NAME = json_data['DB_NAME']

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



'''db_config.pickle'''
# import json
# import pickle



# with open('db_configs/db_config.json', 'r') as json_file:
# 	json_data = json.load(json_file)

# with open('db_configs/db_config.pickle', 'wb') as pickle_file_wb:
# 	pickle.dump(json_data, pickle_file_wb)

# with open('db_configs/db_config.pickle', 'rb') as pickle_file_rb:
# 	pickle_data = pickle.load(pickle_file_rb)

# 	DB_USERNAME = pickle_data['DB_USERNAME']
# 	DB_PASSWORD = pickle_data['DB_PASSWORD']
# 	DB_HOST = pickle_data['DB_HOST']
# 	DB_PORT = pickle_data['DB_PORT']
# 	DB_NAME = pickle_data['DB_NAME']

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'



'''db_config.ini'''
# from configparser import ConfigParser



# config = ConfigParser()
# config.read('db_configs/db_config.ini')

# DB_USERNAME = config['DB_CONFIG']['DB_USERNAME']
# DB_PASSWORD = config['DB_CONFIG']['DB_PASSWORD']
# DB_HOST = config['DB_CONFIG']['DB_HOST']
# DB_PORT = config['DB_CONFIG']['DB_PORT']
# DB_NAME = config['DB_CONFIG']['DB_NAME']

# SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(
	SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
