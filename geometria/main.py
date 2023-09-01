import matematicas.algebra
import matematicas.geometria

valor_a = float(input("Ingrese un valor para a: "))
valor_b = float(input("Ingrese un valor para b: "))
valor_c = float(input("Ingrese un valor para c: "))

solucion_1 = matematicas.algebra.resolver_ecuacion(valor_a, valor_b, valor_c)
print(f"La solucion para la ecuacion de segundo grando es: {solucion_1}")

valor_base = float(input("Ingrese un valor para la base del triangulo: "))
valor_altura = float(input("Ingrese un valor para la altura del triangulo: "))
solucion_2 = matematicas.geometria.calcular_area_triangulo(valor_base, valor_altura)
print(f"La solucion para el area del triangulo es: {solucion_2}")