# 🚀 Algoritmos Gulosos para Busca de Caminhos entre Cidades

## 📌 Sobre o Projeto
Este projeto implementa algoritmos gulosos para encontrar caminhos entre duas cidades com base na menor distância. Ele utiliza um arquivo JSON contendo as distâncias entre as cidades e fornece ao usuário a melhor rota a ser seguida. O sistema possui duas abordagens diferentes:

1. **`algoritmoGuloso.py`**: Encontra o caminho entre a cidade de origem e a cidade de destino, escolhendo sempre a cidade mais próxima na iteração atual.
2. **`algoritmoGulosoMelhorCaminho.py`**: Calcula o melhor caminho possível, considerando a rota globalmente ótima, e não apenas a cidade vizinha mais próxima.

Ambos os algoritmos retornam:
- A sequência de cidades percorridas.
- A distância entre cada cidade.
- A distância total percorrida.
- Um link para visualizar a rota diretamente no Google Maps.

---

## 🏗 Estrutura do Projeto
O projeto é estruturado da seguinte forma:

```
/
├── resources/
│   ├── cidadesSCDistancias.json  # Arquivo JSON contendo as distâncias entre cidades
│
├── algoritmoGuloso.py  # Algoritmo guloso que busca sempre a cidade vizinha mais próxima
├── algoritmoGulosoMelhorCaminho.py  # Algoritmo guloso otimizado para o melhor caminho global
└── README.md  # Documentação do projeto
```

---

## 🔧 Como Executar
### 1️⃣ Requisitos
Para rodar o projeto, é necessário ter instalado:
- Python 3.x
- Bibliotecas padrão (`json`, `sys`, etc.)
- Biblioteca adicional para gerar links do Google Maps (caso necessário)

### 2️⃣ Execução
Para rodar o **algoritmo guloso básico**:
```bash
python algoritmoGuloso.py
```
Para rodar o **algoritmo guloso que encontra o melhor caminho**:
```bash
python algoritmoGulosoMelhorCaminho.py
```
O programa solicitará ao usuário que informe:
1. Cidade de Origem
2. Cidade de Destino

Após a entrada, o programa processará a melhor rota e exibirá os resultados.

---

## 📂 Sobre o Arquivo JSON
O arquivo `cidadesSCDistancias.json` contém os dados de distâncias entre as cidades no seguinte formato:
```json
{
    "Jaraguá do Sul": {
        "Corupá": 21,
        "Guaramirim": 7,
        "Joinville": 18,
        "Pomerode": 14,
        "Schroeder": 25
    },
    "Jardinópolis": {
        "Cordilheira Alta": 22,
        "Faxinal dos Guedes": 18,
        "Xaxim": 20
    },
}
```
Cada cidade é um nó, e as conexões representam as distâncias entre elas.

---

## 📌 Conclusão
Este projeto demonstra como algoritmos gulosos podem ser aplicados na busca por caminhos entre cidades. Ele oferece duas abordagens distintas para resolver o problema, permitindo uma comparação entre um método baseado apenas na escolha do vizinho mais próximo e um que busca um caminho globalmente melhor.

📩 Sinta-se à vontade para contribuir, reportar problemas ou sugerir melhorias!

