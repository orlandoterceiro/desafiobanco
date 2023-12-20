saldo = 0  
limite_diario = 500
saques_realizados = 0

while True:
    print("\nMENU:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Verificar Saldo")
    print("4. Sair")

    escolha = input("Escolha uma opção (1, 2, 3, 4): ")

    if escolha == "1":
        deposito = float(input("Digite o valor do depósito: ").replace(",", "."))
        saldo += deposito
        print(f"Depósito de R$ {deposito:.2f} realizado. Saldo total: R$ {saldo:.2f}")

    elif escolha == "2":
        saque = float(input("Digite o valor do saque: ").replace(",", "."))
        if saque > saldo:
            print("Saldo insuficiente. Operação de saque cancelada.")
        elif (saques_realizados + saque) > limite_diario:
            limite_disponivel = limite_diario - saques_realizados
            print(f"Limite diário de saque excedido. Você pode sacar até R$ {limite_disponivel:.2f} ainda.")
        else:
            saldo -= saque
            saques_realizados += saque
            print(f"Saque de R$ {saque:.2f} realizado. Saldo total: R$ {saldo:.2f}")

    elif escolha == "3":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif escolha == "4":
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
