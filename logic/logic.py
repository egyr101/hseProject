'''Извлечение корней из обычных чисел'''
from decimal import Decimal, getcontext

def sqrt_real(a, dot):
    """Вычисление корня с точностью dot знаков используя Decimal"""
    # Устанавливаем точность (dot знаков после запятой + запас)
    getcontext().prec = dot + 10
    
    if a < 0:
        a = abs(a)
    
    x = Decimal(a)
    # Метод Ньютона с Decimal
    for i in range(50):  # Достаточно итераций для сходимости
        next_x = (x + Decimal(a) / x) / Decimal(2)
        if next_x == x:
            break
        x = next_x
    
    # Форматируем вывод с dot знаками
    return format(x, f'.{dot}f')

def sqrt_real_analytics(a, dot):
    if a < 0:
        return '±' + str(sqrt_real(a, dot)) + 'i'
    elif a == 0:
        return sqrt_real(a, dot)
    else:
        return '±' + str(sqrt_real(a, dot)) 


a = input()
dot = input()

if (not a.isdigit()) or (not dot.isdigit()):
    print('Error!')
else:
    a = float(a)
    dot = float(dot)
    if (dot < 0 or int(dot) != dot):
        print('Error!')
    else:
        print(sqrt_real_analytics(a, dot))