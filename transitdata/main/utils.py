import os
import glob
import pandas as pd
import numpy as np
from flask import current_app
from sqlalchemy.exc import SQLAlchemyError
from transitdata import db
from transitdata.models import Base, ServiceAlerts


"""
from source: "https://stackoverflow.com/questions/11668355/ \
            sqlalchemy-get-model-from-table-name-this-may- \
            imply-appending-some-function-to" 
"""
def get_class_by_tablename(table_fullname):
    """
    Return class reference mapped to table.
    :param table_fullname: String with fullname of table.
    :return: Class reference or None.

    """
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
            return c

def parse_to_datetime(df):
    """ Return dataframe with converted datetime objects. """

    dt_objects = ['date', 'start_date', 'end_date', 'start_time', 'end_time']
    for col in df.columns:
        if col in dt_objects:
            df[col] = pd.to_datetime(df[col], format='%Y%m%d')

    return df

def insert_data_from(file_path, table_name):
    """ 
    Inserts csv data from a given file path to a database by mapping app models. 
    To handle big amounts of data and to speed-up processes, files are processed 
    in chunks and loaded in bulk to the database.
    
    """
    c = get_class_by_tablename(table_name)

    # handle service alert messages, else all other files in table format
    if table_name =='service_alerts':
        header = parse_header_to_dict(file_path)
        service_alert = ServiceAlerts(header)
        try:
            db.session.add(service_alert)
        except SQLAlchemyError as e:
            print(e)
            db.session.rollback()
    else:
        for chunk in pd.read_csv(file_path, chunksize=10000):

            # handle integrity errors
            chunk.replace({np.nan:None}, inplace=True)
            chunk = parse_to_datetime(chunk)

            # insert data
            try:
                db.session.bulk_insert_mappings(c, chunk.to_dict(orient="records"))
                db.session.flush()
                db.session.commit()
            except SQLAlchemyError as e:
                print(e)
                db.session.rollback()
        print("\nSuccessfully inserted: " + table_name + "\n")
    
def parse_header_to_dict(file_path):
    """ 
    Return header file values as dictionary. 
    Remove whitespaces and quotation marks. 
        
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = lines[2:-1]
        lines = [line.strip().replace('\"', '') for line in lines]
        lines = [line.split(' : ') for line in lines]
        lines = dict(zip([val[0] for val in lines], [val[1] for val in lines]))

    return lines

def insert_transitdata():
    """ Retrieve data files and insert each into database. """    

    files = glob.glob(os.path.join("transitdata", "static", "data", "*.txt"))
    for file_path in files:
        table_name = os.path.basename(file_path)[:-4]
        print("\nProcessing: " + table_name + " ...")
        insert_data_from(file_path, table_name)