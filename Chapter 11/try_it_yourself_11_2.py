#Try it yourself 11-2: Population

def city_country2(city_name, country_name, population = ''):
    #optional parameter
    '''A function that combines cities and countries in a formatted line'''
    if population:
        full_description = city_name + ', ' + country_name + ', Population: ' + str(population)
    else:
        full_description = city_name + ', ' + country_name
    return full_description.title()
    
city_country2('boston', 'usa')
