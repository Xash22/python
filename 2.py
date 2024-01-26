def vocal_O_simbolo_del_alfabeto(letra):
    if letra in("a","e","i","o","u"):
        return (f "{letra}es una vocal")
    else:
        return(f "{letra}es un simbolo del alfabeto")
l= input("escriba una letra cualquiera")
print(vocal_O_simbolo_del_alfabeto(l))