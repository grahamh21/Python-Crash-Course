from car import Car, ElectricCar
#can import as many classes as you need into a program file - 

#can also import the module (from car) and then access the class we need by
# module_name.class_name syntax. my_tesla = car.ElectricCar('tesla', etc )  

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_beetle = Car('VW', 'beetle', 2015)
print(my_beetle.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
