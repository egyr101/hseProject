'''Извлечение корней из обычных чисел'''
from decimal import Decimal, getcontext

def is_number(n):
    if n[0] == '-':
        if n[1:].isdigit():
            return True
        else:
            return False
    else:
        if n.isdigit():
            return True
        else:
            return False

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
        return '0'
    else:
        return '±' + str(sqrt_real(a, dot)) 


a = input()
dot = input()


if (not is_number(a)) or (not is_number(dot)):
    print('Error!')
else:
    a = float(a)
    dot = int(dot)
    if (dot < 0 or int(dot) != dot):
        print('Error!')
    else:
        print(sqrt_real_analytics(a, dot))