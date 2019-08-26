#Try it yourself 11-1: City, Country

def city_country(city_name, country_name):
    '''A function that combines cities and countries in a formatted line'''
    full_description = city_name + ', ' + country_name
    return full_description.title()
    
city_country('boston', 'usa')

