import main


class Select(staticmethod):  

    def opcao():
     a = int(input("""
        Insira 1: Geometria Analitica
        Insira 2: Algebra linear
        Insira: """))
     return a
   
    def escolha():
        valor = int(input("""Digite:
        1 - Expressão Analítica
        2 - Modulo do Vetor
        3 - Soma de Vetores
        4 - Produto Escalar
        Insira o numero: """))
        print("")
        return valor

    def geo_opcao_1(): #Expressão Analítica.
        i = int(input("Digite o R: 1,2,3"))
        if i == 1:
            xA = int(input("Insira o valor de xA:"))
            xB = int(input("Insira o valor de xB:"))
            yA = int(input("Insira o valor de yA:"))
            yB = int(input("Insira o valor de yB:"))
            s = main.geometria_Analitica.vetor
            s.expressao_Analitica(xA,yA,xB,yB)
        elif i == 2:
            xA = int(input("Insira o valor de xA:"))
            xB = int(input("Insira o valor de xB:"))
            yA = int(input("Insira o valor de yA:"))
            yB = int(input("Insira o valor de yB:"))
            s = main.geometria_Analitica.vetor_R2
            s.expressao_Analitica(xA,yA,xB,yB)
        elif i == 3:
            print("Ainda não esta pronto.")
        else:
            print("Insira um dos 3 Valores")
            
    def geo_opcao_2(): #Modulo do Vetor.
        x = int(input("Insira o valor de x:"))
        y = int(input("Insira o valor de y:"))
        s = main.geometria_Analitica.vetor
        s.modulo_Do_Vetor(x,y)
        
    def geo_opcao_3(): #Soma de Vetores
        r = main.geometria_Analitica.vetor
        v = int(input("Quantos Vetores Deseja Somar ?"))
        if v == 2:
            a = int(input("Digite o Vetor A: "))
            b = int(input("Digite o Vetor B: "))
            r.soma_De_Vetores(v,a,b,0,0,0)
        elif v == 3:
            a = int(input("Digite o Vetor A: "))
            b = int(input("Digite o Vetor B: "))
            c = int(input("Digite o Vetor C: "))
            r.soma_De_Vetores(v,a,b,c,0,0)
        elif v == 4:
            a = int(input("Digite o Vetor A: "))
            b = int(input("Digite o Vetor B: "))
            c = int(input("Digite o Vetor C: "))
            d = int(input("Digite o Vetor D: "))
            r.soma_De_Vetores(v,a,b,c,d,0)
        elif v == 5:
            a = int(input("Digite o Vetor A: "))
            b = int(input("Digite o Vetor B: "))
            c = int(input("Digite o Vetor C: "))
            d = int(input("Digite o Vetor D: "))
            f = int(input("Digite o Vetor F: "))
            r.soma_De_Vetores(v,a,b,c,d,f)
        else:
            print("Retorne um numero adquado.")

    def geo_opcao_4(): #Produto Escalar
        print("Opção: Produto escalar.")
        xA = int(input("Insira o valor de xA:"))
        xB = int(input("Insira o valor de xB:"))
        yA = int(input("Insira o valor de yA:"))
        yB = int(input("Insira o valor de yB:"))
        s = main.geometria_Analitica.vetor_R2.produto_escalar_2(xA,yA,xB,yB)