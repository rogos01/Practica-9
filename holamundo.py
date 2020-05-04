#Esto es un comentario de una sola linea


#c es un lenguaje compilado y una vez compiladonp depende del compilador y python es interpretado
# no se usa ; y los comentarios cambian
#las variables no se declaran

print("hola mundo")
x=10
print(type(x))
print(x)
x=y=z=2.3
print(x,y,z)
print(type(x))
x="cadena"
print(type(x))

c1 = "hola"
c2 = "rodrigo"
saludo = c1 + " " + c2
print(saludo)

saludo2 = "{} {} {}".format(c1, c2, 3)
print(saludo2)
#las llaves representan un valor 

saludo3 = "cambio de orden {1} {2} {0}".format(c1, c2, 3)
print(saludo3)
#se empieza desde 0    0, 1 y 2


