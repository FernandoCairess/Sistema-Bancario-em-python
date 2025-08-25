import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

hoje = datetime.today()
data_formatada = hoje.strftime("20%y-%m-%d")
def graficoInvestimento():
    data1=str(input("Digite a data que irá começar a análise dos dados históricos (ano-mes-dia): "))
    pergunta = []
    while True:
        entrada = input("Digite o nome da ação que deseja realizar a consulta, caso queira encerrar aperte enter: ")
        if entrada == "":
            break
        pergunta.append(entrada)

    # Adiciona o sufixo ".SA" para cada ticker
    tickers = [ticker + ".SA" for ticker in pergunta]

    # Deixa os dados ajustados
    dados = yf.download(tickers, start=data1, end=data_formatada)["Close"]

    # Plota os gráficos
    plt.figure(figsize=(12,6))
    for acao in dados.columns:
        plt.plot(dados.index, dados[acao], label=acao)

    plt.title("Histórico de Preços (Ajustados)")
    plt.xlabel("Data")
    plt.ylabel("Preço (BRL)")
    plt.legend()
    plt.grid(True)
    plt.show()

