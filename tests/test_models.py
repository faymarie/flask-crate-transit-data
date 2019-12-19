import pytest
from datetime import date 
import pandas as pd
import json
from transitdata import db
from transitdata.config import TestingConfig

def test_new_agency(new_agency):

    assert new_agency.agency_id == 84
    assert new_agency.agency_name == "Stadtverkehrsgesellschaft mbH Frankfurt (Oder)"
    assert new_agency.agency_url == "http://www.svf-ffo.de"
    assert new_agency.agency_timezone == "Europe/Berlin"
    assert new_agency.agency_lang == "de"
    assert new_agency.agency_phone == ""
    assert new_agency.id != "a bad id"

def test_new_calendar(new_calendar):

    assert new_calendar.service_id == 2163
    assert new_calendar.monday == 1
    assert new_calendar.tuesday == 1
    assert new_calendar.wednesday == 1
    assert new_calendar.thursday == 1
    assert new_calendar.friday == 1
    assert new_calendar.saturday == 0
    assert new_calendar.sunday == 0
    assert new_calendar.start_date == pd.to_datetime(20191206, format='%Y%m%d')
    assert new_calendar.end_date == pd.to_datetime(20201212, format='%Y%m%d')
    assert new_calendar.id != "a bad id"

def test_new_calendar_dates(new_calendar_dates):

    assert new_calendar_dates.agency_id == 7
    assert new_calendar_dates.date == pd.to_datetime(20191211, format='%Y%m%d')
    assert new_calendar_dates.exception_type == 1
    assert new_calendar_dates.id != "a bad id"

def test_frequencies(new_frequencies):
    
    assert new_frequencies.trip_id == 7
    assert new_frequencies.start_time == pd.to_datetime(date.today())
    assert new_frequencies.end_time == pd.to_datetime(date.today())
    assert new_frequencies.headway_secs == 99999999
    assert new_frequencies.exact_times == 10
    assert new_frequencies.id != "a bad id"

def test_routes(new_routes):

    assert new_routes.route_id == "19058_100"
    assert new_routes.agency_id == 108
    assert new_routes.route_short_name == "RE3"
    assert new_routes.route_long_name == ""
    assert new_routes.route_type == 100
    assert new_routes.route_color == "FF5900"
    assert new_routes.route_text_color == "FFFFFF"
    assert new_routes.route_desc == "Wittenberg/Falkenberg <> Berlin <> Stralsund/Schwedt"
    assert new_routes.id != "a bad id"

def test_service_alerts(new_service_alerts):

    assert new_service_alerts.header ==  json.loads('{"gtfs_realtime_version": "2.0", "incrementality":"DIFFERENTIAL", "timestamp":"1575622745"}')
    assert new_service_alerts.id != "a bad id"

def test_shapes(new_shapes):

    assert new_shapes.shape_id == 9202
    assert new_shapes.shape_pt_lat == 52.430096
    assert new_shapes.shape_pt_lon == 14.042193
    assert new_shapes.shape_pt_sequence == 125
    assert new_shapes.id != "a bad id"

def stops(new_stops):

    assert new_stops.stop_id == "070101000857"
    assert new_stops.stop_code == ""
    assert new_stops.stop_name == "S+U Zoologischer Garten/Jebensstr. (Berlin)"
    assert new_stops.stop_desc == None
    assert new_stops.stop_lat  == 52.507126000000
    assert new_stops.stop_lon == 13.330430000000
    assert new_stops.location_type == 0
    assert new_stops.parent_station == "900000023172"
    assert new_stops.wheelchair_boarding == None
    assert new_stops.platform_code  == ""
    assert new_stops.zone_id  == ""
    assert new_stops.id != "a bad id"

def test_trips(new_trips):

    assert new_trips.route_id == "17291_700"
    assert new_trips.service_id == 250
    assert new_trips.trip_id == 126033488
    assert new_trips.trip_headsign == "Berlin, U Theodor-Heuss-Platz West"
    assert new_trips.trip_short_name  == ""
    assert new_trips.direction_id == 1
    assert new_trips.block_id == None
    assert new_trips.shape_id == 909
    assert new_trips.wheelchair_accessible == 1
    assert new_trips.bikes_allowed  == None
    assert new_trips.id != "a bad id"


def test_stop_times(new_stop_times):

    assert new_stop_times.trip_id == 126050646
    assert new_stop_times.arrival_time == "13:18:00"
    assert new_stop_times.departure_time == "13:18:00"
    assert new_stop_times.stop_id == "070101007005"
    assert new_stop_times.stop_sequence  == 0
    assert new_stop_times.pickup_type == 0
    assert new_stop_times.drop_off_type == 0
    assert new_stop_times.stop_headsign  == "Gatower Str. via S+U Rathaus Spandau"
    assert new_stop_times.id != "a bad id"

def test_transfers(new_transfers):

    assert new_transfers.from_stop_id == "770000105609"
    assert new_transfers.to_stop_id == "770000205609"
    assert new_transfers.transfer_type  == 1
    assert new_transfers.min_transfer_time == None
    assert new_transfers.from_route_id  == None
    assert new_transfers.to_route_id  == None
    assert new_transfers.from_trip_id  == 123511950
    assert new_transfers.to_trip_id  == 123511400
    assert new_transfers.id != "a bad id"