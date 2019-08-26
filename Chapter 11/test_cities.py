import unittest
from try_it_yourself_11_1 import city_country

class NamesTestCityCountry(unittest.TestCase):
    '''tests whether imported function works'''
    
    def test_city_country(self):
        test_cc = city_country('madrid', 'spain')
        self.assertEqual(test_cc, 'Madrid, Spain')
    
unittest.main()
