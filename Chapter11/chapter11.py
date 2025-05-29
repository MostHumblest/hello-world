#11-1 City Country
print("\n11-1 City Country")
def city_country(city, country, population=''):
    if population:
        formatted_string = city.title() + ", " + country.title() + " - population: " + str(population)
    else:
        formatted_string = city.title() + ", " + country.title()
    return formatted_string

#11-3
class Employee():
    """defines an employee and salary"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """gives the employee a raise, default is 5k"""
        self.salary = self.salary + amount
    
    def show_employee_info(self):
        """print employee info"""
        fullname = self.first + ' ' + self.last
        print(fullname.title() + ' earns $' + str(self.salary))

steve = Employee('steve', 'smith', 175000)
steve.show_employee_info()
