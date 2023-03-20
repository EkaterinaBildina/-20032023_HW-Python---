# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


# first_list = []
# second_list = []
# input_num_n = int(input("Введите число n- кол-во элементов первого множества:  "))
# input_num_m = int(input("Введите число m- кол-во элементов первого множества:  "))


#1 first_list = [1, 4, 5, 8, 9, 12, 5, 6, 7, 2]
import random
first_list = [random.randint(1,20) for i in range(10)]

#2 for _ in range(input_num_n):
#    first_list.append(int(input(f"Введите элементы множества N: ")))
#    print(first_list)

#1 second_list = [1, 3, 1, 12, 6, 10, 5, 8]

second_list = [random.randint(1,20) for i in range(10)]

#2 for _ in range(input_num_m):
#    second_list.append(int(input(f"Введите элементы множества M: ")))
#    print(second_list)

cross_list = {}
for i in first_list:
    for j in second_list:
        if i == j:
            cross_list[i] = i

print(f"Для множеств N: {first_list}")
print(f"Для множеств М: {second_list}")
print("в обоих множествах встречаются числа: ")
print(sorted(cross_list))
