
print("Bem vindo ao jogo do fósforo!")

n1 = 21
jogador = int(input("Queres jogar em primeiro ou em segundo? 1 ou 2? "))
primeira_jogada = True

if jogador == 1:
    print("Então escolheste ser o primeiro! Bora lá")
elif jogador == 2:
    print("Então escolheste ser o segundo, Bora lá")

while n1 > 1:
    if jogador == 1:
        jogar = int(input("Escolha um número de 1 a 4! "))
        if jogar > n1 - 1:
            jogar = n1 - 1
        if jogar>4:
            jogar=4
        if jogar<1:
            jogar=1  
        n1 = n1 - jogar
        print(f"Número de fósforos restantes: {n1}")
        if n1 > 1:
            print("É a vez do computador")
            computador_jogada = (n1 - 1) % 5
            if computador_jogada == 0:
                computador_jogada = 1
            if computador_jogada > n1 - 1:
                computador_jogada = n1 - 1
            print(f"O Computador tirou {computador_jogada} fósforos!")    
            n1 = n1 - computador_jogada
            print(f"Número de fósforos restantes: {n1}")
            if n1 == 1:
                print("Perdeste o jogo!")
                break 
    elif jogador == 2:     #IMPOSSÍVEL O COMPUTADOR GANHAR QUANDO JOGA EM PRIMEIRO LUGAR E USO A ESTRATÉGIA VENCEDORA!!
        if primeira_jogada == True:
            n2 = 1
            print(f"O Computador tirou {n2} fósforos!")  
            n1 = n1 - n2
            print(f"Número de fósforos restantes: {n1}")
            primeira_jogada = False 
        else:
            jogar = int(input("Escolha um número de 1 a 4! "))
            if jogar > n1 - 1:
                jogar = n1 - 1    
            if jogar>4:
                jogar=4
            if jogar<1:
                jogar=1
            n1 = n1 - jogar
            if n1 == 1:
                print(f"Número de fósforos restantes: {n1}")
                print("O Computador perdeu!")
                break 
            print(f"Número de fósforos restantes: {n1}")
            if n1 > 1:
                print("É a vez do computador")
                computador_jogada = (n1 - 1) % 5
                if computador_jogada == 0:  
                    computador_jogada = 1
                if computador_jogada > n1 - 1:
                    computador_jogada = n1 - 1  
                print(f"O Computador tirou {computador_jogada} fósforos!")  
                n1 = n1 - computador_jogada
                print(f"Número de fósforos restantes: {n1}")
            if n1 == 1:
                print("Perdeste o jogo!")
                break
   