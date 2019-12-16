from flask import current_app
# from transitdata import Base
from uuid import uuid4
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
# from crate.client.sqlalchemy import types

def gen_key():
    return str(uuid4())

Base = declarative_base()
# class Character(Base):
    
#     __tablename__ = 'characters'
#     id = sa.Column(sa.String, primary_key=True, default=gen_key)
#     name = sa.Column(sa.String)
#     quote = sa.Column(sa.String)

    #  __mapper_args__ = {
    #      'exclude_properties': ['name_ft', 'quote_ft']
    # }

# Base = declarative_base()

class Agency(Base):
    """ Model for transit agencies with service represented in this dataset. """

    __tablename__ = 'agency'

    id = sa.Column(sa.Integer, primary_key=True, default=gen_key)
    agency_id = sa.Column (sa.Integer, nullable=False)  # Foreign key
    agency_name = sa.Column (sa.Integer, nullable=False)
    agency_url = sa.Column (sa.String, nullable=False)  
    agency_timezone = sa.Column (sa.String, nullable=False)
    agency_lang = sa.Column (sa.String, nullable=True)
    agency_phone = sa.Column (sa.String, nullable=True)

    def __repr__(self):
        return "<Agency: {}>".format(self.agency_name)


class Calendar (Base):
    """ Model for service dates specified using a weekly schedule with start and end dates."""

    __tablename__ = 'calendar'

    service_id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    monday = sa.Column (sa.Integer, nullable=False)
    tuesday = sa.Column (sa.Integer, nullable=False)
    wednesday = sa.Column (sa.Integer, nullable=False)
    thursday = sa.Column (sa.Integer, nullable=False)
    friday = sa.Column (sa.Integer, nullable=False)
    saturday = sa.Column (sa.Integer, nullable=False)
    sunday = sa.Column (sa.Integer, nullable=False)
    start_date = sa.Column (sa.DateTime, nullable=False)   # Start service day for the service interval. Service day in the YYYYMMDD format.
    end_date = sa.Column (sa.DateTime, nullable=False)    # End service day for the service interval. This service day is included in the interval.
    
    def __repr__(self):
        return '<Calendar Service Id {}>'.format(self.agency_id)

class CalendarDates (Base):
    """ Model for transportation service exceptions """

    __tablename__ = 'calendar_dates'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    agency_id = sa.Column (sa.Integer, nullable=False)             # foreign key to calendar      
    date = sa.Column (sa.DateTime(timezone=False), nullable=False)
    exception_type = sa.Column (sa.Integer, nullable=False)

    def __repr__(self):
        return '<Service exceptions {} Date: {}>'.format(self.agency_id, self.date)

class Frequencies (Base):
    """ Model representing trips that operate on regular headways (time between trips). """

    __tablename__ = 'frequencies'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    trip_id = sa.Column (sa.Integer, nullable=False)
    start_time = sa.Column (sa.DateTime(timezone=False), nullable=False) # Time at which the first vehicle departs from the first stop of the trip with the specified headwa               
    end_time = sa.Column (sa.DateTime (timezone=False), nullable=False)  # Time at which service changes to a different headway (or ceases) at the first stop in the trip.
    headway_secs = sa.Column (sa.Integer, nullable=False) #Time, in seconds, between departures from the (same stop (headway) for the trip, during the time interval specified by start_time and end_time.
    exact_times = sa.Column (sa.Integer, nullable=True)

    def __repr__(self):
        return '<Transport frequencies {} Date: {}>'.format(self.trip_id, self.headway_secs)

class Routes (Base):
    """ 
    Model for Transit routes. A route is a group of trips 
    that are displayed to riders as a single service. 
    
    """

    __tablename__ = 'routes'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    route_id = sa.Column (sa.String, nullable=False)
    agency_id = sa.Column (sa.Integer, nullable=False)  # foreign key to calendar    
    route_short_name = sa.Column (sa.String, nullable=False)
    route_long_name = sa.Column (sa.String, nullable=True)
    route_type = sa.Column (sa.Integer, nullable=False)
    route_color = sa.Column (sa.String, nullable=True)
    route_text_color = sa.Column (sa.String, nullable=True)
    route_desc = sa.Column (sa.String, nullable=True)

    def __repr__(self):
        return '<Route id: {}, short name: {}>'.format(self.route_id, self.route_short_name)

class ServiceAlerts (Base):             # parse from json
    """ Model for Service Alerts """
    
    __tablename__ = 'service_alerts'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    gtfs_realtime_version = sa.Column (sa.String, nullable=True)
    incrementally = sa.Column (sa.String, nullable=True)
    timestamp = sa.Column (sa.DateTime, nullable=True)

    def __repr__(self):
        return '<Service Alerts {} {}>'.format(self.id, self.timestamp)

class Shapes (Base):
    """ 
    Model describing the path that a vehicle travels along a route alignment. 
    Shapes are associated with Trips, and consist of a sequence of points 
    through which the vehicle passes in order. Shapes do not need to intercept 
    the location of Stops exactly, but all Stops on a trip should lie within 
    a small distance of the shape for that trip, i.e. close to straight line 
    segments connecting the shape points.
    
    """
    
    __tablename__ = 'shapes'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    shape_id = sa.Column (sa.Integer, nullable=False)
    shape_pt_lat = sa.Column (sa.Float, nullable=False)
    shape_pt_lon = sa.Column (sa.Float, nullable=False)
    shape_pt_lat = sa.Column (sa.Integer, nullable=False)

    def __repr__(self):
        return '<Travel shape {} lat: {} lon: >'.format(self.shape_id, \
            self.shape_pt_lat, self.shape_pt_lon)

class Stops (Base):
    """ 
    Model for stops where vehicles pick up or drop off riders. 
    Also defines stations and station entrances.
    
    """
    
    __tablename__ = 'stops'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    stop_id = sa.Column (sa.Integer, nullable=False)
    stop_code = sa.Column (sa.Float, nullable=True)
    stop_name = sa.Column (sa.String, nullable=False)
    stop_desc = sa.Column (sa.Float, nullable=True)
    stop_lat = sa.Column (sa.Float, nullable=False)
    stop_lon = sa.Column (sa.Float, nullable=False)
    location_type = sa.Column (sa.Integer, nullable=False)
    parent_station = sa.Column (sa.Float, nullable=True)    # references stops.stops_id
    wheelchair_boarding = sa.Column (sa.Float, nullable=True)
    platform_code = sa.Column (sa.String, nullable=True)
    zone_id = sa.Column (sa.String, nullable=True)

    def __repr__(self):
        return '<Transport stops {} {}>'.format(self.stop_id,self.stop_name)

class Trips (Base):
    """ 
    Trips for each route. A trip is a sequence of 
    two or more stops that occur during a specific time period. 
    
    """ 
    
    __tablename__ = 'trips'
    
    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    route_id = sa.Column (sa.String, nullable=False)    # reference routes.route_id               
    service_id = sa.Column (sa.Integer, nullable=False)   # reference calendar.service_id or calendar_dates.service_id    
    trip_id = sa.Column (sa.Integer, nullable=False)          
    trip_headsign = sa.Column (sa.String, nullable=True)   
    trip_short_name = sa.Column (sa.String, nullable=True)   #should be text, but comes as float?            
    direction_id = sa.Column (sa.Integer, nullable=True) 
    block_id = sa.Column (sa.Integer, nullable=True)     #should be int, but may come as float                
    shape_id = sa.Column (sa.Integer, nullable=True)     # reference shapes.shape_id             
    wheelchair_accessible = sa.Column (sa.Integer, nullable=True)    # should be int but comes as float  
    bikes_allowed = sa.Column (sa.Integer, nullable=True)     # should be int but comes as float
 
    def __repr__(self):
        return '<Trips {} {}>'.format(self.trip_id, self.trip_headsign)
                
                        
class StopTimes (Base):
    """ 
    Model describing times that a vehicle arrives 
    at and departs from stops for each trip. 
    
    """
    
    __tablename__ = 'stop_times'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    trip_id = sa.Column (sa.Integer, nullable=False)         # references trips.trip_id        
    arrival_time = sa.Column (sa.String, nullable=False)
    departure_time = sa.Column (sa.String, nullable=False)
    stop_id = sa.Column (sa.String, nullable=False)         # references stops.stop_id
    stop_sequence = sa.Column (sa.Integer, nullable=False)
    pickup_type = sa.Column (sa.Integer, nullable=True)
    drop_off_type = sa.Column (sa.Integer, nullable=True)
    stop_headsign = sa.Column (sa.String, nullable=True)
 
    def __repr__(self):
        return '<Stop Times {} {}>'.format(self.stop_id, self.arrival_time)

class Transfers (Base):
    """ 
    Model refering to rules for making connections at 
    transfer points between routes. 
    
    """
    
    __tablename__ = 'transfers'

    id = sa.Column (sa.Integer, primary_key=True, default=gen_key)
    from_stop_id = sa.Column (sa.String, nullable=False)        # references stops.stop_id
    to_stop_id = sa.Column (sa.String, nullable=False)          # references stops.stop_id
    transfer_type = sa.Column (sa.Integer, nullable=False)
    min_transfer_time = sa.Column (sa.Integer, nullable=True)   # Int or Float unclear !!!   
    from_route_id = sa.Column (sa.String, nullable=True)        # references route.route_id
    to_route_id = sa.Column (sa.String, nullable=True)            # references route.route_id     
    from_trip_id = sa.Column (sa.Integer, nullable=True)     # Int or Float unclear, references trips??? !!!
    to_trip_id = sa.Column (sa.Integer, nullable=True)    # Int or Float unclear, references trips??? !!!
    
    def __repr__(self):
        return '<Transfers {} {}>'.format(self.from_stop_id, self.to_stop_id)