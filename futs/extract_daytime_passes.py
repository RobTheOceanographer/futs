from dateutil import tz
def extract_daytime_passes(overpass_times, sunrise_local, sunset_local, local_time_zone):
    '''extract_daytime_passes takes a list of datetimes, usually from the futs.time_above_the_horizon function, and returns only those that occur during daylight hours.

    overpass_times = the list of sat overpass times  to extract the daylight ones from. - format is [(rise-time, fall-time, max-elevation-time), ...] as datetime objects in the UTC time zone.
    sunrise_local = sunrise datetime in its local time zone.
    sunset_local = sunset datetime in its local time zone.
    local_time_zone = the local time zone for the ground position

    Returns: daylight_passes in the same format as the input overpasses - [(rise-time, fall-time, max-elevation-time), ...] as datetime objects in the UTC time zone.

    Contact:
    robtheoceanographer@gmail.com
    '''
    # is a time before or after sunrise?
    utc_zone = tz.gettz('UTC') # convert local sunrise and set times to their utc equivelent.
    local_zone = tz.gettz(local_time_zone)
    sunrise_with_tz = sunrise_local.replace(tzinfo=local_zone)
    sunset_with_tz = sunset_local.replace(tzinfo=local_zone)
    sunrise_in_utc = sunrise_with_tz.astimezone(utc_zone)
    sunset_in_utc = sunset_with_tz.astimezone(utc_zone)
    daylight_passes=[] # an empty list ready for the addition of the daylight passes.
    # compare the times of overpass with the sunrise and set in the utc space.
    for an_overpass in overpass_times:
        assert an_overpass[0] < an_overpass[1], "There is an issue with the order of the overpass elements. This function assumes that the risetime is the first element in each list triplet as per the output of my futs.time_above_the_horizon function."
        sat_risetime = an_overpass[0]
        sat_risetime = sat_risetime.replace(tzinfo=utc_zone)
        # print (sat_risetime > sunrise_in_utc) & (sat_risetime < sunset_in_utc)
        if (sat_risetime > sunrise_in_utc) & (sat_risetime < sunset_in_utc):
            daylight_passes.append(an_overpass)
        # print sat_risetime.astimezone(local_zone)
    # daylight_passes[0][0].replace(tzinfo=utc_zone).astimezone(local_zone)

    return daylight_passes
