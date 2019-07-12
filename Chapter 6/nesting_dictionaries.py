leo = {'age' : 27, 'last_name' : 'howard', 'occupation' : 'baker'}
simon = {'age' :25, 'last_name' : 'howard', 'occupation' : 'hotel'}
graham = {'age' : 31, 'last_name' : 'howard', 'occupation' : 'IT'}

howards = ['leo', 'simon', 'graham']
for howard in howards:
    print(howard)
#notice with the ' around the names in howards, the above just prints a list

howardz = [leo, simon, graham]
for heyward in howardz:
    print(heyward)
#by removing the ' around the names, it now prints the dictionaries

for heyward1 in howardz:
    print(heyward1.keys())

print(heyward1.values())
#heyward1 in the for loop for howardz, stays last on graham. heyward1.values()
#prints the values for the last heyward1 (ie graham)
print('\n')
for heyward1 in howardz:
    print(heyward1.values())

