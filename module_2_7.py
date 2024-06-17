# Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# print_params(a, b,)
print_params(a = 2)
print_params(b = 3, c = 0.5)
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:

values_list = [2, 1.0, True]
values_dict = {'a' : 2, 'b' : False,'c': 5}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:

values_list_2 = [1.0, False]
print_params(*values_list_2, 42)