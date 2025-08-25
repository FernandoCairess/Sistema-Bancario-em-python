from datetime import datetime
from funcionalidades import banco


def emprestar():
    print("\n Para realizar o empréstimo, o valor das parcelas deve ser inferior a 35% do seu saldo atual.\n Além disso, o banco cobra 12% de juros ao ano")

    valordesejado = float(input("Qual valor você deseja emprestado? "))
    qntprestacoes = int(input("Em quantas prestações mensais deseja pagar? "))

    taxa_juros_anual = 0.12
    tempo_em_anos = qntprestacoes / 12
    valor_total_com_juros = valordesejado * (1 + taxa_juros_anual * tempo_em_anos)
    valor_parcela = valor_total_com_juros / qntprestacoes
    limite = 0.35 * banco.saldo

    if valor_parcela > limite:
        print("Empréstimo negado. O valor das parcelas excede 35% do seu saldo.")
    else:
        banco.saldo += valordesejado
        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        banco.extrato.append(
            f"{data} | Empréstimo aprovado: R$ {valordesejado:.2f} em {qntprestacoes}x de R$ {valor_parcela:.2f} | Total com juros: R$ {valor_total_com_juros:.2f} | Saldo: R$ {banco.saldo:.2f}"
        )

        print(f"\nEmpréstimo de R$ {valordesejado:.2f} aprovado!")
        print(f"Serão {qntprestacoes} parcelas de R$ {valor_parcela:.2f}")
        print(f"Valor total da dívida com juros: R$ {valor_total_com_juros:.2f}")
        print(f"Novo saldo: R$ {banco.saldo:.2f}")
