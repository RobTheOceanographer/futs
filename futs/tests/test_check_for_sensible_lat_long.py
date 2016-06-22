from unittest import TestCase
import futs

# def test_afunction_throws_exception(self):
#     self.assertRaises(ExpectedException, afunction, arg1, arg2)

class Test_check_for_sensible_lat_long(TestCase):
    def test_working(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-19.2590,190])
    def test_working_backwards(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-19.2590,190], order_expected = ['lon','lat'])


# check_for_sensible_lat_long([-19.2590,181])
# check_for_sensible_lat_long([-19.2590,-181])
# check_for_sensible_lat_long([-91,-181])
# check_for_sensible_lat_long([-19.2590,146.8169])
# check_for_sensible_lat_long([146.8169,-19.2590], order_expected = ['lon','lat'])
# check_for_sensible_lat_long([-19.2590,146.8169], order_expected = ['lon','lat'])
# check_for_sensible_lat_long([181,-19.2590], order_expected = ['lon','lat'])
# check_for_sensible_lat_long([-181,-19.2590], order_expected = ['lon','lat'])
# check_for_sensible_lat_long([146.8169,-91], order_expected = ['lon','lat'])
# check_for_sensible_lat_long([146.8169,-91], order_expected = ['lon','lat'])
