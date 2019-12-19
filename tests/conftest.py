import pytest
import pandas as pd
import transitdata
from sqlalchemy.orm import sessionmaker
from datetime import date
from transitdata.models import (Agency, Calendar, CalendarDates, 
                                Frequencies, Routes, ServiceAlerts,
                                Shapes, Stops, StopTimes, Transfers,
                                Trips)
from transitdata import create_app, db
from transitdata.config import TestingConfig
from transitdata.models import Base


@pytest.fixture
def test_client():
    app = create_app(config_class=TestingConfig)
    testing_client = app.test_client()
    context = app.test_request_context()
    context.push()

    yield testing_client
    
    # context.pop()

test_data = []

@pytest.fixture(scope="module")
def new_agency():
    agency = Agency(84,"Stadtverkehrsgesellschaft mbH Frankfurt (Oder)",
                        "http://www.svf-ffo.de","Europe/Berlin","de", None)
    test_data.append(agency)
    return agency

@pytest.fixture(scope="module")
def new_calendar():
    calendar = Calendar(2163, 1, 1, 1, 1, 1, 0, 0, 
                        pd.to_datetime(20191206, format='%Y%m%d'), 
                        pd.to_datetime(20201212, format='%Y%m%d'))
    test_data.append(calendar)

    return calendar

@pytest.fixture(scope="module")
def new_calendar_dates():
    calendar_dates = CalendarDates(7, pd.to_datetime(20191211, 
                                        format='%Y%m%d'), 1)
    test_data.append(calendar_dates)

    return calendar_dates 

@pytest.fixture(scope="module")
def new_frequencies():
    frequencies = Frequencies(7, pd.to_datetime(date.today()), 
                            pd.to_datetime(date.today()), 
                            99999999, 10)
    test_data.append(frequencies)

    return frequencies

@pytest.fixture(scope="module")
def new_routes():
    routes = Routes("19058_100", 108, "RE3", "", 100,
                    "FF5900","FFFFFF",
                    "Wittenberg/Falkenberg <> Berlin <> Stralsund/Schwedt")
    test_data.append(routes)

    return routes

@pytest.fixture(scope="module")
def new_service_alerts():
    header = {"gtfs_realtime_version": "2.0", 
            "incrementality": "DIFFERENTIAL", 
            "timestamp": "1575622745"}
    service_alert = ServiceAlerts(header)
    test_data.append(service_alert)

    return service_alert

@pytest.fixture(scope="module")
def new_shapes():
    shape = Shapes(9202, 52.430096, 14.042193, 125)
    test_data.append(shape)

    return shape

@pytest.fixture(scope="module")
def new_stop_times():
    stop_time = StopTimes(126050646, "13:18:00", "13:18:00", "070101007005", 
                         0, 0, 0, "Gatower Str. via S+U Rathaus Spandau")
    test_data.append(stop_time)

    return stop_time

@pytest.fixture(scope="module")
def new_stops():
    stop = Stops("070101000857", "", 
                "S+U Zoologischer Garten/Jebensstr. (Berlin)",  
                None, 52.507126000000, 13.330430000000, 0, 
                "900000023172", None, "", "")
    test_data.append(stop)

    return stop

@pytest.fixture(scope="module")
def new_transfers():
    transfer = Transfers("770000105609", "770000205609", 
                        1, None, None, None, 123511950, 123511400)
    test_data.append(transfer)

    return transfer

@pytest.fixture(scope="module")
def new_trips():
    trip = Trips("17291_700", 250, 126033488,
                "Berlin, U Theodor-Heuss-Platz West","",
                1, None, 909, 1, None)
    test_data.append(trip)

    return trip

def create_records():
    agency = Agency(84,"Stadtverkehrsgesellschaft mbH Frankfurt (Oder)",
                    "http://www.svf-ffo.de","Europe/Berlin","de","")

    calendar =  Calendar(2163, 1, 1, 1, 1, 1, 0, 0, 
                        pd.to_datetime(20191206, format='%Y%m%d'), 
                        pd.to_datetime(20201212, format='%Y%m%d'))

    calendar_dates = CalendarDates(7, pd.to_datetime(20191211, 
                                    format='%Y%m%d'), 1)
                                    
    frequencies = Frequencies(7, pd.to_datetime(date.today()), 
                            pd.to_datetime(date.today()), 
                            99999999, 10)

    routes = Routes("19058_100", 108, "RE3", "", 100,
                    "FF5900","FFFFFF",
                    "Wittenberg/Falkenberg <> Berlin <> Stralsund/Schwedt")

    header = {"gtfs_realtime_version": "2.0", 
            "incrementality": "DIFFERENTIAL", 
            "timestamp": "1575622745"}
    service_alert = ServiceAlerts(header)

    shape = Shapes(9202, 52.430096, 14.042193, 125)

    stop_time = StopTimes(126050646, "13:18:00", "13:18:00", "070101007005", 
                        0, 0, 0, "Gatower Str. via S+U Rathaus Spandau")

    stop = Stops("070101000857", "", 
                "S+U Zoologischer Garten/Jebensstr. (Berlin)",  
                None, 52.507126000000, 13.330430000000, 0, 
                "900000023172", None, "", "")

    transfer = Transfers("770000105609", "770000205609", 
                        1, None, None, None, 123511950, 123511400)

    trip = Trips("17291_700", 250, 126033488,
                "Berlin, U Theodor-Heuss-Platz West","",
                1, None, 909, 1, None)

    return [agency, calendar, calendar_dates, frequencies, routes, service_alert, 
            shape, stop_time, stop, transfer, trip]

@pytest.fixture
def init_database():

    engine = db.create_engine(TestingConfig.SQLALCHEMY_DATABASE_URI, {})

    # flush database, then create tables and add fixtures
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    db.session.add_all(test_data)
    db.session.commit()

    yield db

    # db.session.remove()
    # Base.metadata.drop_all(engine)