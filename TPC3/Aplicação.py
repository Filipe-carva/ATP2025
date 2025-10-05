import random
def opcao1():
    res=[]
    n=random.randint(1,30)
    while n>0:
        res.append(random.randint(1,100))
        n=n-1
    return res

def opcao2():
    res=[]
    print("------------------------------------")
    n1=int(input("Qual o tamanho da tua lista?"))
    print("------------------------------------")
    while n1>0:
        num=int(input("Que número queres adicionar?"))
        print("------------------------------------")
        res.append(num)
        n1=n1-1
    return res

def opcao3(lista):
    soma=0
    for n in lista:
        soma=soma+n
    return soma

def opcao4(lista):
    if len(lista)==0:
        return 0
    soma=opcao3(lista)
    média=soma/len(lista)
    return média

def opcao5(lista):
    n5=lista[0]
    for n in lista[1:]:
        if n5<n:
            n5=n
    print("------------------------------------")
    print(f"O maior número da tua lista é: {n5}")

def opcao6(lista):
    n6=lista[0]
    for n in lista[1:]:
        if n6>n:
            n6=n
    print("------------------------------------")
    print(f"O menor número da tua lista é: {n6}")

def opcao7(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            print("------------------------------------")
            print("A tua lista não está por ordem crescente!")
            return
    print("------------------------------------")
    print("A tua lista está por ordem crescente!")

def opcao8(lista):
    for i in range(len(lista)-1):
        if lista[i]<lista[i+1]:
            print("------------------------------------")
            print("A tua lista não está por ordem decrescente!")
            return
    print("------------------------------------")
    print("A tua lista está por ordem decrescente!")
        
def opcao9(lista):
    print("------------------------------------")
    elem=int(input("Que elemento queres procurar?"))
    for i in range(len(lista)):
        if lista[i]==elem:
            print("------------------------------------")
            print(f"Está na posição {i}")
            return
    print("------------------------------------")
    print(-1)

def opcao0():
    print("------------------------------------")
    print("Aplicação encerrada")
    print("------------------------------------")

def menu():
   print("------------------------------------")
   print("Bem vindo!")
   print("""
    * (1) Criar Lista 
    * (2) Ler Lista
    * (3) Soma
    * (4) Média
    * (5) Maior
    * (6) Menor
    * (7) estaOrdenada por ordem crescente
    * (8) estaOrdenada por ordem decrescente
    * (9) Procura um elemento
    * (0) Sair""")

   
def jogo():
    primeira_vez=True
    lista=[]
    while True:
        menu()
        print("------------------------------------")
        decisão=int(input("Escolhe uma opção:"))
        if decisão==1:
            lista=opcao1()
            print("------------------------------------")
            print(f"A tua lista está criada: {lista}")
        elif decisão==2:
            lista=opcao2()
            print("------------------------------------")
            print(f"A tua lista está criada: {lista}")
        elif decisão==3:
            soma=opcao3(lista)
            print("------------------------------------")
            print(f"A soma da tua lista dá: {soma}")
        elif decisão==4:
            media=opcao4(lista)
            print("------------------------------------")
            print(f"A média dos elementos da tua lista dá: {media}")
        elif decisão==5:
            opcao5(lista)
        elif decisão==6:
            opcao6(lista)
        elif decisão==7:
            opcao7(lista)
        elif decisão==8:
            opcao8(lista)
        elif decisão==9:
            opcao9(lista)
        elif decisão==0:
            opcao0()
            break
    
jogo()