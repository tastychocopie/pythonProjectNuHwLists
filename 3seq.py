list1 = input("Введите элемент 1-ого списка через запятую: ").split(',')

list2 = input("Введите элемент 2-ого списка через запятую: ").split(',')

result = [x for x in list1 if x not in list2]
result.sort()
unique_list = sorted(set(result), key=int)
print("Результат:", ','.join(unique_list))