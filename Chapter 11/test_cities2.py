import unittest
from try_it_yourself_11_2 import city_country2

class NamesTestCityCountry(unittest.TestCase):
    '''tests whether imported function works'''
    
    def test_city_country(self):
        test_cc2 = city_country2('barcelona', 'spain')
        self.assertEqual(test_cc2, 'Barcelona, Spain')
        
    def test_city_country_population(self):
        test_cc3 = city_country2('paris', 'france', 100)
        self.assertEqual(test_cc3, 'Paris, France, Population: 100')
    
unittest.main()
