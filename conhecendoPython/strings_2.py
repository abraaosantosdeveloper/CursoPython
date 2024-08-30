nome = "Abraão"
idade = 20
profissao  ="Programador"
linguagem = "Python"


## Interpolação com:

## Método "Old Style"(%):

print("Meu nome é %s, tenho %d anos, sou %s e programo em %s" % (nome, idade, profissao, linguagem))

## Método Format:

print("Meu nome é {}, tenho {} anos, sou {} e programo em {}".format(nome, idade, profissao, linguagem))
## passando os indices:

print("Meu nome é {1}, tenho {0} anos, sou {2} e programo em {3}".format(idade, nome, profissao, linguagem))

## Utilizando nomenclaturas:
print("Meu nome é {nome}, tenho {idade} anos, sou {profissao} e programo em {linguagem}".format(idade=idade, nome=nome, profissao=profissao, linguagem=linguagem))

## Utilizando dicionário:

dados = {"nome": "Abraão", "idade": 20}

print("Nome: {nome}. Idade: {idade}".format(**dados))

## Método f-string:

# Bem mais fácil e limpo!!!

print(f"Meu nome é {nome}, tenho {idade} anos, sou {profissao} e programo em {linguagem}")


## Formatação de strings com f-string

PI = 3.14159

print(f"O valor de PI é {PI: .2f}")