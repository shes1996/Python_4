# Вычислить число c заданной точностью d
# Пример - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from decimal import Decimal

pi = '3.14159265358979323846'
accuracy = lambda x: Decimal(x).quantize(Decimal(input('Введите точность d в виде 0.001: ')))
print(accuracy(pi))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

user_number = int(input('Insert your number: '))

i = 2
multipliers = []
while i ** 2 <= user_number:
    while user_number % i == 0:
        multipliers.append(i)
        user_number = user_number // i
    i = i + 1
if user_number > 1:
    multipliers.append(user_number)
print(multipliers)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
nums = [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
new_nums = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        new_nums.append(nums[i])

print(nums)
print(new_nums)

# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень многочлена (наивысшая степень в полиноме): '))


def polinom(k):
    with open('file2.txt', 'w') as polinom:
        for i in range(k, -1, -1):
            if i > 0:
                koef = randint(0, 100)
                if koef > 0:
                    polinom.write(f'{str(koef)}x^{str(i)} + ')
                else:
                    continue
            else:
                koef = randint(0, 100)
                if koef > 0:
                    polinom.write(f'{str(koef)} =0')
                else:
                    polinom.write(' =0')

#print(polinom(k))

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'r') as polinom1:
    my_str1 = polinom1.read()
with open('file2.txt', 'r') as polinom2:
    my_str2 = polinom2.read()

my_list1 = my_str1.split(' + ')
my_list2 = my_str2.split(' + ')
print(my_list1)
print(my_list2)
koefs1 = []
koefs2 = []

for index in range(len(my_list1)):
    k = my_list1[index]
    if len(k) == 6:
        koefs1.append(k[0:3])
    if len(k) == 4:
        koefs1.append(k[0:1])
    else:
        koefs1.append(k[0:2])

print(koefs1)

for index in range(len(my_list2)):
    k = my_list2[index]
    if len(k) == 6:
        koefs2.append(k[0:3])
    if len(k) == 4:
        koefs2.append(k[0:1])
    else:
        koefs2.append(k[0:2])

print(koefs2)

koefs = []
koefs = [(int(koefs1[i]) + int(koefs2[i])) for i in range(len(koefs1))]
print(koefs)

with open('file3.txt', 'w') as two_polinom:
    for i in range(len(koefs)):
        if i < 4:
            two_polinom.write(f'{str(koefs[i])}x^{str(len(koefs) - 1 - i)} + ')
        elif i == 4:
            two_polinom.write(f'{str(koefs[i])}x + ')
        else:
            two_polinom.write(f'{str(koefs[i])} = 0')