class Car():
    '''defines a class to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''Return a neatly formatted name'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''shows a cars mileage'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it!')
        
    def update_odometer(self, mileage):
        '''set the odometer to a given value, reject if the number goes down'''
    
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''Increment the odometer by a given amount'''
        self.odometer_reading += miles

class Battery():
	'''A simple attempt to model a battery for an electric car.'''
	
	def __init__(self, battery_size=70):
		'''Initialize the batterys attributes'''
		self.battery_size = battery_size
		
	def describe_battery(self):
		'''print a statement describing the battery size.'''
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')  
		
	def get_range(self):
		'''Print a statement about the range of the battery.'''
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This can can go approximately " + str(range)
		message += ' miles on a full charge.'
		print(message)  


class ElectricCar(Car):
	'''Represents a simple electric car'''
	
	def __init__(self, make, model, year):
		'''Initialize attribues of the parent class.'''
		super().__init__(make, model, year)
		self.battery = Battery()
		
	def describe_battery(self):
		'''a method to describe the battery size'''
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')
	
	def fill_gas_tank(self):
		'''Electric cars dont have gas tanks!'''
		print('This car does not need a gas tank!')
		
my_tesla = ElectricCar('tesla', 'model s', 2016)

