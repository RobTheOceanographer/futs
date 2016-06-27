from pyorbital.orbital import Orbital
from datetime import datetime
import futs

def time_above_the_horizon(ground_position_lat, ground_position_lon, date, date_format = "%d/%m/%Y", time_window = 24, satellite_sensor = 'aqua', elevation = 0):
    '''time_above_the_horizon calculates the observation times of satellite passes for the day and time window of a given position on the earth.
    It is based on pyorbital functions.

    ground_position_lat = -19.2590 # The latitude of the ground position (int)
    ground_position_lon = 146.8169 # The longitude of the ground position (int)
    date = '21/06/2016' # date of the day to find passes on. (This is techincally in local time for your location an is converted to UTC internally here.) (string)
    date_format = "%d/%m/%Y" # the format of thh date string (string)
    satellite_sensor = 'aqua' # the name of the satellite sensor you are tracking (string) see:
    time_window = 24 # Number of hours to find passes (int)
    elevation = 0 # the elevation of horizon to compute risetime and falltime. (int)

    Returns: [(rise-time, fall-time, max-elevation-time), ...] as datetime objects in the UTC time zone.

    Contact:
    robtheoceanographer@gmail.com
    '''
    # check the lat and lons to be sensible.
    futs.check_for_sensible_lat_long([ground_position_lat, ground_position_lon])
    #set up the satellite
    orb = Orbital(satellite_sensor)
    # convert the local time to a utc time.
    utc_date = futs.local_to_utc(futs.which_time_zone(ground_position_lat, ground_position_lon), date, date_format)
    # do calcs and remove the utc awareness from the utc_date so that pyorbital can use it.
    time_satellite_is_above_horizon = orb.get_next_passes(utc_date.replace(tzinfo=None), time_window, ground_position_lon, ground_position_lon, elevation)
    return time_satellite_is_above_horizon
