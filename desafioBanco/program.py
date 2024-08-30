## Deve obedecer o limite de 3 saques diários
## Deve regitrar todas as movimentações no extrato
## Não deve receber valores negativos no depósito
## Valores devem ser exibidos no formato R$ xxxx.xx

menu = '''
===============MENU===============

            Bem vindo!
           
escolha uma opção:

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

==================================
'''

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

## Condicional para validar operações

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor_saque = float(input("Digite o valor do saque: "))

        if valor_saque > saldo:
            print("Saldo insuficiente!")

        elif valor_saque < 0:
            print("Valor inválido!")
        
        elif valor_saque > limite:
            print("O valor do saque excede o limite...")

        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Limite de saques excedido!")
                numero_saques -= 1
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n "
                print("Saque realizado com sucesso!")
                print(f"Seu saldo atual é de R$ {saldo}")

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito <= 0:
            print("Valor inválido!")
        else:
            print("Depósito realizado com sucesso!")
            saldo += valor_deposito
            extrato += f" Depósito: R$ {valor_deposito:.2f}\n "
            print(f"Seu saldo atual é de R$ {saldo}")

    elif opcao == 3:
        print('\n===============Extrato===============')

        print("Não foram registradas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual é de R$ {saldo}")

        print('=====================================')

    
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Opção inválida! Tente novamente.")




def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f" Depósito: R$ {valor:.2f}\n "
        print("Depósito realizado com sucesso!")
        print(f"Seu saldo atual é de R$ {saldo}")
    else:
        print("\nFalha na operação! O valor informado é inválodo!")

    return saldo, extrato