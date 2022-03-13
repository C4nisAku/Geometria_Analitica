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
        1 - Expressao Analitica
        2 - Modulo do Vetor
        3 - Soma de Vetores
        Insira: """))
        print("")
        return valor

    def geo_opcao_1():
        xA = int(input("Insira o valor de xA:"))
        xB = int(input("Insira o valor de xB:"))
        yA = int(input("Insira o valor de yA:"))
        yB = int(input("Insira o valor de yB:"))
        s = main.geometria_Analitica.vetor
        s.expressao_Analitica(xA,yA,xB,yB)   
  
    def geo_opcao_2():
        x = int(input("Insira o valor de x:"))
        y = int(input("Insira o valor de y:"))
        s = main.geometria_Analitica.vetor
        s.modulo_Do_Vetor(x,y)
        
    def geo_opcao_3():
        pass