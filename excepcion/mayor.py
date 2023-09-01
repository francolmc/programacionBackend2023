class ListaInvalidaError(Exception):
    pass

def obtener_mayor(lista: list) -> None | int:
    mayor = None
    for elemento in lista:
        if not isinstance(elemento, int):
            raise ListaInvalidaError("La lista contiene elementos no son numeros.")
        if mayor is None or elemento > mayor:
            mayor = elemento
    return mayor