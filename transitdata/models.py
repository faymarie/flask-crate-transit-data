from flask import current_app
from transitdata import db
from uuid import uuid4

def gen_key():
    return str(uuid4())

# Base = declarative.declarative_base(bind=engine)

class Agency(db.Model):
    """Model for transport agency"""

    __tablename__ = 'agency'

    id = db.Column(db.Integer,
                   primary_key=True)
    agency_id = db.Column(db.Integer,  # Foreign key
                         index=False,
                         unique=True,
                         nullable=False)
    agency_name = db.Column(db.Integer,
                         index=False,
                         unique=True,
                         nullable=False)
    agency_url = db.Column(db.String,
                         index=False,
                         unique=False,
                         nullable=False)   
    agency_timezone = db.Column(db.String,
                         index=False,
                         unique=False,
                         nullable=False)
    agency_lang = db.Column(db.String,
                         index=False,
                         unique=False,
                         nullable=True)
    agency_phone = db.Column(db.String(20),
                         index=False,
                         unique=False,
                         nullable=True)
    def __repr__(self):
        return '<Agency {}>'.format(self.agency_name)


class Calendar(db.Model):
    """Model for transportation calendar"""

    __tablename__ = 'calendar'
    service_id = db.Column(db.Integer,   # primary key
                         primary_key=True)
    monday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    tuesday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    wednesday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    thursday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    friday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    saturday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    sunday = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    start_date = db.Column(db.DateTime,   # Start service day for the service interval. Service day in the YYYYMMDD format.
                         index=False,
                         unique=False,
                         nullable=False)
    end_date = db.Column(db.DateTime,     # End service day for the service interval. This service day is included in the interval.
                         index=False,
                         unique=False,
                         nullable=False)
    def __repr__(self):
        return '<Calendar Agency {}>'.format(self.agency_id)

class CalendarDates(db.Model):
    """Model for transportation service exceptions """

    __tablename__ = 'calendar_dates'
    id = db.Column(db.Integer,
                   primary_key=True)
    agency_id = db.Column(db.Integer,   # foreign key to calendar
                         index=False,
                         unique=False,
                         nullable=False)
    date = db.Column(db.DateTime,
                         index=False,
                         unique=False,
                         nullable=False)
    exception_type = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)

class Frequencies(db.Model):
    """ Model representing trips that operate on regular headways (time between trips). """

    __tablename__ = 'frequencies'
    id = db.Column(db.Integer,
                   primary_key=True)
    tip_id = db.Column(db.Integer,  
                         index=False,
                         unique=False,
                         nullable=False)
    start_time = db.Column(db.DateTime, # Time at which the first vehicle departs from the first stop of the trip with the specified headwa
                         index=False,
                         unique=False,
                         nullable=False)
    end_time = db.Column(db.DateTime,  # Time at which service changes to a different headway (or ceases) at the first stop in the trip.
                         index=False,
                         unique=False,
                         nullable=False)
    headway_secs = db.Column(db.Integer, #Time, in seconds, between departures from the same stop (headway) for the trip, during the time interval specified by start_time and end_time.
                         index=False,
                         unique=False,
                         nullable=False)
    exact_times = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=True)

class Routes(db.Model):
    """ Transit routes. A route is a group of trips that are displayed to riders as a single service. """

    __tablename__ = 'routes'
    id = db.Column(db.Integer,
                   primary_key=True)
    route_id = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=False)
    agency_id = db.Column(db.Integer,  # foreign key to calendar
                         index=False,
                         unique=False,
                         nullable=False)
    route_short_name = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=False)
    route_long_name = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=True)
    route_type = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    route_color = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=True)
    route_text_color = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=True)
    route_desc = db.Column(db.String,  
                         index=False,
                         unique=False,
                         nullable=True)

class ServiceAlerts(db.Model):             # parse from json
    """ Model for Service Alerts """
    
    __tablename__ = 'service_alerts'
    id = db.Column(db.Integer,
                   primary_key=True)
    gtfs_realtime_version = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=True)
    incrementally = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=True)
    timestamp = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=True)

class Shapes(db.Model):
    """ 
    Model describing the path that a vehicle travels along a route alignment. 
    Shapes are associated with Trips, and consist of a sequence of points 
    through which the vehicle passes in order. Shapes do not need to intercept 
    the location of Stops exactly, but all Stops on a trip should lie within 
    a small distance of the shape for that trip, i.e. close to straight line 
    segments connecting the shape points.
    
    """
    
    __tablename__ = 'shapes'
    id = db.Column(db.Integer,
                   primary_key=True)
    shape_id = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    shape_pt_lat = db.Column(db.Float,
                    index=False,
                    unique=False,
                    nullable=False)
    shape_pt_lon = db.Column(db.Float,
                    index=False,
                    unique=False,
                    nullable=False)
    shape_pt_lat = db.Column(db.Integer,
                    index=False,
                    unique=False,
                    nullable=False)

class Stops(db.Model):
    """ Model for stops where vehicles pick up or drop off riders. Also defines stations and station entrances."""
    
    __tablename__ = 'stops'
    id = db.Column(db.Integer,
                   primary_key=True)
    stop_id = db.Column(db.Integer,     
                        index=False,
                        unique=False,
                        nullable=False)
    stop_code = db.Column(db.Float,     
                        index=False,
                        unique=False,
                        nullable=True)
    stop_name = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=False)
    stop_desc = db.Column(db.Float,     
                        index=False,
                        unique=False,
                        nullable=True)
    stop_lat = db.Column(db.Float,     
                        index=False,
                        unique=False,
                        nullable=False)
    stop_lon = db.Column(db.Float,     
                        index=False,
                        unique=False,
                        nullable=False)
    location_type = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    parent_station = db.Column(db.Float,     # references stops.stops_id
                        index=False,
                        unique=False,
                        nullable=True)
    wheelchair_boarding = db.Column(db.Float,     
                        index=False,
                        unique=False,
                        nullable=True)
    platform_code = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=True)
    zone_id = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=True)

class Trips(db.Model):
    """ Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period. """
    
    __tablename__ = 'trips'
    id = db.Column(db.Integer,
                   primary_key=True)
    route_id = db.Column(db.String,    # reference routes.route_id 
                        index=False,
                        unique=False,
                        nullable=False)
    service_id = db.Column(db.Integer,    # reference calendar.service_id or calendar_dates.service_id
                        index=False,
                        unique=False,
                        nullable=False)
    trip_id = db.Column(db.Integer,     
                        index=False,
                        unique=False,
                        nullable=False)
    trip_headsign = db.Column(db.String,   
                        index=False,
                        unique=False,
                        nullable=True)
    trip_short_name = db.Column(db.String,   #should be text, but comes as float?
                        index=False,
                        unique=False,
                        nullable=True)
    direction_id = db.Column(db.Integer,  
                        index=False,
                        unique=False,
                        nullable=True)
    block_id = db.Column(db.Integer,     #should be int, but may come as float
                        index=False,
                        unique=False,
                        nullable=True)
    shape_id = db.Column(db.Integer,     # reference shapes.shape_id 
                        index=False,
                        unique=False,
                        nullable=True)
    wheelchair_accessible = db.Column(db.Integer,     # should be int but comes as float
                        index=False,
                        unique=False,
                        nullable=True)
    bikes_allowed = db.Column(db.Integer,      # should be int but comes as float
                        index=False,
                        unique=False,
                        nullable=True)

class StopTimes(db.Model):
    """ Model describing times that a vehicle arrives at and departs from stops for each trip. """
    
    __tablename__ = 'stop_times'
    id = db.Column(db.Integer,
                   primary_key=True)
    trip_id = db.Column(db.Integer,          # references trips.trip_id
                        index=False,
                        unique=False,
                        nullable=False)
    arrival_time = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=False)
    departure_time = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=False)
    stop_id = db.Column(db.String,          # references stops.stop_id
                        index=False,
                        unique=False,
                        nullable=False)
    stop_sequence = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    pickup_type = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=True)
    drop_off_type = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=True)
    stop_headsign = db.Column(db.String,
                        index=False,
                        unique=False,
                        nullable=True)

class Transfers(db.Model):
    """ Model refering to rules for making connections at transfer points between routes. """
    
    __tablename__ = 'transfers'
    id = db.Column(db.Integer,
                   primary_key=True)
    from_stop_id = db.Column(db.String,          # references stops.stop_id
                        index=False,
                        unique=False,
                        nullable=False)
    to_stop_id = db.Column(db.String,          # references stops.stop_id
                        index=False,
                        unique=False,
                        nullable=False)
    transfer_type = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    min_transfer_time = db.Column(db.Integer,   # Int or Float unclear !!!
                        index=False,
                        unique=False,
                        nullable=True)
    from_route_id = db.Column(db.String,          # references route.route_id
                        index=False,
                        unique=False,
                        nullable=True)
    to_route_id = db.Column(db.String,            # references route.route_id
                        index=False,
                        unique=False,
                        nullable=True)
    from_trip_id = db.Column(db.Integer,     # Int or Float unclear, references trips??? !!!
                        index=False,
                        unique=False,
                        nullable=True)
    to_trip_id = db.Column(db.Integer,    # Int or Float unclear, references trips??? !!!
                        index=False,
                        unique=False,
                        nullable=True)

# class Tile(Base):
#     __tablename__ = 'example'
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column('data', db.Unicode)

# # __mapper_args__ = {
# ...         'exclude_properties': ['name_ft', 'quote_ft']
    # def __init__(self, data):
    #     self.data = data
#     def __repr__(self):
#         pass