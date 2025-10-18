#aluno = (turma,nome, id, [notaTPC, notaProj, notaTeste])`
# turma = [aluno]
turmas=[]


def aluno(turma):
    nome=str(input("Qual o seu nome?"))
    print("----------------------------------------")
    id=str(input("Qual o seu id?"))
    print("----------------------------------------")
    notaTPC=int(input("Qual a média das notas do TPC?"))
    print("----------------------------------------")
    notaProj=int(input("Qual a nota final do projeto?"))
    print("----------------------------------------")
    notaTeste=int(input("Qual a média das notas do teste?"))
    print("----------------------------------------")
    aluno1=(turma,nome,id,[notaTPC,notaProj,notaTeste])
    turmas.append(aluno1)


def criar_turma():
    nome2=str(input("Qual o nome da turma?"))
    print("----------------------------------------")
    n_alunos=int(input("Quantos alunos tem a turma?"))
    print("----------------------------------------")
    for i in range(0,n_alunos):
        aluno(nome2)
    print(f"A turma {nome2} foi criada com sucesso!")
    print("----------------------------------------") 
    return turmas


def adicionar_aluno():
        nome3=str(input("Qual o nome da turma?"))
        print("----------------------------------------")  
        aluno(nome3)
        print(f"O aluno foi adicionado com sucesso!")
        print("----------------------------------------") 
        return turmas


def listar_turma():
     res=[]
     turmasss=str(input("Qual o nome da turma?"))
     print("----------------------------------------")
     for h in turmas:
        if h[0]==turmasss:
             res.append(h)       
     print(f"Esta é a turma {turmasss}: {res}")
     print("----------------------------------------")


def consultar_aluno():
     id=str(input("Qual o id do aluno?"))
     print("----------------------------------------")
     for h in turmas:
        if h[2]==id:
             print(f"""Nome do Aluno: {h[1]}; 
                       ID: {h[2]}; 
                       Média notas do TPC: {h[3][0]}; 
                       Nota do projeto:{h[3][1]};
                       Nota do Teste:{h[3][2]}""")
     print("----------------------------------------")

def guardar_turma(lista1, fnome):
    turmaa = str(input("Qual o nome da turma?"))
    print("----------------------------------------")
    file = open(fnome, "w")
    res = f"""Turma {turmaa}:\n"""
    for p in lista1:
        if p[0] == turmaa:
            turma=p[0]
            nome = p[1] 
            id_aluno = p[2]  
            notas = p[3] 
            res = res + str(turma) + ";" + str(nome) + ";" + str(id_aluno) + ";" + str(notas) + ";"
        res = res + "\n"
    
    file.write(res)   
    file.close()
    print(f"A turma {turmaa} foi guardada com sucesso no ficheiro:{fnome}!")
    print("----------------------------------------")


def ver_turma(fnome):
    lista1=[]
    turms=str(input("Qual o nome da turma?"))
    print("----------------------------------------")
    file=open(fnome,"r")
    text=file.read()
    turmas_text=text.split("\n")
    
    for linhas_text in turmas_text[:-1]:
        if ";" in linhas_text:
            alunos_text=linhas_text.split(";")
            if len(alunos_text) >= 1:  
                turma = alunos_text[0]
                nome = alunos_text[1]
                id_aluno = alunos_text[2]
                notas = alunos_text[3]
                
                if turma == turms: 
                    aluno = (turma, nome, id_aluno, notas)
                    lista1.append(aluno)

    print(f"Esta é a turma {turms}: {lista1}")
    print("----------------------------------------")

def menu():
    condi=True
    while condi:
        print("----------------------------------------")
        print(""" 
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 5: Guardar a turma em ficheiro;
    - 6: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação""")
        print("----------------------------------------")
        decisão=int(input("Indique a opção que deseja:"))
        print("----------------------------------------")
        if decisão==1:
             criar_turma()
             print("----------------------------------------")
        elif decisão==2:
             adicionar_aluno()
             print("----------------------------------------")
        elif decisão==3:
             listar_turma()
             print("----------------------------------------")
        elif decisão==4:
            consultar_aluno()
            print("----------------------------------------")
        elif decisão==5:
             guardar_turma(turmas,"turmas.txt")
             print("----------------------------------------")
        elif decisão==6:
             ver_turma("turmas.txt")
             print("----------------------------------------")
        elif decisão==0:
             print("Até Breve!")
             print("----------------------------------------")
             condi=False        

menu()
    



