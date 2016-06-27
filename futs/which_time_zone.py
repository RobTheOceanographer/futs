from tzwhere import tzwhere
import futs
def which_time_zone(ground_position_lat, ground_position_lon):
    '''which_time_zone takes a gps coord and returns the timezone it falls in.

    Contact:
    robtheoceanographer@gmail.com
    '''
    # check the lat and lons to be sensible.
    futs.check_for_sensible_lat_long([ground_position_lat, ground_position_lon])
    tz = tzwhere.tzwhere()
    return tz.tzNameAt(ground_position_lat, ground_position_lon)
