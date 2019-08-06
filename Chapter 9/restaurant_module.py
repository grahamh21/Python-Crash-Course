class Restaurant():
    '''Defining a class called restaurant'''
    
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 23
        
# Any variable prefixed with self is available to every method in the class 
      
    def describe_restaurant(self):
        print('The name of the restaurant is ' 
            + self.restaurant_name.title() + '.')
        print('The food served is ' + self.cuisine_type + '.')
        print('People served: ' + str(self.number_served))
        
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')
        
    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers
        
    def increment_number_served(self, patrons):
        self.number_served += patrons
