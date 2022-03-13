import select

class Exc():
    a = select.Select

    opcao = int(input("""
    Insira 1: Geometria Ánalitica
    Insira 2: Algebra linear
    Insira: """))

    if opcao == 1:      
        opcao = a.escolha()
    if opcao == 1:
        a.geo_opcao_1()
    if opcao == 2: #Soma de dois vetores
        pass
    if opcao == 3: #Soma de varios vetores
        pass
    if opcao == 4: #Vetor R2_D2
        pass
    if opcao == 5: #Produto_escalar_de_2_vetores_no_R2            
        pass
Exc()
