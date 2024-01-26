def suma(a,c):
    suma1 = a+c
    print(suma1)

suma(c=5,a=10)
suma(8,46)

def minimo(num1,num2,num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        print("uno de los numero es igual a otro")
    elif num1 < num2:
        if num1 < num3:
            print(f"este es el menor {num1}")
    elif num2 < num3:
        print(f"este es menor {num2}")
    elif num3 < num1:
        print(f"este es menor {num3}")

minimo(5,5,4)
minimo(15,12,13)
