import unittest
from chapter11 import city_country
from chapter11 import Employee

class TestCityCountryCase(unittest.TestCase):
    """test the city_country function in chapter 11"""
    def test_city_country(self):
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_country_pop(self):
        formatted_city = city_country('santiago', 'chile', 500000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population: 500000')

unittest.main()

class TestEmployee(unittest.TestCase):
    """tests the employee class"""
    def setUp(self):        
        self.base_salary = 175000
        self.my_employee = Employee('steve', 'smith', self.base_salary)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertGreater(self.my_employee.salary, self.base_salary)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(20000)
        self.assertGreater(self.my_employee.salary, self.base_salary)

unittest.main()