MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade.') 
elif idade == IDADE_ESPECIAL:
    print('Idade especial')
elif idade < MAIOR_IDADE:
    print('Você é menor de idade')
else:
    print('Idade inválida')


## Estrutura condicional ternaria

saldo = 200
saque = float(input(f'Qual o valor do saque? \nSeu saldo: {saldo}. \n->'))

status = 'sucesso' if saldo >= saque else 'falha'

print(f'{status} ao realizar o saque. Saldo atual: {saldo - saque}')
