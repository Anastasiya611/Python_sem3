# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 10.01] => 0.19

newList = list(map(float, input("введите список чисел:").split()))
subList = []
for i in newList:
    subList.append(i- int(i))
    dif = round(max(subList)- min(subList), 3)
print(f'{dif}')