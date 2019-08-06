#Try it yourself 9-10:Imported Restaurant
from restaurant_module import Restaurant

mings = Restaurant('mings', 'chinese')
mings.describe_restaurant()

#Try it yourself 9-11:Imported Admin

from admin_module import Admin, User, Privileges

linky = Admin('lily', 'howard', 'dog', 'april', 2013)
linky.privileges.show_privileges()



