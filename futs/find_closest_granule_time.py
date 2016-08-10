import futs
from datetime import datetime
from dateutil.relativedelta import relativedelta
def find_closest_granule_time(riseORfalltime, granule_step = 6):
    '''Finds the closest granule time to the datetime you pass into it.
    The function works out a list of granules that we can compare against for that day by creatign a list from midnight on the day you give it stepping through the day in the granule_steps until the end of that day.
    It then finds the closest match in this list to the datetime you gave it.

    riseORfalltime = a datetime obj that is the time you want to find the closest granule for.
    granule_step = the number of minutes to divide the day up into for the granules - modis is 5mins viirs is 6mins.

    returns a datetime obj of the closest granule on the day.
    '''
    start_date = datetime(riseORfalltime.date().year,riseORfalltime.date().month,riseORfalltime.date().day) # start at midnight on the dat of interest
    end_date = start_date + relativedelta(days=1) #end the beginning of the next day.
    # work out a list of granules that we can compare against for that day.
    datetime_list = futs.date_range(start_date, end_date, granule_step, 'minutes')
    # remove the last time step  as it's a 0000 on the next day and we're not interested in that day.
    datetime_list.pop()
    # find the closest granule time in the list we just made to the datetime we were passed.
    closest_granule_time = min(datetime_list, key=lambda x:abs(x - riseORfalltime))
    return closest_granule_time #return the closest matching granule time as a datetime.
