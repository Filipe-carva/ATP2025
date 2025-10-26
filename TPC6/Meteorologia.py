from matplotlib import pyplot as plt

tabMeteo3 = [((2022,1,20), 2, 16, 0), ((2022,1,21), 1, 13, 0.2), ((2022,1,23), 6, 19, 0.6), 
             ((2022,1,24), 3, 18, 0.8), ((2022,2,20), 6, 19, 0.2), ((2022,2,24), 3, 18, 0.2), 
             ((2022,2,28), 3, 18, 0.2)]

def medias(tabMeteo):
    res = []
    for h in tabMeteo:
        res.append((h[0],(h[2]+h[1])/2))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    res = ""
    for i in t:
        ano = i[0][0]
        mes = i[0][1]
        dia = i[0][2]
        tempmin = i[1]
        tempmax = i[2]
        prec = i[3]

        res = f"{str(ano)}-{str(mes)}-{str(dia)}::{tempmin}::{tempmax}::{prec}\n"
        file.write(res)
    
    file.close()

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    text = file.read()
    linhas_text = text.split("\n")
    for elementos in linhas_text[:-1]:
        dados = elementos.split("::")
        data, tmin, tmax, prec = dados 
        ano, mes, dia = data.split("-") 
        elem = ((int(ano), int(mes), int(dia)), float(tmin), float(tmax), float(prec))  
        res.append(elem)

    return res

def minMin(tabMeteo):
    base = tabMeteo[0][1]
    for h in tabMeteo[1:]:
        if h[1] < base:
            base = h[1]
    return base

def amplTerm(tabMeteo):
    res = []
    for h in tabMeteo:
        amplitude = h[2] - h[1]
        res.append((h[0], amplitude))
    return res 

def maxChuva(tabMeteo):
    base = tabMeteo[0][3]
    data = tabMeteo[0][0]  
    for h in tabMeteo[1:]:
        if h[3] > base:
            base = h[3]
            data = h[0]
    return (data, base)

def diasChuvosos(tabMeteo, p):
    res = []
    for h in tabMeteo:
        if h[3] > p:
            res.append((h[0], h[3]))
    return res

def maxPeriodoCalor(tabMeteo, p):
    res = []
    for h in tabMeteo:
        if h[3] < p:  
            res.append((h[0], h[3]))
    res.sort()
    return res

def grafTabMeteo(t):
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, tmin, tmax, prec in t]
    ytmin = [tmin for data, tmin, tmax, prec in t]
    ytmax = [tmax for data, tmin, tmax, prec in t]
    y_prec = [prec for data, tmin, tmax, prec in t]
    

    plt.figure(figsize=(10, 6))
    plt.plot(x, ytmin, label="Temperatura Mínima (ºC)", color="blue", marker="o")
    plt.plot(x, ytmax, label="Temperatura Máxima (ºC)", color="red", marker="o")
    plt.legend()
    plt.title("Tabela meteorológica - Temperaturas")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    plt.figure(figsize=(10, 6))
    plt.bar(x, y_prec, label="Pluviosidade (mm)", color="c")
    plt.legend()
    plt.title("Tabela meteorológica - Precipitação")
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()
    return

def menu():
    print(""" 
    1- Ver Média Temperatura
    2- Guardar dados Meteorologia
    3- Carregar dados meterológicos
    4- Temperatura Mínima
    5- Amplitude térmica
    6- Dia com maior precipitação
    7- Nível de precipitação
    8- Dias de calor
    9- Gráficos Meteorologia
    10- Sair""")

condi=True
while condi:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("Médias de temperatura:", medias(tabMeteo3))
        elif opcao == "2":
            guardaTabMeteo(tabMeteo3, "dados_meteo.txt")
            print("Dados guardados!")
        elif opcao == "3":
            dados = carregaTabMeteo("dados_meteo.txt")
            print("Dados carregados:", dados)
        elif opcao == "4":
            print("Temperatura mínima absoluta:", minMin(tabMeteo3))
        elif opcao == "5":
            print("Amplitude térmica:", amplTerm(tabMeteo3))
        elif opcao == "6":
            print("Dia com maior precipitação:", maxChuva(tabMeteo3))
        elif opcao == "7":
            p = float(input("Digite o nível de precipitação: "))
            print("Dias chuvosos:", diasChuvosos(tabMeteo3, p))
        elif opcao == "8":
            p = float(input("Digite o nível de temperatura mínima: "))
            print("Dias de calor:", maxPeriodoCalor(tabMeteo3, p))
        elif opcao == "9":
            grafTabMeteo(tabMeteo3)
        elif opcao == "10":
            print("A sair...")
            condi=False
        else:
            print("Opção inválida!")

