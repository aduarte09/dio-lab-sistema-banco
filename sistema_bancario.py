menu = '''
MENU
(1) Sacar
(2) Depositar
(3) Extrato
(0) Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = float(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Saque não realizado. Número máximo de saques excedido.")
        elif valor > (saldo + limite):
            print("Saque não realizado. Saldo insuficiente.")
        elif valor <=0:
            print("Saque não realizado. Valor inválido.")
        else:
            if valor <= saldo:
                saldo -= valor
            else:
                limite += (saldo - valor)
                saldo = 0
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.\n")

    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.\n")
        else:
            print("Depósito não realizado. Valor inválido.\n")
    
    elif opcao == 3:
        print("-- EXTRATO --\n")
        print("Não houve movimentações nesta conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("-------------\n")
    
    elif opcao == 0:
        print("Programa encerrado.\n")
        break
    
    else:
        print("Opção inválida.\n")