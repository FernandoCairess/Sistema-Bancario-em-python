from funcionalidades import banco


def depositar():
    valor = float(input("Digite o valor que deseja depositar: "))
    if valor <= 0:
        print("Valor inválido. Depósito precisa ser maior que zero.")
    else:
        banco.saldo += valor
        banco.registrar_operacao("Depósito", valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {banco.saldo:.2f}")