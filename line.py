import math

def line():
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el coeficiente X1: "))
    x2 = float(input("Ingrese el coeficiente X2: "))
    y1 = a * x1 + b
    y2 = a * x2 + b

    print(f"El coeficiente A de su ecuación de la recta es: {a}")
    print(f"El coeficiente B de su ecuación de la recta es: {b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print(f"\nPara la siguiente ecuación:\n\tY = {a}X + {b}\n")
    print(f"Dados los siguientes puntos:\n\tP1 ({x1}, {y1})\n\tP2 ({x2}, {y2})\n")

    # https://es.wikipedia.org/wiki/Distancia#Distancia_de_dos_puntos_en_el_plano
    # d(ab) = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    # https://www.w3schools.com/python/module_math.asp
    # math.pow() math.sqrt()
    print(f"La distancia entre ellos es: {math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))}")