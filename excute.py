import main

class exc():
    a = main.geometria_Analitica
    b = main.geometria_Analitica
    c = main.geometria_Analitica
    r2 = main.vetor_R2

    opcao = int(input("""
    Insira 1: Geometria Ánalitica
    Insira 2: Algebra linear
    Insira: """))

    if opcao == 1:      
        opcao = int(input("""
        Insira 1: Calculo de vetor
        Insira 2: Soma de dois vetores
        Insira 3  Soma de varios vetores
        Insira 4: Vetor R2
        Insira 5: Produto escalar de 2 vetores no R2
        Insira: """))

        if opcao == 1: #Calcula o Vetor
            x = int(input("Insira X:"))
            y = int(input("Insira Y:"))
            a = a.calcula_Vetor(1,x,y)

            p1 = str(input("Deseja Adicionar a soma ? S/N: "))

            if p1 == "S" or "s":                
                p1 = str(input("Você ja possui o Vetor? S/N: "))                
                if p1 == "S" :
                    v1 = int(input("Insira o Vetor: "))
                    c.soma_De_Vetores(1,a,v1)    
                elif p1== "N" or "n":    
                    print("Insira Proximo calculo do vetor: ")
                    x = int(input("Insira X: "))
                    y = int(input("Insira Y: "))
                    b =b.calcula_Vetor(1,x,y)
                    c.soma_De_Vetores(1,a,b)
                else:
                    print("Por favor renicie o Aplicativo...")

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
