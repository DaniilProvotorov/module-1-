immutable_var = 1, 4, True, 'dad'
print(immutable_var)
#immutable_var[0] = 7  не можем изменить т.к. кортеж- неизменяемая конструкция, чтобы изменить что-то внутри, там должен быть элемент, структуру которого можно изменить, например, список
mutable_list = [1, 6, 3, True, 'dad']
mutable_list[-1] = 'mam'
print(mutable_list)