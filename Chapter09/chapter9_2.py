from restaurant import Restaurant
from admin import Admin

dennys = Restaurant("dennys", "breakfast")
dennys.describe()

steve = Admin("steve", "smith", dog="larry")
steve.describe()
steve.priviages.show_privilages()