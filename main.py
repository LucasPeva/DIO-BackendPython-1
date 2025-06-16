menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

> """

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("\nBem vindo ao sistema de controle bancário!")

while True:
    opcao = input(menu)
    
    if opcao.lower().strip() == "d":
        
        print("Operação: Depósito\n")
        
        try:
            deposito = float(input("Quanto deseja depositar?\n> "))
            
            if deposito <= 0:
                print("ERRO: Você deve depositar um valor maior que 0!")
                
            else:
                print(f"Depositado {deposito} na conta bancária.\n")
                saldo += deposito.__round__(2)
                extrato += f"Depósito feito no valor de R${deposito:.2f}.\n"
                print(f"Novo saldo da conta: {saldo}")
                
        except ValueError:
            print("ERRO: Valor inválido inserido. Tente novamente")            
    
    
    elif opcao.lower().strip() == "s":
        
        print("Operação: Saque\n")
        
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário atingido!")
            
        else:
            try:
                print(f"Seu saldo atual é: {saldo}\n")
                saque = float(input("Quando deseja sacar?\n> "))
                
                if saque > saldo:
                    print("ERRO: Valor de saque maior que saldo disponível!")
                    
                elif saque > 500.0:
                    print("ERRO: Valor de saque maior que limite!")
                    
                else:
                    numero_saques += 1
                    saldo -= saque.__round__(2)
                    extrato += f"Saque feito no valor de R${saque:.2f}.\n"
                    print(f"Novo saldo da conta: {saldo}")
            except ValueError:
                print("ERRO: Valor inválido inserido. Tente novamente")
        
    elif opcao.lower().strip() == "e":
        
        print("Operação: Extrato\n")
        
        print(extrato)
        print(f"Saldo: {saldo:.2f}")
        
    elif opcao.lower().strip() == "q":
        break
    
    else:
        print("Opção inválida.")