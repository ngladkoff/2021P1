# Clase 2
"""
print("hola mundo".replace("mundo", "UADE"))
print("hola mundo".replace("mundo", '"  \''))

print("hola mundo".title())

texto = "Nicolas<#>Gladkoff<#>ngladkoff@uade.edu.ar"
persona= texto.split('<#>')
print(persona)
print(persona[1])
#texto2= "=".join(persona)
#print(texto2)
print("=".join(persona))
"""

texto = "Nicolas<#>Gladkoff<#>ngladkoff@uade.edu.ar"

#persona= texto.split('<#>')

# print("Nombre: ", persona[0])
# print("Nombre: {0}, Apellido: {1}".format(persona[0], persona[1]))

# print(texto[0])

vocales = ['a', 'e', 'i', 'o', 'u']
print(texto)
for i in range(0,len(texto)):
    if texto[i] in vocales:
        print(texto[i], end='')

for letra in texto:
    print(letra + "|", end="")
