2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

my_list = [8, 3, 15, 6, 4, 2]
result = [my_list.index(i) for i in my_list if i % 2 == 0]
print(result)
