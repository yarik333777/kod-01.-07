my_dict = {'Tom': 2001, 'Anton': 2004, 'Lili': 2003}
print(my_dict)
my_dict['Dinise'] = 2009
print(my_dict['Dinise'])
my_dict.update({'Pavle': 2003,
                'Qliya': 2003})
print(my_dict)
del my_dict['Dinise']
print({'Dinise': 2009})
print(my_dict)

my_set = {1, 2, 2, 1, 1, 3, 4, 5, 4, 6, 7, True, False, False, True, 'hello World'}
print(my_set)
my_set.add(9)
my_set.update({'hello world', 45, True})
print(my_set)
my_set.remove(45)
print(my_set)



