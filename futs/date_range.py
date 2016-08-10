from datetime import datetime
from dateutil.relativedelta import relativedelta
def date_range(start_date, end_date, increment, period):
    '''Create a range between two dates based on the increment and period.

    The example "every 8 hours between now and tomorrow 19:00" would be written like this:
        start_date = datetime.now()
        end_date = start_date + relativedelta(days=1)
        end_date = end_date.replace(hour=19, minute=0, second=0, microsecond=0)
        date_range(start_date, end_date, 8, 'hours')
    Notice that the valid values for period are those defined for the relativedelta relative information, namely: 'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds', 'microseconds'.
    URL: http://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval
    '''
    result = []
    nxt = start_date
    delta = relativedelta(**{period:increment})
    while nxt <= end_date:
        result.append(nxt)
        nxt += delta
    return result
