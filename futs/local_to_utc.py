from datetime import datetime
from dateutil import tz
def local_to_utc(local_time_zone, date, date_format = "%d/%m/%Y"):
    '''local_to_utc is a function to convert from local to utc time zones.

    local_time_zone = 'Australia/Brisbane'
    date = '21/06/2016 00:00'
    date_format = "%d/%m/%Y %H:%M"

    Contact:
    robtheoceanographer@gmail.com
    '''
    utc_zone = tz.gettz('UTC')
    local_zone = tz.gettz(local_time_zone)
    local_datetime = datetime.strptime(date, date_format).replace(tzinfo=local_zone)
    utc_datetime = local_datetime.astimezone(utc_zone)
    return utc_datetime
