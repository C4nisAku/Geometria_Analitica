import select

class Exc():
    a = select.Select
    
    seletor_geo_alg = a.opcao()

    if seletor_geo_alg == 1:      
        opcao = a.escolha()
        if   opcao == 1:
            a.geo_opcao_1()
        elif opcao == 2:
            a.geo_opcao_2()
        elif opcao == 3:
            a.geo_opcao_3()
        elif opcao == 4:
            pass
        elif opcao == 5:         
            pass

Exc()
