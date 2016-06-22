from unittest import TestCase
import futs

class Test_check_for_sensible_lat_long(TestCase):
    def test_is_working_default(self):
        self.assertTrue(isinstance(futs.check_for_sensible_lat_long([-19.2590,146.8169]), basestring))
    def test_is_working_reverse(self):
        self.assertTrue(isinstance(futs.check_for_sensible_lat_long([146.8169,-19.2590], order_expected = ['lon','lat']), basestring))
    def test_lon_too_big(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-19.2590,190])
    def test_lon_too_small(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-19.2590,-201.0])
    def test_lat_too_big(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [100,146.8169])
    def test_lat_too_small(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-93.6,146.8169])
    def test_lon_too_big_reverse(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [181,-19.2590], order_expected = ['lon','lat'])
    def test_lon_too_small_reverse(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-181,-19.2590], order_expected = ['lon','lat'])
    def test_lat_too_big_reverse(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [120,98.2590], order_expected = ['lon','lat'])
    def test_lat_too_small_reverse(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [120,-99.2590], order_expected = ['lon','lat'])
    def test_wrong_order(self):
        self.assertRaises(AssertionError, futs.check_for_sensible_lat_long, [-19.2590,190], order_expected = ['lon','lat'])
