# todo: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):

    baixo_consumo = consumo <= 10
    consumo_medio = consumo > 10 and consumo <= 20
    consumo_alto = consumo > 20

    plano_essencial = "Plano Essencial Fibra - 50Mbps"
    plano_prata = "Plano Prata Fibra - 100Mbps"
    plano_premium = "Plano Premium Fibra - 300Mbps"
# todo: Crie uma Estrutura Condicional para verifica o consumo médio mensal 


    if baixo_consumo:
        return plano_essencial
    
    elif consumo_medio:
        return plano_prata
    
    elif consumo_alto:
        return plano_premium
    
# todo: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))