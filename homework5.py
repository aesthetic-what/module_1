immutable_var = 1,2,3,'int','string'
print('Кортеж:',immutable_var)
print(type(immutable_var))
#immutable_var[0] = 2 - нельзя изменять кортеж, так как он неизменяем, в отличее от списка

mutable_list = [1,2,3,4,'int','food']
print('Список:',mutable_list)
mutable_list[0] = 100
mutable_list[4] = 'string'
new_mutable_list = mutable_list.append(True)
print('Обновленный список:',mutable_list)
print(type(mutable_list))