my_dict = {'Egor': 2011, 'Adam': 2000, 'Sam': 2021}
print('Dict:',my_dict)
print('Existing value:',my_dict['Egor'])
print('Existing value:',my_dict['Sam'])
print('Not existing value:',my_dict.get('Linda'))
my_dict.update({'Nikita': 2010,
                'Anton': 1970})
print(my_dict)
del my_dict['Sam']
print(my_dict)

########################

my_set = {1,2,3,4,5,6,1,3,2,4,4,5,3,2,1}
print('Set:',my_set)
my_set.add((1,3,5,2,611.2))
my_set.add('Apple')
print('Set:',my_set)
my_set.remove(1)
print('Set:',my_set)