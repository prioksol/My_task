my_dict = {'Oxana': 1980, 'Nelly': 1977, 'Lev': 2008}
print('Dic:',my_dict)
print('Date_Oxana:', my_dict.get('Oxana'))
print('Not exiting value:', my_dict.get('Victor', 'None'))
my_dict.update({'Yakov': 2010, 'Vic': 1955})
my_dict.pop('Nelly')
print('Deleted value:', '1977')
print('Modified dictionary:', my_dict)

my_set = {7, 9, 8, 7, 7, 5, 8, 5, 9, 'ice', 'water', True, (12,15,18), 'air'}
print('set:', my_set)
new_elements = 4, 'wind'
print(my_set.add(new_elements))
print(my_set.remove(7))
print('Modified set:', my_set)



