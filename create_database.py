'''
create_database.py creates the Steam_Recommender database and Steam_Data table in Postgres SQL
Uncomment line 30 to create a local copy of steamData.csv
 '''

# Importing dependencies
import psycopg2
import sqlalchemy #version 1.4.7
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists , create_database
from sqlalchemy import Table , Column , Integer , String , MetaData , Float , JSON


# Download steam_app_data as df
AppDF = pd.read_csv('Resources/steam_app_data.csv')

# renaming column
AppDF.rename(columns={'steam_appid':'appid'} , inplace=True)

# Loading Steamspy_data
spyDF = pd.read_csv('Resources/steamspy_data.csv')

# Joining AppDF and spyDF on appid and name
steamData = AppDF.merge(spyDF , on = ['appid' , 'name'] ,how= 'inner' )

# Saving steamData as a csv file
#steamData.to_csv('Resources/steamData.csv')

# Connect to PostgreSQL using Pscopg2
postgresEngine = create_engine('postgresql+psycopg2://postgres:Postgres@localhost/Steam_Recommender' , echo = True)

# if the database steam_recommender does not exist , create it
if not database_exists(postgresEngine.url):
    create_database(postgresEngine.url)


# Create list of column Names
colNames = steamData.columns

# Create list of column types
colTypes = []

# switch out pythonic data types with sqlAlchemy version
typesToSwitch = ['object' ,'int64' , 'float64']

for dtype in steamData.dtypes:
    
    if dtype in typesToSwitch:
        
        if dtype == 'object':
            dtype = String

        elif dtype == 'int64':
            dtype = Integer
        
        else:
            dtype = Float
        
    colTypes.append(dtype)


# Creating the table
meta = MetaData()

# Initialize list of constructors
Columns = [];

# Generate a list of Column constructors to pass to the table constructor
for col in range(0  , len(colNames)):

    Columns.append(Column(colNames[col] , colTypes[col]))

# Defining the schema of Game_Data
SteamSpy_Data = Table(
    'Steam_Data' , meta , *Columns , extend_existing= True)

meta.create_all(postgresEngine)