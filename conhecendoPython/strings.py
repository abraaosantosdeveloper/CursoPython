curso = "pYtHon"

## Converte os caracteres minusculos para maiusculos

print(curso.upper())

## Quebra de linha

print()

## Converte os caracteres maiusculos para minusculos

print(curso.lower())

## Quebra de linha

print()

## Converte apenas o primeiro caractere para maiusculo e os demais para minusculos

print(curso.title())

## Quebra de linha

print()

## Segunda parte

curso = "   Python "

## Remover todos os espacos vazios

print(curso.strip())

## Quebra de linha

print()

## Remover os espacos vazios a direita

print(curso.rstrip())

## Quebra de linha

print()

## remover todos os espacos vazios a esquerda

print(curso.lstrip())

## Quebra de linha

print()

## Mesclar caracteres:

curso = "Python"

## Centraliza somado ao caractere especificado ate que atinja a quantidade de caracteres do argumento 1

print(curso.center(10, "#"))

## Quebra de linha

print()

## Adiciona caractere especificado

print(".".join(curso))

## Quebra de linha

print()

## Com iteracao

# It's easier to use the join method

for letra in curso:
    print(letra, end="-")
    
print()