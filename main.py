import math

class matematica():    
    def raiz_quadrada(raiz):
        r = math.sqrt(raiz)
        return r    
    
class geometria_Analitica(): 
    class vetor(matematica):

        def expressao_Analitica(xA,yA,xB,yB):
            x = xA - xB  
            y = yA - yB
            print(f"Resultado: (x {x};y {y})")
            return x , y
        
        def modulo_Do_Vetor(x,y):
            x1 = x * x
            y1 = y * y
            s  = x1 + y1
            raiz = matematica.raiz_quadrada(s)
            print(f"""Modulo sem raiz calculada: {s}
            Modulo com raiz calculada {raiz}""")

        def soma_De_Vetores(n,a,b,c,d,f):
            if n == 2 :
                s = a * a + b * b
                print(f"O Resultado é: {s}") 
            elif n == 3:
                s = a * a + b * b + c * c
                print(f"O Resultado é: {s}") 
            elif n == 4:
                s = a * a + b * b + c * c + d * d
                print(f"O Resultado é: {s}") 
            elif n == 5:
                s = a * a + b * b + c * c + d * d + f * f
                print(f"O Resultado é: {s}")   
     
    class vetor_R2(matematica):
        def expressao_Analitica(xA,yA,xB,yB):
            x = xA - xB             
            y = yA - yB
            s = x * x + y * y
            raiz = matematica.raiz_quadrada(s)

            #Print
            print("Vetor: ")
            print(f"X:{x}    Y:{y}")

            print("Quadrado Calculado:")
            print(f"(X:{s} Y:{s})")

            print(f"Modulo do vetor: V = {s}")
            print(f"Raiz do vetor: {raiz}")

        def produto_escalar_2(xA,yA,xB,yB):
            s = xA * xB + yA * yB
            print(f"Produto escalar desse vetores é {s}")
            return s
        
        def calcula_angulo_R2(xA,yA,xB,yB):
            pass

    class vetor_R3(matematica):
        pass

class algebra_Linear(matematica):    
    pass