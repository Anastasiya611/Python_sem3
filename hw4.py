#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:- 45 -> 101101 - 3 -> 11 - 2 -> 10

numder = int(input("Введите десятичное число:"))
binary = 0
k = 1
while numder > 0:
    div = numder%2
    binary +=div*k
    numder //=2
    k*=10
print (f'{binary}')