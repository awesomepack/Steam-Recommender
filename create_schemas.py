'''
create_schemas.py does the following:
* Creates a database named steam_recommender if it does not exist within a local instance of PostgreSQL
* Creates schemas for our set of csv data in steam_recommender

requirements:
* in lines 24 and 27 you need to specify the file paths to the csv source files
* import your Postgres credentials for connection to Postgres

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
from credentials import password , user_name


# Download steam_data_clean.csv as df
steam_data_df = pd.read_csv('Resources/steam_data_clean.csv')

# Download steamspy_data_clean.csv as df
steamspy_df = pd.read_csv('Resources/steamspy_data_clean.csv')

# Connect to PostgreSQL using Pscopg2
postgresEngine = create_engine(f'postgresql+psycopg2://{user_name}:{password}@localhost/Steam_Recommender' , echo = True)

# if the database steam_recommender does not exist , create it
if not database_exists(postgresEngine.url):
    create_database(postgresEngine.url)

# Load steam_data_df into Steam_Recommender database
steam_data_df.to_sql('Steam_Data'  , postgresEngine , if_exists= 'replace'  )

# Load steamspy_df into Postgres
steamspy_df.to_sql('Steamspy_Data'  , postgresEngine , if_exists= 'replace'  )
    
