def calculate_series_of_granule_HHMM(risetime_HHMM, falltime_HHMM, step=5):
    '''calculate_series_of_granule_HHMM takes a rise and fall time as HHMM and works out what the 5min granule times are for between those times.

    risetime_HHMM is a string time the satellite comes above the horizon in utc - usually comes from the futs.closest_five_min_granule_time function
    falltime_HHMM is a string time the satellite goes over the horizon in utc - usually comes from the futs.closest_five_min_granule_time function
    step is the time step and is set to 5 for five minute steps as per most nasa ocean colour satellites.

    returns: [HHMM, HHMM, HHMM] a list of HHMM strings that are the 5 on granule times between the risetime_HHMM falltime_HHMM values given.

    Contact:
    robtheoceanographer@gmail.com
    '''
    #calculate the range of numbers as if they were ints.
    tmp_granule_series = range(int(risetime_HHMM), (int(falltime_HHMM)+step), step)
    granule_series = []
    # this checks if the granule number has a 0 in front (e.g. 0210) and is not just three numbers (e.g. 210) as the ftp sites always use file names like 0210. It also makes them strings.
    for HMM_time in tmp_granule_series:
        if len(str(HMM_time)) is 3:
            HHMM_time = '0'+str(HMM_time)
            granule_series.append(HHMM_time)
        else:
            granule_series.append(str(HMM_time))
    # print tmp_granule_series
    # print granule_series
    return granule_series
