'''
## Before the backslash: Positional Only
## After the asterisk: Keword only

#The function below means that every argument in the function that is before the backslash is considered
#a positional argument, not a keyword argument. In addition, every argument in the function that
#is after the asterisk is considered a positional argument. Be careful when using. 
#You can change the position of the arguments and cause issues.

def message(texto, /, *, nome ):
    print(f"{texto} {nome}")

message('Bem vindo, ', nome='Abraão')

## Arguments and keyword arguments
## Every argument in the function that is after the asterisk is considered a positional argument only.
## Every argument in the function that is after the double asterisk is considered a keyword only argument.

def arg_karg(*args, **kwargs):
    print(args)
    print(kwargs)

arg_karg(1, 2, 3, 'Fim dos Argumentos não nomeados', nome='Abraão', idade=20, sobrenome="Santos", mensagem="Fim dos Argumentos nomeados")


## Join Method

tupla = ('Abraão', '20', 'Brasileiro')

print(' | '.join(tupla))
'''

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("12 de junho de 2024", "Zen of Python", "Beautiful is better than ugly.", "Some another text.", author="Tim Peters", Year=1999 )





