
def check_for_sensible_lat_long(ground_position, order_expected = ['lat','lon']):
    '''Check that the values of lat and long given to this function are between -90 and 90 and -180 and 180.

    ground_position = [-19.2590,146.8169] # this is the lat and long of your site. the order is determinged by the order_expected.
    order_expected = ['lat','lon'] or ['lon','lat']

    Returns an AssertionError is it fails or the string "Lat and Lon values seem sensible." is successful.

    Contact:
    robtheoceanographer@gmail.com

    '''
    if order_expected == ['lat','lon']:
        assert (ground_position[0] <= 90) & (ground_position[0] >= -90), "Your latitude values seem to be inccorrect. I expected them to be between -90 and 90."
        assert (ground_position[1] <= 180) & (ground_position[1] >= -180), "Your longitude values seem to be inccorrect. I expected them to be between -180 and 180."
    elif order_expected == ['lon','lat']:
        assert (ground_position[1] <= 90) & (ground_position[1] >= -90), "Your latitude values seem to be inccorrect. I expected them to be between -90 and 90."
        assert (ground_position[0] <= 180) & (ground_position[0] >= -180), "Your longitude values seem to be inccorrect. I expected them to be between -180 and 180."
    else:
        print "I am not familiar with your order_expected, there might be a typo there. I expected it to be either ['lat','lon'] or ['lon','lat']."
    print "Lat and Lon values seem sensible."
