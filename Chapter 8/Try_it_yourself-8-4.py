####################Try_it_yourself_8-9:Magicians############################
#doing something with each name in a list
def show_magicians(first_name):                                      #parameter
    '''function prints every name in a list'''                       #docstring 
    for name in first_name:
        print('Hello ' + str(name))
    
#list comes after the function
magicians = ['glen', 'larry', 'jordan', 'feldspar']                       #list
show_magicians(magicians)                                   #function(argument)


##############Try_it_yourself_8-10: Great Magicians###########################
#modifying a list 
def make_great(the_great):
        for each_name in the_great:
            each_name = each_name + 'the great'
            
            
            
make_great(magicians)
show_magicians(magicians) 
