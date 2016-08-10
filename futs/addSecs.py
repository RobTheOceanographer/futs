import datetime
def addSecs(tm, secs = 300):
    ''' Adds a number of seconds to a datetime.
    tm = datetime (must be a full datetime obj not just time or date).
    secs = number of second to add.
    returns the time as a datetime
    '''
    fulldate = tm + datetime.timedelta(seconds=secs)
    return fulldate
