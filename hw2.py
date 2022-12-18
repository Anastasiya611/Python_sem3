#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

newList = list(map(int, input("введите список чисел:").split()))
compList = []
for i in range((len(newList)+1)//2):
    compList.append(newList[i]*newList[len(newList)-1-i])
print(f'{compList}')