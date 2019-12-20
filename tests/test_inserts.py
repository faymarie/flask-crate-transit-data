import time
import pytest
from transitdata import db
from transitdata.models import (Agency, Calendar, CalendarDates, 
                                Frequencies, Routes, ServiceAlerts,
                                Shapes, Stops, StopTimes, Transfers,
                                Trips, Base)
from transitdata.config import TestingConfig

engine = db.create_engine(TestingConfig.SQLALCHEMY_DATABASE_URI, {})


def test_db_tablenames(test_client, init_database):
    table_names = engine.table_names()

    assert table_names == ["agency", "calendar", "calendar_dates", 
                         "frequencies", "routes", "service_alerts", 
                         "shapes", "stop_times", "stops", "transfers", 
                         "trips"]

def test_add_agency(test_client, init_database, new_agency):
    # allow insertion processes to finish
    time.sleep(2)
    query = db.session.query(Agency).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_agency, x.name) for x in new_agency.__table__.columns}

    assert result == data

def test_add_calendar(test_client, init_database, new_calendar):
    time.sleep(2)
    query = db.session.query(Calendar).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_calendar, x.name) for x in new_calendar.__table__.columns}
    
    assert result == data

def test_add_calendar_dates(test_client, init_database, new_calendar_dates):
    time.sleep(2)
    query = db.session.query(CalendarDates).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_calendar_dates, x.name) for x in new_calendar_dates.__table__.columns}
    
    assert result == data

def test_add_frequencies(test_client, init_database, new_frequencies):
    time.sleep(2)
    query = db.session.query(Frequencies).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_frequencies, x.name) for x in new_frequencies.__table__.columns}
    
    assert result == data

def test_add_routes(test_client, init_database, new_routes):
    time.sleep(2)
    query = db.session.query(Routes).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_routes, x.name) for x in new_routes.__table__.columns}
    
    assert result == data

def test_add_service_alerts(test_client, init_database, new_service_alerts):
    time.sleep(2)
    query = db.session.query(ServiceAlerts).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_service_alerts, x.name) for x in new_service_alerts.__table__.columns}
    
    assert result == data

def test_add_shapes(test_client, init_database, new_shapes):
    time.sleep(2)
    query = db.session.query(Shapes).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_shapes, x.name) for x in new_shapes.__table__.columns}
    
    assert result == data

def test_add_stop_times(test_client, init_database, new_stop_times):
    time.sleep(2)
    query = db.session.query(StopTimes).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_stop_times, x.name) for x in new_stop_times.__table__.columns}
    
    assert result == data

def test_add_stops(test_client, init_database, new_stops):
    time.sleep(2)
    query = db.session.query(Stops).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_stops, x.name) for x in new_stops.__table__.columns}
    
    assert result == data

def test_add_transfers(test_client, init_database, new_transfers):
    time.sleep(2)
    query = db.session.query(Transfers).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_transfers, x.name) for x in new_transfers.__table__.columns}
    
    assert result == data

def test_add_trips(test_client, init_database, new_trips):
    time.sleep(2)
    query = db.session.query(Trips).first()
    result = {x.name: getattr(query, x.name) for x in query.__table__.columns}
    data = {x.name: getattr(new_trips, x.name) for x in new_trips.__table__.columns}
    
    assert result == data