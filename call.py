import main

class Select(object):    
    def geo_opcao_1():
        print("Expressão Analitica")
        xA = int(input("Insira o valor de xA:"))
        xB = int(input("Insira o valor de xB:"))
        yA = int(input("Insira o valor de yA:"))
        yB = int(input("Insira o valor de yB:"))
        s = main.geometria_Analitica.vetor
        s.expressao_Analitica(xA,yA,xB,yB)
        print(s)
        
          



        



