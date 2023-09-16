saldo = 0
LIMITE_SAQUE_DIARIO = 3
extrato = ""
saques = 0
LIMITE_SAQUE = 500
#lista_deposito = []
#lista_saque = []
valor_depositado = 0




while True:
    menu = """
Selecione a operação que gostaria de executar?

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
--=> """
    opcao = input(menu)

    if opcao == "d":
        while True:
            try:
                valor = float(input("Deposito no valor de: "))
                if valor > 0:                    
                    extrato += (f"\n Depósito de R${valor:.2f}")
#                   lista_deposito(valor)
                    saldo += valor
                    valor_depositado += valor                    
                    menuD = """
Deseja depositar novamente?
[s]Sim
[n]Não
-=> """
                    opcaoD = input(menuD)
                    if opcaoD == "s":        
                        print(f"Total depositado de {valor_depositado}")                
                        continue  # Continua depositando
                    elif opcaoD == "n":
                        print(f"Total depositado de {valor_depositado}") 
                        valor_depositado = 0
                        print(f"Saldo total de {saldo}")
                        break
                    else:
                         print("Opção inválida. Retornando a tela principal.")
                         print(f"Total depositado de {valor_depositado}") 
                         valor_depositado = 0
                         break
                else:
                    print("Este sistema não pode depositar um valor negativo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Certifique-se de depositar um valor positivo.")
            
    elif opcao == "s":
        print(f"Seu valor em conta é de {saldo}")
        while True:
            try:
                valor_saque = float(input("Saque no valor de: "))
                if valor_saque > 0 and saques < LIMITE_SAQUE_DIARIO and valor_saque <= LIMITE_SAQUE and valor_saque <= saldo:
                    saldo -= valor_saque
                    saques += 1
 #                   lista_saque.append(valor_saque)
                    extrato += (f"\n Saque de R${valor_saque:.2f}")
                    print(f"Saque de {valor_saque} realizado com sucesso.")
                elif saques == LIMITE_SAQUE_DIARIO:
                    print("""Você atingiu o limite diário de saques.
Encerrando operação de saque.""")
                    break
                elif valor_saque > LIMITE_SAQUE:
                    print(f'O valor do saque excede o limite diário de {LIMITE_SAQUE}.')
                elif valor_saque > saldo:
                    print("Saldo insuficiente para o saque.")
                else:
                    print("Não é possível sacar um valor nulo ou negativo.")
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir um valor válido.")
            menuS = """
Deseja sacar novamente?
[s]Sim
[n[Não
-=>]"""
            optionS = input(menuS)
            if optionS == "s":
                print(f"Seu saldo agora é {saldo}")
                continue
            elif optionS == "n":
                print(f"Seu saldo agora é {saldo}")
                break
            else:
                print("Opção inválida. Retornando a tela principal.")
                valor_depositado = 0
                break


            

    elif opcao == "e":
        print("\n======================EXTRATO===================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo R${saldo:.2f}")
        print("==================================================")
# IMPLEMENTAR EXTRATO UNICO SAQUES/DEPOSITOS
 #       for valores in lista_deposito:
 #           print(f"Foram depositados os seguintes valores: R${valores:.2f}")
 #       for valores in lista_saque:
 #           print(f"Saque R${valores:.2f}")
 #       print(f"Seu saldo final em conta é de R${saldo}")
              
    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços")
        break  # Sai do loop principal e encerra o programa
    else:
        print("Opção inválida. Selecione uma opção válida.")