my_dict = {'Anna': 1980, 'Dad': 1947, 'Mom': 1955, 'Bro': 1985}
print(my_dict)
print(my_dict.get('Dad'))
print(my_dict.get('Sis'))
my_dict.update({'Granny': 1927, 'Aunt': 1953}) #add a couple of pairs
print(my_dict)
a = my_dict.pop('Bro') #delete one of the pairs
print(my_dict)
print(a)
print(my_dict)

my_set = {10, 20, 10, 30, 40, 30.5, 30.5, 30.9, True, (1, 2, 3), 'weather'}
print(my_set)
my_set.update([66,'local'])
print(my_set)
my_set.discard('weather')
print(my_set)