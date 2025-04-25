def Kaprekar(n, k, b):  # Задано число (последовательность цифр) n длины k в системе счисления b
    if (type(n) is int) and (n in range(b ** k)) and \
            (type(k) is int) and (k >= 2) & \
            (type(b) is int) and (b >= 2):
        d = []
        for m in range(k):
            n, q = divmod(n, b)
            d.append(q)

        l_alpha = sorted(d, reverse=True)
        l_omega = sorted(d)

        def N(l):
            c = 0
            for m in range(k):
                c = c * b + l[m]
            return c

        i_alpha = N(l_alpha)
        i_omega = N(l_omega)
        return i_alpha - i_omega
    else:
        return None