from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['leo'] = 'davis'
favorite_languages['jon'] = 'larry'
favorite_languages['claire'] = 'elaine'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())
