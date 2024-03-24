list_size = int(input("Введите количество элементов: "))

elements = []
for i in range(list_size):
    new_element = int(input(f"Введите {i+1} элемент: "))
    elements.append(new_element)

elements.sort()
print(f"Вывод: {elements}")