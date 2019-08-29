import time
#Desenvolvedor: Iago
#Funcao sons e barra direita e esquerda ------------------------------------------------
def verificar_sons_barras():
    som1_barra1 = 0
    som1_barra2 = 0
    som2_barra1 = 0
    som2_barra2 = 0
    contador_geral = 0
    quantidade_experimentos = 5

    while True:

        while True:

            som = int(input("SOM 1 (1) - SOM (2): "))
            barra = int(input("ESQUERDA (1) - DIREITA (2): "))
            
            if ((som == 1 or som == 2) and (barra == 1 or barra == 2)):
                break

        if(som == 1 and barra == 1):
            som1_barra1 = som1_barra1 + 1
            print("ACERTOU...")
        if(som == 1 and barra == 2):
            som1_barra2 = som1_barra2 + 1
            print("ERROU...")
        if(som == 2 and barra == 1):
            som2_barra1 = som2_barra1 + 1
            print("ERROU...")
        if(som == 2 and barra == 2):
            som2_barra2 = som2_barra2 + 1
            print("ACERTOU...")
        
        contador_geral = contador_geral + 1

        if(contador_geral == quantidade_experimentos):
            break

    return 1
#---------------------------------------------------------------------------------------

#Funcao verificar toque na barra -------------------------------------------------------
def verificar_toque_barra():
    contador_barra = 20
    contador_toques = 0
    while contador_barra > 0:
        toque_barra = float(input("O ANIMAL TOCOU NA BARRA? "))
        if toque_barra == 1:
            contador_barra = contador_barra - 1
            contador_toques = contador_toques + 1
            print("0/ Toque: ", contador_toques)
    print("PASSOU PARA A PROXIMA ETAPA DO EXPERIMENTO...")
    return 1
#---------------------------------------------------------------------------------------


#Funcao para verificar aproximacao -----------------------------------------------------
def verificar_aproximacao():
    aproximacao = 30
    aproximacao_atual = 0

    while aproximacao > 0:
        while True:
            aproximacao_atual = float(input("QUANTOS CM O ANIMAL SE APROXIMOU? "))
            if (aproximacao - aproximacao_atual) < 0 or (aproximacao_atual) < 0:
                print("ERRO... VERIFIQUE O SENSOR E O CÓDIGO...")
            elif (aproximacao - aproximacao_atual) >= 0:
                break
        if(aproximacao_atual <= aproximacao):
            print("LIBERAR 0.5ML DE RECOMPENSA")
        aproximacao = aproximacao - aproximacao_atual
    return 1
#---------------------------------------------------------------------------------------


#Funcao de habituacao ------------------------------------------------------------------
def habituacao():
    habituado = 0

    while habituado!=1:
        habituado = int(input("O ANIMAL ESTÁ HABITUADO? 0 - NÃO / 1 - SIM: "))
        if habituado == 0:
            print("ANIMAL NÃO HABITUADO...")
        elif habituado == 1:
            print("ANIMAL HABITUADO...")
    return habituado
#---------------------------------------------------------------------------------------


#Funcao principal ----------------------------------------------------------------------
def funcao_principal():
    esta_habituado = habituacao()
    if esta_habituado:
        aproximacao_max = verificar_aproximacao()
        if aproximacao_max:
            toque_b = verificar_toque_barra()
            if toque_b:
                inicio = time.time()
                verificar_sons_barras()
                fim = time.time()
                tempo_segundos = fim - inicio
                minutos = 1
                tempo_limite = 60*minutos
                if tempo_segundos <= tempo_limite:
                    print("TEMPO EM SEGUNDOS: %.2f" % tempo_segundos)
                    print("PASSOU A PROXIMA ETAPA DO EXPERIMENTO...")
#---------------------------------------------------------------------------------------

funcao_principal() #Chamando funcao principal 
