#Try it yourself 9-1: Restaurant

class Restaurant():
    '''Defining a class called restaurant'''
    
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('The name of the restaurant is ' 
            + self.restaurant_name.title() + '.')
        print('The food served is ' + self.cuisine_type + '.')
# Any variable prefixed with self is available to every method in the class        
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')
        
        
good_luck = Restaurant('good luck', 'new american')
cure = Restaurant('cure', 'french')
cedars_med = Restaurant('cedars mediterranian', 'greek')

print(good_luck.restaurant_name)
print(good_luck.cuisine_type)



good_luck.describe_restaurant()
good_luck.open_restaurant()

#Try it yourself 9-2: Three Restaurants
print('!!!!!!!!!!!!!!!!!!!!!!!!!')
good_luck.describe_restaurant()
cure.describe_restaurant()
cedars_med.describe_restaurant()


