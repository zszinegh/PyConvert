from nose.tools import *

import pyconvert.conversions as conv


class TestPyConvert(object):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_convert_string_number_to_float(self):
        """validate_input should convert string number to a float"""
        assert_equal(conv.validate_input('32.4'), 32.4)

    def test_fail_if_string_text(self):
        """validate_input should fail if input is text"""
        assert_equal(conv.validate_input('string'), 'string')

    def test_zero_is_good(self):
        """validate_input should pass if input is 0"""
        assert_equal(conv.validate_input('0'), 0.0)

    def test_convert_celsius_to_fahrenheit(self):
        """celsius_fahrenheit should convert C to F"""
        assert_almost_equal(conv.celsius_fahrenheit(25.5), 77.9, places=1)

    def test_convert_fahrenheit_to_celsius(self):
        """fahrenheit_celsius should convert F to C"""
        assert_almost_equal(conv.fahrenheit_celsius(77.9), 25.5, places=1)

    def test_convert_kms_to_miles(self):
        """kms_miles should convert kms to miles"""
        assert_almost_equal(conv.kms_miles(88.4), 54.9, places=1)

    def test_convert_miles_to_kms(self):
        """miles_kms should convert miles to kms"""
        assert_almost_equal(conv.miles_kms(54.9), 88.4, places=1)