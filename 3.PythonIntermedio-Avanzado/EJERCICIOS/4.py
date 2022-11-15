def type_number(func_calc):
    def find_type(n):
        result = func_calc(n)
        if result:
            return 'Es par'
        return 'Es impar'

    return find_type


@type_number
def calc_par_impar(n):
    if n % 2 == 0:
        return True
    return False

result = calc_par_impar(13)
print(result)