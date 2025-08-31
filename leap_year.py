def leap_year():
    year = int(input("Ingrese un año: "))

    isLeapYear = year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)

    if (isLeapYear):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")