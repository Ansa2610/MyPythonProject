def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

my_lst = [1, 2, 3]
print_params(1, 25, my_lst)

values_list = [2, True, 'Python']
values_dict = {'a': 7, 'b': False, 'c': 'string'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [100, 'note']
print_params(*values_list_2, 42)