'''
This script contains helper functions used to create the Steam_Recommender Database and Game_Data table

'''

# Define the create columns function
import sqlalchemy
from sqlalchemy.sql.schema import Column


def create_columns(names , types):
    '''
    function create_columns uses a list of str and a list of data type to produce a list of SqlAlchemy Column Constructors
    ( [str , str , ...]  , [type1 , type2 , ...] ) ----> [Column1 , Column2 , ...] 
    Requisites:
    list of names and type should be the same length
    sqlAlchemy helper modules such as Column , Integer , str , MetaData should be imorted prior to function's use
    '''
    from sqlalchemy.sql.schema import Column
    import sqlalchemy
    # Initialize Columns list
    Columns = [];

    # generate a Column constructor for each name passed
    for col in range(0 , len(names)):

        Columns.append(sqlalchemy.Column(names[col] , types[col]))
    

    return Columns