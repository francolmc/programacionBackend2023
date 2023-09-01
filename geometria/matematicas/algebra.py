import math

def resolver_ecuacion(a: float, b: float, c: float) -> float:
    if a == 0:
        if b == 0:
            return None
        else:
            return (-c/b,)
    else:
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return None
        elif discriminante == 0:
            return (-b/(2*a),)
        else:
            x1 = (-b + math.sqrt(discriminante))/(2*a)
            x2 = (-b - math.sqrt(discriminante))/(2*a)
            return (x1, x2)