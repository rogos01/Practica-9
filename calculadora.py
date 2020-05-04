def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a -b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b == 0:
        print("error division sobre 0")
        return
    return a//b    

def division(a, b):
    if b == 0:
        print("error division sobre 0")
        return
    return a/b

def modulo(a, b):
    if b == 0:
        print("error division sobre 0")
        return
    return a%b

def potencia(a, b):
    return a**b

def main():
    print("ingresa los valores")
    x = int(input())
    y = int(input())

    print("1. sumar \n 2. restar \n 3. division entera")
    print("4. division \n 5. modulo \n 6. potencia \n 7. multiplicar")
    op = int(input())

    var = True
    var = False
    #&& ||  < > <=  >=  !=
    #and    or
#while True:
    if op == 1:
        print(sumar(x, y))
    elif op == 2:
        print(restar(x, y))           
    elif op == 3:
        print(div_entera(x, y))    
    elif op == 4:
        print(division(x, y))    
    elif op == 5:
        print(modulo(x, y))
    elif op == 6:
        print(potencia(x, y))
    elif op == 7:
        print(multiplicar(x, y))
    elif op == 8:
       # break    
    else:
        print("opcion no valida")

if __name__ == "__main__":      #si se ejecuta directamenete manda a llamar a main
    main()