import datetime
import futs
def calculate_series_of_granule_HHMM(risetime_HHMM, falltime_HHMM, step=5):
    '''calculate_series_of_granule_HHMM takes a rise and fall time as HHMM and works out what the 5min granule times are for between those times.

    risetime_HHMM is a string time the satellite comes above the horizon in utc - usually comes from the futs.closest_five_min_granule_time function
    falltime_HHMM is a string time the satellite goes over the horizon in utc - usually comes from the futs.closest_five_min_granule_time function
    step is the time step and is set to 5 for five minute steps as per most nasa ocean colour satellites.

    returns: [HHMM, HHMM, HHMM] a list of HHMM strings that are the 5 on granule times between the risetime_HHMM falltime_HHMM values given.

    Contact:
    robtheoceanographer@gmail.com
    '''
    # calculate the difference between the two numbers as if they were datetimes.
    falltime_HHMM_dobj = datetime.datetime.strptime(falltime_HHMM,'%H%M')
    risetime_HHMM_dobj = datetime.datetime.strptime(risetime_HHMM,'%H%M')
    timediff = falltime_HHMM_dobj - risetime_HHMM_dobj
    # how many steps is that?
    number_of_5min_granules = timediff.seconds/60/step
    # add the number of steps to the risetime.
    tmp_granule_series = []
    tmp_granule_series.append(risetime_HHMM_dobj)
    for g in range(number_of_5min_granules):
        tmp_granule_series.append(futs.addSecs(tmp_granule_series[g], secs=60*step))
    del(g)
    # convert the datetimes back to HHMM strings.
    granule_series = []
    for g in tmp_granule_series:
        granule_series.append(g.time().strftime('%H%M'))
    return granule_series
