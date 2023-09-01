from mayor import *

try:
    resultado = obtener_mayor([1, "2", 3])
    print(f"El valor mayor es: {resultado}")
except ListaInvalidaError as e:
    print(f"Error: {e}")