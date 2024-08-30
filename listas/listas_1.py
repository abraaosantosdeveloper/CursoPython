## Listas

frutas = ["Laranja", "maçã", "uva", "banana"]
## print(frutas)
print(frutas[-1])
print(frutas[0])
print(frutas[2])

## lista vazia

frutas_vazia = []
print(frutas_vazia)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

## Matriz com listas aninhadas

matriz = [
    [1, 2, 3],
    ["c", 5, 6],
    [7, 8, "t"]
]

print(matriz)

## Fatiamento

lista = ["p","y","t","h","o","n"]

print(lista[2:])

print(lista[:2])

print(lista[1:3])

print(lista[0:3:2])

print(lista[::])

print(lista[::-1])


carros = ["Gol", "Fox", "Celta", "Omega"]

for carro in carros:
    print(carro)


## Com enumerate:

for indice, carro in enumerate(carros):
    print(f"{indice + 1}: {carro}") ## Foi adicionado o + 1 porque os índices iniciam sempre em 0(zero)


## Filtros:

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

## comprehention

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(f" Com o comprehention: {pares}")