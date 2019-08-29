habituado = int(input("O ANIMAL ESTÁ HABITUADO? 0 - NÃO / 1 - SIM: "))

if habituado == 0:
    print("ANIMAL NAO HABITUADO! HABITUAR ANIMAL...")
elif habituado == 1:
    print("ANIMAL HABITUADO!")
    
    aproximacao_constante = 30
    aproximacao_atual = float(input("APROXIMACAO DO ANIMAL EM CENTIMETROS: "))
    
    if(aproximacao_atual < aproximacao_constante):
        print("LIBERAR 0.5ML DE RECOMPENSA")
        
        barra = int(input("O ANIMAL TOCOU NA BARRA 20 VEZES? 0 - NÃO / 1 - SIM: "))
        if barra  == 0:
            print("AINDA NÃO PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...")
        elif barra == 1:
            print("PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...")

            som1 = int(input("O SOM 1 FOI EMITIDO? 0 - NÃO / 1 - SIM: "))
            barra_esquerda = int(input("A BARRA ESQUERDA FOI TOCADA? 0 - NÃO / 1 - SIM: "))

            if som1 == 1 and barra_esquerda == 1:
                print("LIBERAR 0.5ML DE RECOMPENSA")
            else: 
                print("NÃO LIBERAR RECOMPENSA")

            som2 = int(input("O SOM 2 FOI EMITIDO? 0 - NÃO / 1 - SIM: "))
            barra_direita = int(input("A BARRA DIREIRA FOI TOCADA? 0 - NÃO / 1 - SIM: "))

            if som2 == 1 and barra_direita == 1:
                print("LIBERAR 0.5ML DE RECOMPENSA")
            else: 
                print("NÃO LIBERAR RECOMPENSA")
                
            experimento_tempo = int(input("O EXPERIMENTO FOI REALIZADO 50x EM 30min? 0 - NÃO / 1 - SIM: "))
            if experimento_tempo == 1:
                print("PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...")
            else:
                print("AINDA NÃO PASSOU PARA A PRÓXIMA ETAPA DO EXPERIMENTO...") 