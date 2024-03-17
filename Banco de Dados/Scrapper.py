## Tarefa 2 - Banco de Dados - PPGTI 2024.1

# Questão 3: Crie um Scraper para ler os dados dos docentes da página do PPGTI (https://www.ifpb.edu.br/ppgti/programa/corpo-docente) - construa um dataframe que liste o nome, linha de pesquisa, url do lattes e e-mail de cada professor (4,0)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.ifpb.edu.br/ppgti/programa/corpo-docente"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find('div', {'id': 'parent-fieldname-text'}) # Encontrando a div com o id "parent-fieldname-text":

nomes = []
linhas_de_pesquisa = []
urls_lattes = []
emails = []

# Encontra todos os itens h4 dentro da div declarada na linha 15
for item in div.find_all('h4'):
    # Verifica se o item h4 não está vazio, porque tem alguns h4 vazio no codigo fonte e ficava salvo no df
    if item.text.strip() != '':

        # Nome do docente
        nome = item.text.strip()
        nomes.append(nome)
        
        # Linha de pesquisa (sempre que puxava próximo "p" vinha com o nome "curriculo lattes" junto, então to tirando com um replace)
        linha_de_pesquisa = item.find_next_sibling('p').text.strip().split(':')[1]
        linha_de_pesquisa = linha_de_pesquisa.replace("Currículo Lattes", "").strip()
        linhas_de_pesquisa.append(linha_de_pesquisa)
        
        # Lattes (encontra o próximo elemento a dentro do p. Alguns tão como external link, outros não... assim foi como conseguir puxar todos da lista)
        url_lattes = item.find_next_sibling('p').find('a')['href']
        urls_lattes.append(url_lattes)
        
        # E-mail (encontrando o próximo item e puxando o item 4 no split)
        email = item.find_next_sibling('p').text.strip().split(':')[4]
        emails.append(email)


# Criando o DataFrame com os dados coletados
docentes = pd.DataFrame({
    'Nome': nomes,
    'Linha de Pesquisa': linhas_de_pesquisa,
    'Lattes': urls_lattes,
    'Email': emails
})

print(docentes)

docentes.to_csv('Docentes.csv', index=False)
