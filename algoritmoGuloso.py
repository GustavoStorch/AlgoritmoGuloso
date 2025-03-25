import json
import webbrowser

def carregar_dados(arquivo):
    """Carrega o grafo das cidades a partir de um JSON."""
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def encontrar_caminho_guloso(grafo, origem, destino):
    """Encontra um caminho viável usando uma abordagem gulosa, escolhendo o vizinho mais próximo."""
    
    if origem not in grafo or destino not in grafo:
        print(f"Erro: Cidade de origem '{origem}' ou destino '{destino}' não encontrada no mapa.")
        return None, None

    cidade_atual = origem
    caminho = [cidade_atual]
    visitadas = set()
    distancia_total = 0 

    while cidade_atual != destino:
        visitadas.add(cidade_atual)

        vizinhos_disponiveis = [cidade for cidade in grafo[cidade_atual] if cidade not in visitadas]

        if not vizinhos_disponiveis:
            print(f"Erro: Não há caminho de '{cidade_atual}' para '{destino}'!")
            print(f"Caminho percorrido até o momento: {' -> '.join(caminho)}")
            print(f"Distância percorrida até o erro: {distancia_total} km")
            return None, None

        vizinhos_disponiveis.sort(key=lambda cidade: grafo[cidade_atual][cidade])

        proxima_cidade = vizinhos_disponiveis[0]
        distancia_total += grafo[cidade_atual][proxima_cidade]  
        caminho.append(proxima_cidade)
        cidade_atual = proxima_cidade

    return caminho, distancia_total

def gerar_url_google_maps(caminho):
    """Gera uma URL do Google Maps com o caminho indicado."""
    base_url = "https://www.google.com/maps/dir/"
    caminho_url = "/".join(caminho)
    return base_url + caminho_url

grafo_cidades = carregar_dados("resources/cidadesSCDistâncias.json")

origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")

resultado, distancia = encontrar_caminho_guloso(grafo_cidades, origem, destino)

if resultado:
    print(f"Caminho encontrado: {' -> '.join(resultado)}")
    print(f"Distância total percorrida: {distancia} km")
    
    url_mapa = gerar_url_google_maps(resultado)
    print(f"Você pode ver o caminho no Google Maps clicando no link abaixo:")
    print(url_mapa)
    
    webbrowser.open(url_mapa)
else:
    print("Não foi possível encontrar um caminho.")
