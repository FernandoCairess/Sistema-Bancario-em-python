from funcionalidades import banco

def contasPagar():
    conta = float(input("Digite o valor da conta que deseja pagar: "))
    banco.saldo -= conta
    banco.registrar_operacao("Pagamento de conta", -conta)
    print("Certo, seu novo saldo é de: R$ ", banco.saldo)
def verificarSaldo():
    if banco.saldo <= 0:
        print("Seu saldo está zerado ou negativo. Só é possível realizar depósitos.")
        return False
    return True