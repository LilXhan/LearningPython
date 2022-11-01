"""
    Recibimos el siguiente código y proponga mejoras para obtener un código más limpio, legible y mantenible.

    Simplificar el siguiente código:

    def mostrar_mensaje(esta_corriendo, esta_bloqueando, esta_saltando):
    if not esta_corriendo:
        if not esta_bloqueando:
            if not esta_saltando:
                print("Drakarys")
            else:
                print("No puedo atacar mientras salto")
        else:
            print("No puedo atacar mientras bloqueo")
    else:
        print("No puedo atacar mientras corro")

    mostrar_mensaje(True, False, False)
    mostrar_mensaje(False, True, True)
    mostrar_mensaje(False, False, True)
"""

def show_message(is_running, is_blocked, is_jumping):
    if not is_running and not is_blocked and not is_jumping:
        print("Drakarys")
    elif is_running:
        print("can't attack while running")
    elif is_blocked:
        print("can't attack while blocking.")
    else:
        print("can't attack while jumping")


show_message(True, False, False)
show_message(False, True, True)
show_message(False, False, True)
