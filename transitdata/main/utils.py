import pandas as pd
import numpy as np
import os
import glob
from flask import current_app
from transitdata import db
# import sqlalchemy as sa
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, mapper
from transitdata.models import Base, ServiceAlerts
# from transitdata.config import Config


# source: https://stackoverflow.com/questions/11668355/sqlalchemy-get-model-from-table-name-this-may-imply-appending-some-function-to
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
        service_alert = parse_service_alerts(pd.read_csv(file_path))
        db.session.add(service_alert)
    else:
        for chunk in pd.read_csv(file_path, chunksize=10000):

            # handle integrity errors
            chunk.replace({np.nan:None}, inplace=True)
            chunk = parse_to_datetime(chunk)
            
            db.session.bulk_insert_mappings(c, chunk.to_dict(orient="records"))
            db.session.flush()

    db.session.commit()
    print("Successfully inserted: " + table_name)

def parse_header_to_dict(filepath):
    """ Return header file as document-typed Object. """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = lines[1:-1]
        print(lines)

def parse_service_alerts(df):
    """ Return header file as document-typed Object. """

    # parse to dictionary
    data = df.to_dict('list')
    data = [*data['header{'][:-1]]
    data = [item.split(' : ') for item in data]
    data = dict(zip([val[0] for val in data], [val[1] for val in data]))
    data['gtfs_realtime_version'] = data['gtfs_realtime_version'][1:-1]

    # add document values
    service_alert = ServiceAlerts()
    service_alert.header = {}
    for el in data.items():
        service_alert.header[el[0]] = el[1]

    return service_alert


def insert_transitdata():
    """ Retrieve data files and process one-by-one to be inserted into database. """    

    files = glob.glob(os.path.join("transitdata", "static", "data", "*.txt"))
    for file_path in files:
        table_name = os.path.basename(file_path)[:-4]
        print("Processing: " + table_name)
        insert_data_from(file_path, table_name)