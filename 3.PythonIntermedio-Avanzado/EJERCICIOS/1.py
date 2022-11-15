def show_msg_avg(func_avg):
    def return_avg():
        print("Inicio del calculo del promedio de lista de números")
        promedio = func_avg()
        print(f"El promedio es: {promedio}")
        print("El calculo a finalizado")
    return return_avg


@show_msg_avg
def get_avg() -> float:
    lista = [10, 40, 20, 45, 25, 35, 15]
    promedio = sum(lista) / len(lista)
    return promedio

get_avg()

