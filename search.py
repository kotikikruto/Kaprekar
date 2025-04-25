# Search_1 - поиск циклов и неподвижных точек
# Search_2 - поиск глубины дерева
from kaprekar import Kaprekar
from conversion import in_N
from make_values import solving_the_main_problem


def Search_1(nums, l, s):  # Получаем на вход множество из неподвижных точек и циклов, длину, систему счисления
    nums = sorted(nums)  # Отсортировали список
    nums_new = []  # Множество чисел, которые уже обработали
    nwonn = nums  # Множество чисел, которые еще не обработали (Nums WithOut Nums_New)
    a = []  # Множество чисел, участвующих в одном цикле
    k = 0  #
    while len(nwonn) != 0:
        if k == 0:
            a.append(nwonn[k])  # Добавили в a первое число из очереди необработанных чисел
            nums_new.append(nwonn[k])  # Показали, что первое число обработали
        c = Kaprekar(nwonn[k], l, s)  # Результат значения функции Капрекара от последнего элемента в a
        if c in a:  # Если c уже находится в массиве, значит, цикл закончен,
            # выводим его и определяем, цикл это или неподвижная точка
            for i in range(len(a)):
                print(in_N(a[i], s), end=" -> ")
            print(in_N(c, s), end=", ")
            if len(a) == 1:
                print('Неподвижная точка')
            else:
                print('Цикл длины', len(a))
            nwonn = []  # Обновляем очередь, убирая оттуда уже обработанные числа
            for i in range(len(nums)):
                if nums[i] not in nums_new:
                    nwonn.append(nums[i])
            a = []
            k = 0
        else:  # Если новое значение еще не находится в a
            for i in range(len(nwonn)):  # Ищем, под каким индексом он находится в nwonn
                if nwonn[i] == c:
                    k = i
                    break
            a.append(c)  # Добавляем в a это значение
            nums_new.append(c)  # Добавляем в множество обработанных чисел


def Search_2(nums, l, s):
    all_nums = solving_the_main_problem(s, l)
    c = 0  # Текущее число итераций
    c1 = 0  # Максимальное число итераций
    for i in range(len(all_nums)):
        n = all_nums[i]
        while n not in nums:  # Пока не пришли к множеству значений, делаем еще одну итерацию и увеличиваем счетчик на 1
            n = Kaprekar(n, l, s)
            c += 1
        c1 = max(c, c1)
        c = 0
    print("Глубина дерева:", c1)
