from flask import current_app
# from transitdata import Base
from uuid import uuid4
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
# from crate.client.sqlalchemy import types

def gen_key():
    return str(uuid4())

Base = declarative_base()
class Character(Base):
    
    __tablename__ = 'characters'
    id = sa.Column(sa.String, primary_key=True, default=gen_key)
    name = sa.Column(sa.String)
    quote = sa.Column(sa.String)

    #  __mapper_args__ = {
    #      'exclude_properties': ['name_ft', 'quote_ft']
    # }

# Base = declarative_base()

# class Agency(Base):
#     """Model for transport agency"""

#     __tablename__ = 'agency'

#     id = sa.Column(sa.Integer,
#                    primary_key=True, default=gen_key)

#     agency_id = sa.Column (sa.Integer,  # Foreign key
#                          index=False,
#                          unique=True,
#                          nullable=False)
#     agency_name = sa.Column (sa.Integer,
#                          index=False,
#                          unique=True,
#                          nullable=False)
#     agency_url = sa.Column (sa.String,
#                          index=False,
#                          unique=False,
#                          nullable=False)   
#     agency_timezone = sa.Column (sa.String,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     agency_lang = sa.Column (sa.String,
#                          index=False,
#                          unique=False,
#                          nullable=True)
#     agency_phone = sa.Column (sa.String(20),
#                          index=False,
#                          unique=False,
#                          nullable=True)
#     def __repr__(self):
#         return "Agency: {}".format(self.agency_name)


# class Calendar (sa.Model):
#     """Model for transportation calendar"""

#     __tablename__ = 'calendar'
#     service_id = (sa.Column (sa.Integer,   # primary key
#                          primary_key=True)
#     monday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     tuesday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     wednesday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     thursday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     friday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     (saturday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     sunday = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     start_date = (sa.Column (sa.DateTime,   # Start service day for the service interval. Service day in the YYYYMMDD format.
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     end_date = (sa.Column (sa.DateTime,     # End service day for the service interval. This service day is included in the interval.
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     def __repr__(self):
#         return '<Calendar Agency {}>'.format(self.agency_id)

# class CalendarDates (sa.Model):
#     """Model for transportation service exceptions """

#     __tablename__ = 'calendar_dates'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     agency_id = (sa.Column (sa.Integer,   # foreign key to calendar
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     date = (sa.Column (sa.DateTime,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     exception_type = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)

# class Frequencies (sa.Model):
#     """ Model representing trips that operate on regular headways (time between trips). """

#     __tablename__ = 'frequencies'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     tip_id = (sa.Column (sa.Integer,  
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     start_time = (sa.Column (sa.DateTime, # Time at which the first vehicle departs from the first stop of the trip with the specified headwa
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     end_time = (sa.Column (sa.DateTime,  # Time at which service changes to a different headway (or ceases) at the first stop in the trip.
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     headway_secs = (sa.Column (sa.Integer, #Time, in seconds, between departures from the (same stop (headway) for the trip, during the time interval specified by start_time and end_time.
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     exact_times = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=True)

# class Routes (sa.Model):
#     """ Transit routes. A route is a group of trips that are displayed to riders as a single service. """

#     __tablename__ = 'routes'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     route_id = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     agency_id = (sa.Column (sa.Integer,  # foreign key to calendar
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     route_short_name = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     route_long_name = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=True)
#     route_type = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     route_color = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=True)
#     route_text_color = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=True)
#     route_desc = (sa.Column (sa.String,  
#                          index=False,
#                          unique=False,
#                          nullable=True)

# class ServiceAlerts (sa.Model):             # parse from json
#     """ Model for Service Alerts """
    
#     __tablename__ = 'service_alerts'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     gtfs_realtime_version = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     incrementally = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     timestamp = (sa.Column (sa.DateTime,
#                         index=False,
#                         unique=False,
#                         nullable=True)

# class Shapes (sa.Model):
#     """ 
#     Model describing the path that a vehicle travels along a route alignment. 
#     Shapes are associated with Trips, and consist of a sequence of points 
#     through which the vehicle passes in order. Shapes do not need to intercept 
#     the location of Stops exactly, but all Stops on a trip should lie within 
#     a small distance of the shape for that trip, i.e. close to straight line 
#     segments connecting the shape points.
    
#     """
    
#     __tablename__ = 'shapes'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     shape_id = (sa.Column (sa.Integer,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     shape_pt_lat = (sa.Column (sa.Float,
#                     index=False,
#                     unique=False,
#                     nullable=False)
#     shape_pt_lon = (sa.Column (sa.Float,
#                     index=False,
#                     unique=False,
#                     nullable=False)
#     shape_pt_lat = (sa.Column (sa.Integer,
#                     index=False,
#                     unique=False,
#                     nullable=False)

# class Stops (sa.Model):
#     """ Model for stops where vehicles pick up or drop off riders. Also defines stations and station entrances."""
    
#     __tablename__ = 'stops'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     stop_id = (sa.Column (sa.Integer,     
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     stop_code = (sa.Column (sa.Float,     
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     stop_name = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     stop_desc = (sa.Column (sa.Float,     
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     stop_lat = (sa.Column (sa.Float,     
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     stop_lon = (sa.Column (sa.Float,     
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     location_type = (sa.Column (sa.Integer,
#                          index=False,
#                          unique=False,
#                          nullable=False)
#     parent_station = (sa.Column (sa.Float,     # references stops.stops_id
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     wheelchair_boarding = (sa.Column (sa.Float,     
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     platform_code = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     zone_id = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=True)

# class Trips (sa.Model):
#     """ Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period. """
    
#     __tablename__ = 'trips'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     route_id = (sa.Column (sa.String,    # reference routes.route_id 
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     service_id = (sa.Column (sa.Integer,    # reference calendar.service_id or calendar_dates.service_id
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     trip_id = (sa.Column (sa.Integer,     
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     trip_headsign = (sa.Column (sa.String,   
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     trip_short_name = (sa.Column (sa.String,   #should be text, but comes as float?
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     direction_id = (sa.Column (sa.Integer,  
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     block_id = (sa.Column (sa.Integer,     #should be int, but may come as float
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     shape_id = (sa.Column (sa.Integer,     # reference shapes.shape_id 
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     wheelchair_accessible = (sa.Column (sa.Integer,     # should be int but comes as float
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     bikes_allowed = (sa.Column (sa.Integer,      # should be int but comes as float
#                         index=False,
#                         unique=False,
#                         nullable=True)

# class StopTimes (sa.Model):
#     """ Model describing times that a vehicle arrives at and departs from stops for each trip. """
    
#     __tablename__ = 'stop_times'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     trip_id = (sa.Column (sa.Integer,          # references trips.trip_id
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     arrival_time = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     departure_time = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     stop_id = (sa.Column (sa.String,          # references stops.stop_id
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     stop_sequence = (sa.Column (sa.Integer,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     pickup_type = (sa.Column (sa.Integer,
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     drop_off_type = (sa.Column (sa.Integer,
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     stop_headsign = (sa.Column (sa.String,
#                         index=False,
#                         unique=False,
#                         nullable=True)

# class Transfers (sa.Model):
#     """ Model refering to rules for making connections at transfer points between routes. """
    
#     __tablename__ = 'transfers'
#     id = (sa.Column (sa.Integer,
#                    primary_key=True)
#     from_stop_id = (sa.Column (sa.String,          # references stops.stop_id
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     to_stop_id = (sa.Column (sa.String,          # references stops.stop_id
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     transfer_type = (sa.Column (sa.Integer,
#                         index=False,
#                         unique=False,
#                         nullable=False)
#     min_transfer_time = (sa.Column (sa.Integer,   # Int or Float unclear !!!
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     from_route_id = (sa.Column (sa.String,          # references route.route_id
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     to_route_id = (sa.Column (sa.String,            # references route.route_id
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     from_trip_id = (sa.Column (sa.Integer,     # Int or Float unclear, references trips??? !!!
#                         index=False,
#                         unique=False,
#                         nullable=True)
#     to_trip_id = (sa.Column (sa.Integer,    # Int or Float unclear, references trips??? !!!
#                         index=False,
#                         unique=False,
#                         nullable=True)