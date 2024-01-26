def valor_futuro(vp,i,n):
    return vp * (1+i)**n

valor_presente = 100
interes = 3.5
periodos = 7
print(valor_futuro(valor_presente,interes/100,periodo))