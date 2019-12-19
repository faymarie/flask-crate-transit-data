import pytest
import pandas as pd
import transitdata
from datetime import date
# import json
# import sqlalchemy as sa
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
    context = app.test_request_context().push()
    print("hello")
    db.drop_all()   
    yield testing_client
    context.pop()
        # engine = db.create_engine(config_class.SQLALCHEMY_DATABASE_URI, {})
        # Base.metadata.drop_all(engine)
        # db.drop_all()

@pytest.fixture()
def new_agency():
    agency = Agency(84,"Stadtverkehrsgesellschaft mbH Frankfurt (Oder)",
                        "http://www.svf-ffo.de","Europe/Berlin","de","")
    return agency

@pytest.fixture()
def new_calendar():
    calendar = Calendar(2163, 1, 1, 1, 1, 1, 0, 0, 
                        pd.to_datetime(20191206, format='%Y%m%d'), 
                        pd.to_datetime(20201212, format='%Y%m%d'))
    return calendar

@pytest.fixture()
def new_calendar_dates():
    calendar_dates = CalendarDates(7, pd.to_datetime(20191211, format='%Y%m%d'),1)
    return calendar_dates 

@pytest.fixture()
def new_frequencies():
    frequencies = Frequencies(7, date.today(), date.today(), 
                             999999999999999999999999999999, 
                             10)
    return frequencies

@pytest.fixture()
def new_routes():
    routes = Routes("19058_100", 108, "RE3", "", 100,
                    "FF5900","FFFFFF",
                    "Wittenberg/Falkenberg <> Berlin <> Stralsund/Schwedt")
    return routes

@pytest.fixture()
def new_service_alerts():
    header = {"gtfs_realtime_version": "2.0", 
            "incrementality": "DIFFERENTIAL", 
            "timestamp": "1575622745"}
    service_alert = ServiceAlerts(header)
    return service_alert

@pytest.fixture()
def new_shapes():
    shape = Shapes(9202, 52.430096, 14.042193, 125)
    return shape

@pytest.fixture()
def new_stop_times():
    stop_time = StopTimes(126050646, "13:18:00", "13:18:00", "070101007005", 
                         0, 0, 0, "Gatower Str. via S+U Rathaus Spandau")
    return stop_time

@pytest.fixture()
def new_stops():
    stop = Stop("070101000857", "", 
                "S+U Zoologischer Garten/Jebensstr. (Berlin)",  
                None, 52.507126000000, 13.330430000000, 0, 
                "900000023172", None, "", "")
    return stops

@pytest.fixture()
def new_transfers():
    transfer = Transfers("770000105609", "770000205609", 
                        1, None, None, None, 123511950, 123511400)
    return transfer

@pytest.fixture()
def new_trips():
    trip = Trips("17291_700", 250, 126033488,
                "Berlin, U Theodor-Heuss-Platz West","",
                1, None, 909, 1, None)
    return trip

        # Create the database and the database table
    # db.create_all()

#     # Insert user data
    # user2 = User(email='kennedyfamilyrecipes@gmail.com', plaintext_password='PaSsWoRd')
    # db.session.add(user1)
    # db.session.add(user2)

#     # Commit the changes for the users
#     db.session.commit()

#     yield db  # this is where the testing happens!

#     db.drop_all()



    # db.session.remove()
    # db.drop_all()