import random

def listar(cinema):
    for c in cinema:
        print(f"Filme em exibição: {c[2]}")

def disponivel(cinema,filme,lugar):
    cond=False
    for g in cinema:
        if g[2]==filme:
            if lugar not in g[1]:
                cond=True
    return cond

def vendebilhete(cinema,filme,lugar):
    for h in cinema:
        if h[2]==filme:
            if lugar not in h[1]:
                h[1].append(lugar)
    return cinema 

def listardisponibilidades(cinema):
    for j in cinema:
        lugares=j[0]
        vendidos=len(j[1])
        filme=j[2]
        disponiveis=lugares-vendidos
        print(f"Filme em exibição: {filme} :: {disponiveis} Lugares disponíveis:: {vendidos} bilhetes vendidos")

def inserirsala(cinema,lugares,filme):
    sala = (lugares, [], filme) 
    cinema.append(sala)
    return cinema

def retirarlugar(cinema,filme,lugar):
    for c in cinema:
        if c[2]==filme:
            if lugar in c[1]:
                c[1].remove(lugar)
    return cinema 

def menu():
    print(""" 
    (1) Ver lugar disponível
    (2) Filmes em exibição
    (3) Comprar bilhete
    (4) Ver salas de cinema 
    (5) Inserir sala cinema 
    (6) Retirar lugar
    ...
    (0) Sair
    """)

def cinema():
    cinema22=[]
    inserirsala(cinema22,100,"Oppenheimer")
    inserirsala(cinema22,100,"Interstellar")
    inserirsala(cinema22,100,"Barbie")
    inserirsala(cinema22,100,"Saw IV")
    
    condi=True
    while condi:
        menu()
        decisão=int(input("Indica qual a opção que desejas?"))
        if decisão==1:
            filme=str(input("Que filme desejas ver?"))
            lugar=int(input("Qual o lugar que estás à procura?"))
            if disponivel(cinema22,filme,lugar):
                print(f"Lugar {lugar} está disponível para {filme}!")
            else:
                print(f"Lugar {lugar} NÃO está disponível para {filme}!")
                
        if decisão==2:
            listar(cinema22)
            
        if decisão==3:
            lugare=random.randint(1,100)
            filme=str(input("Que filme desejas ver?"))
            cinema22 = vendebilhete(cinema22,filme,lugare)
            print(f"Ficaste no lugar {lugare}!. Bom filme :)")
            
        if decisão==4:
            listardisponibilidades(cinema22)
            
        if decisão==5:
            ol=int(input("Quantos lugares tem a sala?"))
            al=str(input("Qual o nome do filme em exibição?"))
            cinema22 = inserirsala(cinema22,ol,al)
            print(f"Sala para {al} com {ol} lugares adicionada!")
            
        if decisão==6:
            filme=str(input("Que filme desejas ver?"))
            lugares=int(input("Qual o lugar em causa?"))
            cinema22 = retirarlugar(cinema22,filme,lugares)
            print(f"Lugar {lugares} removido de {filme}!")
            
        if decisão==0:
            print("Obrigado!")
            condi=False

cinema()