import main
import call

class Exc():
    a = call.Select

    opcao = int(input("""
    Insira 1: Geometria Ánalitica
    Insira 2: Algebra linear
    Insira: """))

    if opcao == 1:      
            opcao = int(input("""
            Insira 1: Expressão Analitica
            Insira 2: Soma de dois vetores
            Insira 3  Soma de varios vetores
            Insira 4: Vetor R2
            Insira 5: Produto escalar de 2 vetores no R2
            Insira: """))
        if opcao == 1:
            a.geo_opcao_1()

        if opcao == 2: #Soma de dois vetores
            print("Insira o vetor A é B")            
            v_A = float(input("Insira o A: "))
            v_B = float(input("Insira o B: "))
            a.soma_De_Vetores(1,v_A,v_B)

        if opcao == 3: #Soma de varios vetores
            print("Insira o Numero de Vetores ate 5 vetores:")
            n=int(input(""))
            if n == 2:
                v_A = int(input("Insira Vetor A: "))
                v_B = int(input("Insira Vetor B: "))
                a.soma_De_Varios_Vetores(2,v_A,b,0,0,0)
            if n == 3:
                v_A = int(input("Insira Vetor A: "))
                v_B = int(input("Insira Vetor B: "))
                v_C = int(input("Insira Vetor C: "))
                a.soma_De_Varios_Vetores(3,v_A,v_B,v_C,0,0)
            if n == 4:
                v_A = int(input("Insira Vetor A: "))
                v_B = int(input("Insira Vetor B: "))
                v_C = int(input("Insira Vetor C: "))
                v_D = int(input("Insira Vetor D: "))
                a.soma_De_Varios_Vetores(4,v_A,v_B,v_C,v_D,0)
            if n == 5:
                v_A = int(input("Insira Vetor A: "))
                v_B = int(input("Insira Vetor B: "))
                v_C = int(input("Insira Vetor C: "))
                v_D = int(input("Insira Vetor D: "))
                v_F = int(input("Insira Vetor F: "))
                a.soma_De_Varios_Vetores(5,v_A,v_B,v_C,v_D,v_F)
            else:
                print("Insira o numero ate 4")

        if opcao == 4: #Vetor R2_D2
            xA = int(input("Insira xA: "))
            yA = int(input("Insira yA: "))
            xB = int(input("Insira xB: "))
            yB = int(input("Insira yB: "))
            a.vetor_R2(0,xA,yA,xB,yB)

        if opcao == 5: #Produto_escalar_de_2_vetores_no_R2            
            xA = float(input("Insira xA: "))
            yA = float(input("Insira yA: "))
            xB = float(input("Insira xB: "))
            yB = float(input("Insira yB: "))
            r2.produto_esc_2_no_R2(0,xA,yA,xB,yB)
exc()
