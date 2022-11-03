"""
    Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo 
    dígito más alto por el cuál es divisible. Por ejemplo para 328 es 8.
"""

def div(min, max):
    dict = {}
    numbers = [i for i in range(min, max)]
    for num in numbers:
        max_div = 0
        for digit in str(num):
            digit = int(digit)
            if digit == 0: continue
            if num % digit == 0 and digit > max_div:
                max_div = digit
                dict[num] = digit
    return dict


result = div(10, 500)

print(result)
