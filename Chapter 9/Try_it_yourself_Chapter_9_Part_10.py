#Try it yourself 9-13:OrderedDict Rewrite
from collections import OrderedDict
glossary = OrderedDict()

glossary['slice'] = 'A specific group of item(s) in a list'
glossary['list comprehension'] = 'generate lists in one line of code'
glossary['range function'] = 'use to generate a series of numbers'
glossary['string'] = 'a series of characters'
glossary['concatenation'] = 'method of combining strings'
glossary['set'] = 'similar to a list except that each item must be unique'
glossary['list'] = 'collection of items in a particular order'
glossary['len()method']='can find the length of something'
glossary['reverse()method'] = 'used to reverse the original order of a list'
glossary['class'] = 'represent real world things and situations'
glossary['function'] = 'named blocks of code that are designed to do one job'

for name, value in glossary.items():
    print(name.title() + ' : ' + value.title())

#can use a for loop in the list, or in the dictionary.keys(), depends on
#what you want to poll.
