from flask import current_app
from uuid import uuid4
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from crate.client.sqlalchemy import types

Base = declarative_base()

def gen_key():
    return str(uuid4())

class Agency(Base):
    """ Model for transit agencies with service represented in this dataset. """

    __tablename__ = 'agency'

    id = db.Column(db.String, primary_key=True, default=gen_key)
    agency_id = db.Column (db.Integer, nullable=False)
    agency_name = db.Column (db.String, nullable=False)
    agency_url = db.Column (db.String, nullable=False)  
    agency_timezone = db.Column (db.String, nullable=False)
    agency_lang = db.Column (db.String, nullable=True)
    agency_phone = db.Column (db.String, nullable=True)

    def __repr__(self):
        return "<Agency: {}>".format(self.agency_name)

    def __init__(self, agency_id, agency_name, agency_url,
                agency_timezone, agency_lang, agency_phone):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = agency_lang
        self.agency_phone = agency_phone

class Calendar (Base):
    """ Model for service dates specified using a weekly schedule with start and end dates."""

    __tablename__ = 'calendar'

    id = db.Column(db.String, primary_key=True, default=gen_key)
    service_id = db.Column (db.Integer, nullable=False)
    monday = db.Column (db.Integer, nullable=False)
    tuesday = db.Column (db.Integer, nullable=False)
    wednesday = db.Column (db.Integer, nullable=False)
    thursday = db.Column (db.Integer, nullable=False)
    friday = db.Column (db.Integer, nullable=False)
    saturday = db.Column (db.Integer, nullable=False)
    sunday = db.Column (db.Integer, nullable=False)
    start_date = db.Column (db.DateTime(timezone=False), nullable=False)
    end_date = db.Column (db.DateTime(timezone=False), nullable=False)
    
    def __repr__(self):
        return '<Calendar Service Id {}>'.format(self.service_id)

    def __init__(self, service_id, monday, tuesday, wednesday, thursday,
                friday, saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = monday
        self.tuesday= tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date
    
class CalendarDates (Base):
    """ Model for transportation service exceptions """

    __tablename__ = 'calendar_dates'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    agency_id = db.Column (db.Integer, nullable=False)
    date = db.Column (db.DateTime(timezone=False), nullable=False)
    exception_type = db.Column (db.Integer, nullable=False)

    def __repr__(self):
        return '<Service exceptions {} Date: {}>'.format(self.agency_id, self.date)

    def __init__(self, agency_id, date, exception_type):
        self.agency_id = agency_id
        self.date = date
        self.exception_type = exception_type

class Frequencies (Base):
    """ Model representing trips that operate on regular headways (time between trips). """

    __tablename__ = 'frequencies'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    trip_id = db.Column (db.Integer, nullable=False)
    start_time = db.Column (db.DateTime(timezone=False), nullable=False) 
    end_time = db.Column (db.DateTime (timezone=False), nullable=False)
    headway_secs = db.Column (db.Integer, nullable=False)
    exact_times = db.Column (db.Integer, nullable=True)

    def __repr__(self):
        return '<Transport frequencies {} Date: {}>'.format(self.trip_id, self.start_time)

    def __init__(self, trip_id, start_time, end_time, headway_secs, exact_times):
        self.trip_id = trip_id
        self.start_time = start_time
        self.end_time = end_time
        self.headway_secs = headway_secs 
        self.exact_times = exact_times

class Routes (Base):
    """ 
    Model for Transit routes. A route is a group of trips 
    that are displayed to riders as a single service. 
    
    """

    __tablename__ = 'routes'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    route_id = db.Column (db.String, nullable=False)
    agency_id = db.Column (db.Integer, nullable=False)   
    route_short_name = db.Column (db.String, nullable=False)
    route_long_name = db.Column (db.String, nullable=True)
    route_type = db.Column (db.Integer, nullable=False)
    route_color = db.Column (db.String, nullable=True)
    route_text_color = db.Column (db.String, nullable=True)
    route_desc = db.Column (db.String, nullable=True)

    def __repr__(self):
        return '<Route id: {}, short name: {}>'.format(self.route_id, self.route_short_name)

    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_type,
                route_color, route_text_color, route_desc):
        self.route_id = route_id
        self.agency_id = agency_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.route_type = route_type
        self.route_color = route_color
        self.route_text_color = route_text_color
        self.route_desc = route_desc

class ServiceAlerts (Base):
    """ Model for Service Alerts """
    
    __tablename__ = 'service_alerts'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    header = db.Column(types.Object)

    def __init__(self, header):
        self.header = header

class Shapes (Base):
    """ 
    Model describing the path that a vehicle travels along a route alignment. 
    Shapes are associated with Trips, and consist of a sequence of points 
    through which the vehicle passes in order.
    
    """
    
    __tablename__ = 'shapes'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    shape_id = db.Column (db.Integer, nullable=False)
    shape_pt_lat = db.Column (db.Float, nullable=False)
    shape_pt_lon = db.Column (db.Float, nullable=False)
    shape_pt_sequence = db.Column (db.Integer, nullable=False)

    def __repr__(self):
        return '<Travel shape {} lat: {} lon: >'.format(self.shape_id, \
            self.shape_pt_lat, self.shape_pt_lon)

    def __init__(self, shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence):
            self.shape_id = shape_id
            self.shape_pt_lat = shape_pt_lat
            self.shape_pt_lon = shape_pt_lon
            self.shape_pt_sequence = shape_pt_sequence

class Stops (Base):
    """ 
    Model for stops where vehicles pick up or drop off riders. 
    Also defines stations and station entrances.
    
    """
    
    __tablename__ = 'stops'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    stop_id = db.Column (db.String, nullable=False)
    stop_code = db.Column (db.String, nullable=True)
    stop_name = db.Column (db.String, nullable=False)
    stop_desc = db.Column (db.Float, nullable=True)
    stop_lat = db.Column (db.Float, nullable=False)
    stop_lon = db.Column (db.Float, nullable=False)
    location_type = db.Column (db.Integer, nullable=False)
    parent_station = db.Column (db.Float, nullable=True)
    wheelchair_boarding = db.Column (db.Float, nullable=True)
    platform_code = db.Column (db.String, nullable=True)
    zone_id = db.Column (db.String, nullable=True)

    def __repr__(self):
        return '<Transport stops {} {}>'.format(self.stop_id,self.stop_name)

    def __init__(self, stop_id, stop_code, stop_name, stop_desc, 
                stop_lat, stop_lon , location_type, parent_station, wheelchair_boarding,
                platform_code, zone_id):
            self.stop_id = stop_id
            self.stop_code = stop_code
            self.stop_name = stop_name
            self.stop_desc = stop_desc
            self.stop_lat = stop_lat
            self.stop_lon = stop_lon
            self.location_type = location_type
            self.parent_station = parent_station
            self.wheelchair_boarding = wheelchair_boarding
            self.platform_code= platform_code
            self.zone_id = zone_id    

class Trips (Base):
    """ 
    Trips for each route. A trip is a sequence of 
    two or more stops that occur during a specific time period. 
    
    """ 
    
    __tablename__ = 'trips'
    
    id = db.Column (db.String, primary_key=True, default=gen_key)
    route_id = db.Column (db.String, nullable=False)          
    service_id = db.Column (db.Integer, nullable=False)
    trip_id = db.Column (db.Integer, nullable=False)          
    trip_headsign = db.Column (db.String, nullable=True)   
    trip_short_name = db.Column (db.String, nullable=True)        
    direction_id = db.Column (db.Integer, nullable=True) 
    block_id = db.Column (db.Integer, nullable=True)               
    shape_id = db.Column (db.Integer, nullable=True)           
    wheelchair_accessible = db.Column (db.Integer, nullable=True)
    bikes_allowed = db.Column (db.Integer, nullable=True)
 
    def __repr__(self):
        return '<Trips {} {}>'.format(self.trip_id, self.trip_headsign)

    def __init__(self, route_id, service_id, trip_id, trip_headsign,
                trip_short_name, direction_id, block_id, shape_id, wheelchair_accessible,
                bikes_allowed):
            self.route_id = route_id
            self.service_id = service_id
            self.trip_id = trip_id
            self.trip_headsign = trip_headsign
            self.trip_short_name = trip_short_name
            self.direction_id = direction_id
            self.block_id = block_id
            self.shape_id = shape_id            
            self.wheelchair_accessible = wheelchair_accessible
            self.bikes_allowed = bikes_allowed  

class StopTimes (Base):
    """ 
    Model describing times that a vehicle arrives 
    at and departs from stops for each trip. 
    
    """
    
    __tablename__ = 'stop_times'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    trip_id = db.Column (db.Integer, nullable=False)     
    arrival_time = db.Column (db.String, nullable=False)
    departure_time = db.Column (db.String, nullable=False)
    stop_id = db.Column (db.String, nullable=False) 
    stop_sequence = db.Column (db.Integer, nullable=False)
    pickup_type = db.Column (db.Integer, nullable=True)
    drop_off_type = db.Column (db.Integer, nullable=True)
    stop_headsign = db.Column (db.String, nullable=True)
 
    def __repr__(self):
        return '<Stop Times {} {}>'.format(self.stop_id, self.arrival_time)
    
    def __init__(self, trip_id, arrival_time, departure_time, stop_id, stop_sequence, 
                pickup_type,  drop_off_type, stop_headsign):
            self.trip_id = trip_id
            self.arrival_time = arrival_time
            self.departure_time = departure_time
            self.stop_id = stop_id
            self.stop_sequence = stop_sequence
            self.pickup_type = pickup_type
            self.drop_off_type = drop_off_type
            self.stop_headsign = stop_headsign

class Transfers (Base):
    """ 
    Model refering to rules for making connections at 
    transfer points between routes. 
    
    """
    
    __tablename__ = 'transfers'

    id = db.Column (db.String, primary_key=True, default=gen_key)
    from_stop_id = db.Column (db.String, nullable=False)
    to_stop_id = db.Column (db.String, nullable=False)
    transfer_type = db.Column (db.Integer, nullable=False)
    min_transfer_time = db.Column (db.Integer, nullable=True)   
    from_route_id = db.Column (db.String, nullable=True)
    to_route_id = db.Column (db.String, nullable=True) 
    from_trip_id = db.Column (db.Integer, nullable=True)
    to_trip_id = db.Column (db.Integer, nullable=True)
    
    def __repr__(self):
        return '<Transfers {} {}>'.format(self.from_stop_id, self.to_stop_id)
    
    def __init__(self, from_stop_id, to_stop_id, transfer_type, min_transfer_time,
                from_route_id, to_route_id, from_trip_id, to_trip_id):
            self.from_stop_id = from_stop_id
            self.to_stop_id = to_stop_id
            self.transfer_type = transfer_type
            self.min_transfer_time, = min_transfer_time,
            self.from_route_id = from_route_id
            self.to_route_id = to_route_id
            self.from_trip_id = from_trip_id
            self.to_trip_id = to_trip_id