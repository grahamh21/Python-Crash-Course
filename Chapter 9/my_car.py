from car import Car

my_new_car = Car('lexus', 'sl500', 1995)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer = 10
my_new_car.read_odometer()
my_new_car.update_odometer = 9
my_new_car.read_odometer()
