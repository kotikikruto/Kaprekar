from conversion import in_10


def solving_the_combinatorial_problem(b, k):  # Вспомогательная функция, решаем задачу с шариками и корзинами
    if k == 0:  # Если шариков не осталось, корзины оставляем пустыми
        return [b * '0']
    elif b == 1:  # Если осталась только одна корзина, складываем туда все оставшиеся шарики
        return [str(k)]
    else:  # В иных случаях используем рекурсию
        solution = []
        for i in range(k + 1):  # Забрали i шариков для первой корзины,
            solution_of_subtask = solving_the_combinatorial_problem(b - 1, k - i)  # рассмотрели подзадачу с меньшим количеством корзин
            for j in range(len(solution_of_subtask)):
                solution.append(str(i) + solution_of_subtask[j])
        return solution


def solving_the_main_problem(b, k):  # Основная функция, через решение задачи с шариками и корзинами восстановим интересующий набор цифр
    solution = []
    solution_of_previous_problem = solving_the_combinatorial_problem(b, k)  # Получили вспомогательный набор
    for i in range(len(solution_of_previous_problem)):
        s = ''
        for j in range(b):
            s += int(solution_of_previous_problem[i][j]) * str(j)  # Восстановили текущее число по набору
        solution.append(in_10(s, b))
    return solution
