import os

variavel1 = "Hello, world!"

print(variavel1)

os.system("pause")  # Para não fechar a janela do Python após a execução do código


letraSelecionada = input("Informe a letra a ser substituida: ")
letraAlterada = input("Informe a letra que substituirá a letra informada: ")

print(variavel1.replace(letraSelecionada, letraAlterada))

