'''Извлечение корней из всех чисел'''
from decimal import Decimal, getcontext
import gui.gui as g

''' from numba import njit '''


def sqrt_real(a, dot):
    """Вычисление корня с точностью dot знаков используя Decimal"""
    # Устанавливаем точность (dot знаков после запятой + запас)
    getcontext().prec = dot + 10
    
    if a < 0:
        a = abs(a)
    
    x = Decimal(a)
    # Метод Ньютона с Decimal
    for i in range(1000):  # Достаточно итераций для сходимости
        next_x = (x + Decimal(a) / x) / Decimal(2)
        if next_x == x:
            break
        x = next_x
    
    if dot == 0:
        return round(x, 0)
    else:
        # Форматируем вывод с dot знаками
        result = format(x, f'.{dot + 1}f')
        if int(result[-1]) >= 5:
            result = result[:-2] + str(int(result[-2]) + 1)
        else:
            result = result[:-1]
        return result

def sqrt_real_analytics(a, dot):
    if a < 0:
        return '±' + str(sqrt_real(a, dot)) + 'i'
    elif a == 0:
        return '0'
    else:
        return '±' + str(sqrt_real(a, dot)) 

def sqrt_complex(a, b, dot):
    r = Decimal(sqrt_real((a**2 + b**2), dot))
    
    re = Decimal(a) + r
    im = Decimal(-a) + r

    getcontext().prec = dot + 10

    re = Decimal(re) / Decimal(2)
    im = Decimal(im) / Decimal(2)

    re = Decimal(sqrt_real(re, dot))
    im = Decimal(sqrt_real(im, dot))

    if b < 0:
        return f'± ({re} - i * {im})'
    else:
        return f'± ({re} + i * {im})'

def num_type(a, dot):

    try:
        n = complex(a)
        
        if n.imag == 0:  
            if n.real == 0:
                return '0'
            else:                                              # если мнимая часть числа равна 0
                return sqrt_real_analytics(n.real, dot)                       # вещественное число
        else:                                                          # если мнимая часть числа не равна 0
            return sqrt_complex(n.real, n.imag, dot)                   # комплексное число
            
    except ValueError:
        g.show_input_error()
        return 

def answer(a,dot):
    a = a.replace('i', 'j', -1)
    a = a.replace(' ', '', -1)
    a = a.replace(',', '.', -1)
    dot = dot.replace(' ', '', -1)
    if dot.isdigit():
        if int(dot) >= 0:
            dot = int(dot)
            return num_type(a, dot)
        else:
            g.show_input_error()
            return
    elif dot=='':
        return num_type(a, 5)
    else:
        g.show_input_error()
        return