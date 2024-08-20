immutable_var = ([1,2,3,4], True, 'food')
print(immutable_var)
#immutable_var [1] = False # внутри кортежа менять исходные данные нельзя, мы можем это делать только с [] скобками
mutable_list = ['school', 'hospital', 'university']
print(mutable_list)
mutable_list[1] = 'home'
print(mutable_list)