

# Tests...
# ------------------------------------------------------------
check_for_sensible_lat_long([-19.2590,146.8169])

check_for_sensible_lat_long([-19.2590,181])
check_for_sensible_lat_long([-19.2590,-181])
check_for_sensible_lat_long([-91,-181])
check_for_sensible_lat_long([-19.2590,146.8169])
check_for_sensible_lat_long([146.8169,-19.2590], order_expected = ['lon','lat'])
check_for_sensible_lat_long([-19.2590,146.8169], order_expected = ['lon','lat'])
check_for_sensible_lat_long([181,-19.2590], order_expected = ['lon','lat'])
check_for_sensible_lat_long([-181,-19.2590], order_expected = ['lon','lat'])
check_for_sensible_lat_long([146.8169,-91], order_expected = ['lon','lat'])
check_for_sensible_lat_long([146.8169,-91], order_expected = ['lon','lat'])
