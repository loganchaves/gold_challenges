import unittest
import outing_repo
from outing import Outing



class Testouting_repo (unittest.TestCase):

    def test_outing_repo_create_outing_should_add_outing_to_all_outings(self):
        self.outing_type = 'type'
        self.numberofpeople = 2
        self.date = 'date'
        self.costperperson = 2
        self.costperevent = 4
        self.outing1 = outing_repo.create_outing(self.outing_type, self.numberofpeople, self.date, self.costperperson, self.costperevent)
        actual = len(outing_repo.all_outings)
        expected = 1

        self.assertEqual(actual,expected)

    def test_total_cost_this_year(self):
        
        actual = outing_repo.total_cost_this_year()
        expected = 104

        self.assertEqual(actual, expected)
    def test_total_cost_of_type_should_add_all_of_certain_type(self):
        self.outing2 = outing_repo.create_outing('pizza', 10, '01/01/2019', 50, 100)
        
        actual = outing_repo.total_cost_of_type('pizza')
        expected = 100

        self.assertEqual(expected, actual)
    
        
