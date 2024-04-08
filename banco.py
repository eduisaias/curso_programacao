menu = """ Olá bem vindo ao Banco 100% 
            Digite a opção desejada
            
            Menu

            [e] - Extrato
            [s] - Saque
            [d] - Depositar
            [q] - Sair
 
 """

print(menu)
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo += valor
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito : R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido.")

    
    elif opcao == "s": 
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_Saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é inválido")
      
    elif opcao == "e":
        print("\n ================= Extrato ================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo: R$: {saldo:.2f}")
        print("=============================================")


    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")