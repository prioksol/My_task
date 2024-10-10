def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, int):  # проверка содержания данных типа int
        return data_structure
    if isinstance(data_structure, str):  # проверка содержания данных типа str
        return len(data_structure)
    if isinstance(data_structure, (list, tuple, set)):  # проверка содержания данных типа list, tuple, set
        for i in data_structure:
            summa += calculate_structure_sum(i)  # добавляем i-й элемент к сумме при условиях описанных в строке 3 и 5, если не подходит, функция переходит в строку 9 или возвращается в строку 7
    if isinstance(data_structure, dict):  # проверка содержания данных типа dict
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)  # добавляем значения ключа к сумме при условиях, описанных в строке 3 и 5
            summa += calculate_structure_sum(value)  # добавляем значения величины к сумме при условиях, описанных в строке 3 и 5
    return summa




data_structure=[
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)