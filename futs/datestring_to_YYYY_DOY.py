
import datetime
def datestring_to_YYYY_DOY(date, date_format = "%d/%m/%Y"):
    '''datestring_to_YYYY_DOY does what it says on the box - takes a date as a string and tells you what the DOY is and what Year it is in.

    date = '21/06/2016' # date of the day as a string.
    date_format = "%d/%m/%Y" # the format of the date string (string)

    Returns: [YYYY, DOY] as strings.

    Contact:
    robtheoceanographer@gmail.com
    '''
    datetime_obj = datetime.datetime.strptime(date, date_format)
    YYYY = datetime_obj.strftime('%Y')
    DOY = str(datetime_obj.timetuple().tm_yday)
    return YYYY, DOY
