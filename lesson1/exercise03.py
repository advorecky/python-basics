# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))

nn = int(("%d%d" % (n, n)))
nnn = int(("%d%d%d" % (n, n, n)))
n_sum = n + nn + nnn

print("Сумма чисел {} + {} + {} = {}".format(n, nn, nnn, n_sum))
