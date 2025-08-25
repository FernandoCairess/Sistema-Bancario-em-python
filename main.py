from funcionalidades import banco
from funcionalidades.empréstimo import emprestar
from funcionalidades.contas import contasPagar, verificarSaldo
from funcionalidades.homeBroker import graficoInvestimento
from funcionalidades.deposito import depositar

def mostrarExtrato():
    print("\nExtrato Bancário:")
    if not banco.extrato:
        print("Nenhuma operação registrada.")
    else:
        for item in banco.extrato:
            print("-", item)
    print("Saldo atual: R$ ", banco.saldo)

def menuDoCliente(opcao):
    if opcao == 1:
        print("Saldo: R$", banco.saldo)
    elif opcao == 2:
        if verificarSaldo():
            print("Analisando dados de ações históricas...")
            graficoInvestimento()
    elif opcao == 3:
        if verificarSaldo():
            print("Solicitando empréstimo...")
            emprestar()
    elif opcao == 4:
        if verificarSaldo():
            print("Acessando pagamento de contas...")
            contasPagar()
    elif opcao == 5:
        mostrarExtrato()
    elif opcao == 6:
        depositar()
    else:
        print("Número errado, tente novamente.")

print("-"*20)
print("Bem-vindo ao sistema bancário")

while True:
    print("-"*20)
    print("\nMenu do Cliente:\n")
    print(" 1. Consultar Saldo")
    print(" 2. Analisar dados de ações históricas")
    print(" 3. Solicitar um empréstimo")
    print(" 4. Pagar contas")
    print(" 5. Ver extrato bancário")
    print(" 6. Realizar depósito")
    print(" F. Encerrar sistema")

    entrada = input("\nO que deseja realizar? ")

    if entrada.upper() == "F":
        print("Encerrando sistema bancário. Até mais!")
        break

    if entrada.isdigit():
        opcao = int(entrada)
        menuDoCliente(opcao)
    else:
        print("Entrada inválida. Digite um número de 1 a 6 ou F para sair.")
