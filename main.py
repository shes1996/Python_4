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

power = int(input('Введите натуральную степень многочлена (наивысшая степень в полиноме): '))


def polinom(power):
    with open('file2.txt', 'w') as polinom:
        for i in range(power, -1, -1):
            koef = randint(0, 100)
            if i > 0:
                if koef > 0:
                    polinom.write(f'{str(koef)}x^{str(i)} + ')
            else:
                if koef > 0:
                    polinom.write(f'{str(koef)} = 0')
                else:
                    polinom.write(' = 0')

#polinom(power)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'r') as polinom1:
    my_str1 = polinom1.read()
with open('file2.txt', 'r') as polinom2:
    my_str2 = polinom2.read()

my_list1 = my_str1.split(' + ')
my_list2 = my_str2.split(' + ')

dictionary1 = {}

for i in range(len(my_list1)):
    if 'x' in my_list1[i]:
        posX = my_list1[i].find('x')
        dictionary1[int(my_list1[i][posX + 2:])] = int(my_list1[i][:posX])
    else:
        posEqualy = my_list1[i].find(' =')
        dictionary1[0] = int(my_list1[i][:posEqualy])

print(dictionary1)
dictionary2 = {}

for i in range(len(my_list2)):
    if 'x' in my_list2[i]:
        posX = my_list2[i].find('x')
        dictionary2[int(my_list2[i][posX + 2:])] = int(my_list2[i][:posX])
    else:
        posEqualy = my_list2[i].find(' = ')
        dictionary2[0] = int(my_list2[i][:posEqualy])

print(dictionary2)

maxDegree = max(max(dictionary1.keys()), max(dictionary2.keys()))

with open('file3.txt', 'w') as two_polinom:
    for i in range(maxDegree, 0, -1):
        koef = 0
        if i in dictionary1.keys():
            koef += dictionary1[i]
        if i in dictionary2.keys():
            koef += dictionary2[i]
        if koef != 0:
            two_polinom.write(f'{koef}x^{i} + ')
    koef = 0
    if 0 in dictionary1.keys():
        koef += dictionary1[0]
    if 0 in dictionary2.keys():
         koef += dictionary2[0]
    if koef != 0:
         two_polinom.write(f'{koef} = 0')

