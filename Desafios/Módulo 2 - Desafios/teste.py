import requests
from bs4 import BeautifulSoup

# Função para extrair o número de escanteios de uma partida
def extrair_escanteios(url):
    # Faz a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    if response.status_code == 200:
        # Cria um objeto BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra o elemento HTML que contém o número de escanteios
        elemento_escanteios = soup.find('div', class_='js-event-details-statistics')

        if elemento_escanteios:
            # Extrai o número de escanteios da partida
            numero_escanteios = elemento_escanteios.find_all('span', class_='js-stat-value')[1].text.strip()
            return int(numero_escanteios)

    return None

# URL da partida
url_partida = "https://www.sofascore.com/pt/saint-louis-city-sc-la-galaxy" pelo nome correto da partida

# Extrai o número de escanteios da partida
numero_escanteios = extrair_escanteios(url_partida)

if numero_escanteios is not None:
    print("Número de escanteios:", numero_escanteios)
else:
    print("Não foi possível obter o número de escanteios da partida.")
