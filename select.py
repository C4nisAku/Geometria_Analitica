import main

class Select(object):   
    def escolha():
        valor = int(input("""
                Insira 1: Expressão Analitica
                Insira 2: Soma de dois vetores
                Insira 3  Soma de varios vetores
                Insira 4: Vetor R2
                Insira 5: Produto escalar de 2 vetores no R2
                Insira: """))
        return valor

    def geo_opcao_1():
        xA = int(input("Insira o valor de xA:"))
        xB = int(input("Insira o valor de xB:"))
        yA = int(input("Insira o valor de yA:"))
        yB = int(input("Insira o valor de yB:"))
        s = main.geometria_Analitica.vetor
        s.expressao_Analitica(xA,yA,xB,yB)
        
          



    