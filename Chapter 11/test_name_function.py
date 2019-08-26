import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Tests for 'name_function.py'.'''
    
    def test_first_last_name(self):
        '''Do names like 'Elvis Presley' work?'''
        formatted_name = get_formatted_name('elvis', 'presley')
        self.assertEqual(formatted_name, 'Elvis Presley')

    def test_first_last_middle_name(self):
        '''Do names like graham mckay howard work'''
        formatted_name = get_formatted_name('graham', 'howard', 'mckay')
        self.assertEqual(formatted_name, 'Graham Mckay Howard')
        
unittest.main()
