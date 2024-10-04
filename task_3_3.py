# 1. Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(0, [4,6,4,6])
# print_params(54, 11, 16, 8) # Error
print_params(b = 25)
print_params(c = [1,2,3])

# 2. Распаковка параметров:
value_list = [2, 'book', True]
value_dict = {'a': 3, 'b': 'pen', 'c': True}

print_params(*value_list)
print_params(**value_dict)

# 3. Распаковка + отдельные параметры:

value_list_2 = (54.32, "Строка")
print_params(*value_list_2, 42)


