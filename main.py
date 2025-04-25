# Основной файл
from kaprekar import Kaprekar
from search import Search_1, Search_2
from make_values import solving_the_main_problem

lenght = int(input("Введите длину (от 2 до 10): "))  # Ввод длины числа
base = int(input("Введите систему счисления (от 2 до 10): "))  # Ввод системы счисления

range_of_values = solving_the_main_problem(base, lenght)  # Составляем область определения
range_of_values_new = []  # Область значений функции капрекара, пока не заполнено

while True:
    for i in range(len(range_of_values)):
        k = Kaprekar(range_of_values[i], lenght, base)
        if k not in range_of_values_new:
            range_of_values_new.append(k)  # Заполняем область значений
    if len(range_of_values) == len(range_of_values_new):
        break  # Из свойства унаров понятно, что в области значений не может появиться значение, которого
        # нет в области определения, тогда из равенства мощностей множеств следует равенство множеств

    range_of_values = range_of_values_new  # Теперь область значений стала областью определения
    range_of_values_new = []  # Новая область значений снова пустая

Search_1(range_of_values, lenght, base)  # Эта функция ищет циклы и неподвижные точки
Search_2(range_of_values, lenght, base)  # Эта функция ищет глубину дерева
# (максимальное число итераций, которое необходимо, чтобы войти в цикл или неподвижную точку)
