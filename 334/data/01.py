A = int(input())
B = int(input())
# насколько одно число больше другого? что прибавлять к меньшему
Diff = int(abs(A - B))
# Для того чтобы получить четкий признак + или -
isPositive = (A // B - B // A)
# что-то вроде сигмоида, но используются везде Int и не используются
# другие функции.
# Питон приводит тип к Int и получаем ноль вместо очень маленького
# положительного числа
dec = int(10 ** isPositive // 10 * (A // B))
# выводим число В. Если оно больше, то к нему прибавляется разница,
# умноженная на 0, иначе - число В - меньше
# и к нему прибавляется разность А и В
R = int(B + dec * Diff)
print(R)