
import pandas as pd
import numpy as np
import os
import glob
import json
from flask import flash
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapper
from transitdata.models import Base, ServiceAlerts
from transitdata.config import Config


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
    dt_objects = ['date', 'start_date', 'end_date', 'start_time', 'end_time']
    for col in df.columns:
        if col in dt_objects:
            df[col] = pd.to_datetime(df[col], format='%Y%m%d')

    return df


def insert_data_from_file(file_path):

    # connect to crateDB and initiate a session
    engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    # get table name from file
    table_name = file_path.split('/')[-1][:-4]
    print(table_name)

    # identify model class 
    c = get_class_by_tablename(table_name)
    print(c)
    # read file into dataframe
    data_chunks = []
    for chunk in pd.read_csv(file_path, chunksize=200000, low_memory=False):
        data_chunks.append(chunk)
    df = pd.concat(data_chunks, axis=0)

    if table_name =='service_alerts':
        service_alert = parse_service_alerts(df)
        session.add(service_alert)
    else:
        # df = pd.read_csv(file_path, low_memory=False)
        df.replace({np.nan:None}, inplace=True) 
        df = parse_to_datetime(df)

        # get column names from file
        cols = df.columns

        # convert data to lists
        csv_data=df.values.tolist()

        for row in csv_data[:3000]:
            print(row)
            new_entry = c(*row)
            session.add(new_entry)
    session.commit()
    # flash("Account created!", "success")

def parse_service_alerts(df):
    data = df.to_dict('list')
    data = [*data['header{'][:-1]]
    data = [item.split(' : ') for item in data]
    data = dict(zip([val[0] for val in data], [val[1] for val in data]))
    data['gtfs_realtime_version'] = data['gtfs_realtime_version'][1:-1]

    service_alert = ServiceAlerts()
    service_alert.header = {}
    for el in data.items():
        service_alert.header[el[0]] = el[1]
    return service_alert


def insert_transitdata():
    files = glob.glob("transitdata/data/*.txt")
    print(files)
    file_path = 'transitdata/data/service_alerts.txt'
    insert_data_from_file(file_path)