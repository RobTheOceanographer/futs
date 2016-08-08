import futs
def closest_five_min_granule_time(riseORfalltime, riseORfall = 'rise'):
    '''closest_five_min_granule_time takes a risetime or falltime datetime and returns the HHMM of the nearest 5min granule time.

    The riseORfall flag must be set to either 'rise' or 'fall' as we round the time down if it is a rise time and up if it is a fall time to make sure we capture as much data as possible.

    riseORfalltime is a datetime object of the time the satellite comes above the horizon or goes below the horizan in utc.

    Returns: a four letter string of time that should be in multiple of five like '0245'

    Contact:
    robtheoceanographer@gmail.com
    '''
    HHMM =  riseORfalltime.strftime('%H%M')
    # We round the time down if it is a rise time and up if it is a fall time to make sure we capture as much data as possible.
    if riseORfall is 'rise':
        rounded_time = futs.round_down_to_nearest(int(HHMM))
    elif riseORfall is 'fall':
        rounded_time = futs.round_up_to_nearest(int(HHMM))
    else:
        raise Exception("The riseORfall flag must be set to either 'rise' or 'fall'")

    if len(str(rounded_time)) is 3:
        five_min_time = '0'+str(rounded_time)
    else:
        five_min_time = str(rounded_time)

    if str(five_min_time)[-2:] == '60':
        tmp = int(five_min_time[:-2]) + 1
        if len(str(tmp)) is 1:
            five_min_time = '0'+str(tmp)+'00'
        else:
            five_min_time = str(tmp)+'00'
    return five_min_time

    # HHMM =  riseORfalltime.strftime('%H%M')
    # # We round the time down if it is a rise time and up if it is a fall time to make sure we capture as much data as possible.
    # if riseORfall is 'rise':
    #     rounded_time = futs.round_down_to_nearest(int(HHMM))
    # elif riseORfall is 'fall':
    #     rounded_time = futs.round_up_to_nearest(int(HHMM))
    # else:
    #     raise Exception("The riseORfall flag must be set to either 'rise' or 'fall'")
    #
    # if len(str(rounded_time)) is 3:
    #     five_min_time = '0'+str(rounded_time)
    # else:
    #     five_min_time = str(rounded_time)
    # return five_min_time
