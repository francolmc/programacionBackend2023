from calculadora import *

first_input_value = int(input("Ingrese un valor: "))
second_input_value = int(input("Ingrese otro valor: "))

print(f"El resultado de la suma es: {add_two_values(first_input_value, second_input_value)}")
print(f"El resultado de la resta es: {substract_two_values(first_input_value, second_input_value)}")
print(f"El resultado de la multiplicacion es: {multiply_two_value(first_input_value, second_input_value)}")
print(f"El resultado de la division es: {division_two_values(first_input_value, second_input_value)}")