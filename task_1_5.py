immutable_var = 20, 40, 60, False, "tube"
print(immutable_var)
# immutable_var[2]=50    # Кортеж не поддерживает обращение по элементам, поэтому изменить его невозможно
mutable_list = ['car', 'bike', 'train', 'plane']
print(mutable_list)
mutable_list[1]='cycle'
print(mutable_list)