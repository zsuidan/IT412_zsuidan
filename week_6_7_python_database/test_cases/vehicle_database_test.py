import unittest
from functions.vehicle_database_functions import *

class TestVehicleDatabaseFunctions(unittest.TestCase):
    """Tests functions in vehicle database functions"""
    def test_make_success(self):
        """These are values I think SHOULD work"""
        valid_makes_to_test = ['Ford', 'ford', 'FORD']

        for make in valid_makes_to_test:
            self.assertTrue(validMake(make))
    
    def test_make_failure(self):
        """These are values I think should NOT work"""
        invalid_makes_to_test = ['', '  ', '!@#^', '123']

        for make in invalid_makes_to_test:
            self.assertFalse(validMake(make))
    
    def test_model_success(self):
        """These are values I think SHOULD work"""
        valid_models_to_test = ['Abc 123', 'F-150', 'Abc', '123']

        for model in valid_models_to_test:
            self.assertTrue(validModel(model))

    def test_model_failure(self):
        """These are values I think should NOT work"""
        invalid_models_to_test = ['', '@#%^', 'Abc !@#', '123 !@#']

        for model in invalid_models_to_test:
            self.assertFalse(validModel(model))

    def test_VIN_success(self):
        """These are values I think SHOULD work"""
        valid_VINs_to_test = ['1234ABCD', 'ABCD', 'abcd', '1234']

        for vin in valid_VINs_to_test:
            self.assertTrue(validVIN(vin))

    def test_VIN_failure(self):
        """These are values I think should NOT work"""
        invalid_VINs_to_test = ['', '  ', '!@#%', '123!@%4', 'abcd!@#']

        for vin in invalid_VINs_to_test:
            self.assertFalse(validVIN(vin))

    def test_name_success(self):
        """These are values I think SHOULD work"""
        valid_people_to_test = ['Zach Suidan', 'Zach\'Suidan', 'Zach.Suidan', 'Zach-Suidan', 'Zach,Suidan']

        for person in valid_people_to_test:
            self.assertTrue(validPerson(person))

    def test_name_failure(self):
        """These are values I think should NOT work"""
        invalid_people_to_test = ['1234', '~#%@!', 'Zach!@#', 'Zach123']

        for person in invalid_people_to_test:
            self.assertFalse(validPerson(person))

    def test_price_paid_success(self):
        """These are values I think SHOULD work"""
        valid_prices_to_test = ['', '12.50', '500']

        for price in valid_prices_to_test:
            self.assertTrue(validPricePaid(price))

    def test_price_paid_failure(self):
        """These are values I think should NOT work"""
        invalid_prices_to_test = ['abc', '   ', '!@#']

        for price in invalid_prices_to_test:
            self.assertFalse(validPricePaid(price))

    def test_sales_price_success(self):
        """These are values I think SHOULD work"""
        valid_prices_to_test = ['12.50', '500']

        for price in valid_prices_to_test:
            self.assertTrue(validSalesPrice(price))

    def test_sales_price_failure(self):
        """These are values I think should NOT work"""
        invalid_prices_to_test = ['abc', '   ', '!@#', '']

        for price in invalid_prices_to_test:
            self.assertFalse(validSalesPrice(price))