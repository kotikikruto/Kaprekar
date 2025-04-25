# Вспомогательные функции перевода в 10сс и из 10сс

def in_N(a, N):
    if a == 0:
        return '0'
    n = ''
    k = ''
    while a > 0:
        n = n + str(a % N)
        a = a // N
    n = list(reversed(n))
    for j in range(len(n)):
        k += n[j]
    return k


def in_10(a, n):
    if a == 0:
        return 0
    a = str(a)
    k = 0
    for i in range(len(a)):
        k += int(a[len(a) - i - 1]) * int(n ** i)
    return k
