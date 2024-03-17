## Tarefa 2 - Banco de Dados - PPGTI 2024.1

# Questão 2: Crie um script para consumir dados da API do IBGE para listar os nomes das cidades de um estado específico (3,0)

import requests
import pandas as pd

while True:
    try:
        estado = input("Digite a sigla do estado que deseja visualizar as cidades (ex.: PB; PA; SP): ").upper()
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/distritos"
        response = requests.request("GET", url)
        resultado = pd.DataFrame(response.json())

        lista_cidades = resultado['nome']

        print(f"Lista de cidades do estado {estado}: \n{lista_cidades.to_string(index=False)}")
        break 
    except KeyError: 
        print(f"\nEstado inválido. Por favor, tente novamente.\n")