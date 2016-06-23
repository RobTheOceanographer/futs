import ephem
from datetime import datetime
import futs
def when_is_sunrise_and_sunset(ground_position_lat, ground_position_lon, date, date_format = "%d/%m/%Y"):
    '''when_is_sunrise_and_sunset calculates the sunrise and sunset time at any location on earth for the date given.

    ground_position_lat = -19.2590 # The latitude of the ground position (int)
    ground_position_lon = 146.8169 # The longitude of the ground position (int)
    date = '21/06/2016' # date of the day to find passes on in UTC (string)
    date_format = "%d/%m/%Y" # the format of thh date string (string)

    Returns: [sunrise-time, sunset-time)] as datetime objects in the local time zone

    Contact:
    robtheoceanographer@gmail.com
    '''
    # check the lat and lons to be sensible.
    futs.check_for_sensible_lat_long([ground_position_lat, ground_position_lon])
    # set up my observer.
    user = ephem.Observer()
    user.lat = ground_position_lat
    user.lon = ground_position_lon
    user.date = datetime.strptime(date, date_format)
    # set up the celestial body we're interested in
    body=ephem.Sun()
    body.compute()
    # do the calcs
    local_sun_rise_set = [ephem.localtime(user.previous_rising(body)),ephem.localtime(user.next_setting(body))] # rise then set
    return local_sun_rise_set
