import unittest
from functions.customer_database_functions import *

class TestCustomerDatabaseFunctions(unittest.TestCase):
    """Tests functions in customer_database_functions.py"""
    
    def test_valid_address_success(self):
        """These are values which SHOULD work"""
        valid_addresses_to_test = ["123 ABC Street", ",", "-", "123", "ABC"]

        for address in valid_addresses_to_test:
            self.assertTrue(validAddress(address))

    def test_valid_address_failure(self):
        """These are values which should NOT work"""
        invalid_addresses_to_test = ["", " ", "!", "\"", "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", "[", "]", "{", "}"]

        for address in invalid_addresses_to_test:
            self.assertFalse(validAddress(address))

    def test_valid_city_success(self):
        """These are values which SHOULD work"""
        valid_cities_to_test = ["City", "Ci ty", "Ci'ty", "city", "CITY"]

        for city in valid_cities_to_test:
            self.assertTrue(validCity(city))

    def test_valid_city_failure(self):
        """These are values which should NOT work"""
        invalid_cities_to_test = ["", " ", "!@#", "City!@#%", "123", "City123"]

        for city in invalid_cities_to_test:
            self.assertFalse(validCity(city))

    def test_valid_email_success(self):
        """These are values which SHOULD work"""
        valid_emails_to_test = ["bob@gmail.com", ""]

        for email in valid_emails_to_test:
            self.assertTrue(validEmail(email))

    def test_valid_email_failure(self):
        """These are values which should NOT work"""
        invalid_emails_to_test = ["bob @ gmail.com", "!", "\"", "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", " "]

        for email in invalid_emails_to_test:
            self.assertFalse(validEmail(email))

    def test_valid_name_success(self):
        """These are values which SHOULD work"""
        valid_names_to_test = ["Zach", "Za-ch", "Za'ch"]

        for name in valid_names_to_test:
            self.assertTrue(validName(name))

    def test_valid_name_failure(self):
        """These are values which should NOT work"""
        invalid_names_to_test = ["Za%#$ch", "Z4ch", "", " "]

        for name in invalid_names_to_test:
            self.assertFalse(validName(name))

    def test_valid_phone_success(self):
        """These are values which SHOULD work"""
        valid_phones_to_test = ["1234567890", "123-456-7890", ""]

        for phone in valid_phones_to_test:
            self.assertTrue(validPhone(phone))

    def test_valid_phone_failure(self):
        """These are values which should NOT work"""
        invalid_phones_to_test = ["123abcd", "123 456", "abc", "!@#", "123$^%"]

        for phone in invalid_phones_to_test:
            self.assertFalse(validPhone(phone))

    def test_valid_state_success(self):
        """These are values which SHOULD work"""
        valid_states_to_test = ["MI", "AZ", "NY"]

        for state in valid_states_to_test:
            self.assertTrue(validState(state))

    def test_valid_state_failure(self):
        """These are values which should NOT work"""
        invalid_states_to_test = ["ABC", "A", "", " ", "12", "!@", "mi"]

        for state in invalid_states_to_test:
            self.assertFalse(validState(state))

    def test_valid_zip_success(self):
        """These are values which SHOULD work"""
        valid_zips_to_test = ["1234", "12345"]

        for zip in valid_zips_to_test:
            self.assertTrue(validZIP(zip))

    def test_valid_zip_failure(self):
        """These are values which should NOT work"""
        invalid_zips_to_test = ["123", "123456", "abcd", "abcde", "!@#$", "!@#$%", "", " "]

        for zip in invalid_zips_to_test:
            self.assertFalse(validZIP(zip))