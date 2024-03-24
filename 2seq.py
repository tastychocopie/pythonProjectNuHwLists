input_str = input("Введите элементы списка через запятую: ")
input_list = input_str.split(',')

unique_list = sorted(set(input_list), key=int)
print("Результат:", ", ".join(unique_list))