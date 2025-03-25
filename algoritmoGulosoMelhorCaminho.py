import json
import heapq
import webbrowser

def carregar_dados(arquivo):
    """Carrega o grafo das cidades a partir de um JSON."""
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def encontrar_melhor_caminho_dijkstra(grafo, origem, destino):
    """Encontra o caminho mais curto usando o algoritmo de Dijkstra."""
    
    if origem not in grafo or destino not in grafo:
        print(f"Erro: Cidade de origem '{origem}' ou destino '{destino}' não encontrada no mapa.")
        return None, None

    fila_prioridade = [(0, origem, [])]  
    visitados = set()

    while fila_prioridade:
        distancia_atual, cidade_atual, caminho = heapq.heappop(fila_prioridade)

        if cidade_atual in visitados:
            continue

        caminho = caminho + [cidade_atual]
        visitados.add(cidade_atual)

        if cidade_atual == destino:
            return caminho, distancia_atual

        for vizinho, distancia in grafo[cidade_atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (distancia_atual + distancia, vizinho, caminho))

    print(f"Erro: Não há caminho de '{origem}' para '{destino}'!")
    return None, None

def gerar_url_google_maps(caminho):
    """Gera uma URL do Google Maps com o caminho indicado."""
    base_url = "https://www.google.com/maps/dir/"
    caminho_url = "/".join(caminho)
    return base_url + caminho_url

grafo_cidades = carregar_dados("resources/cidadesSCDistâncias.json")

origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")

resultado, distancia = encontrar_melhor_caminho_dijkstra(grafo_cidades, origem, destino)

if resultado:
    print(f"Melhor caminho encontrado: {' -> '.join(resultado)}")
    print(f"Distância total percorrida: {distancia} km")
    
    url_mapa = gerar_url_google_maps(resultado)
    print(f"Você pode ver o caminho no Google Maps clicando no link abaixo:")
    print(url_mapa)
    
    webbrowser.open(url_mapa)
else:
    print("Não foi possível encontrar um caminho.")
