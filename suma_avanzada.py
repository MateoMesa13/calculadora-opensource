def suma_avanzada(arr):
    try:
        return sum(arr)
    except TypeError:
        raise TypeError("Algo salió mal, asegúrate de que el argumento sea una lista de números.")