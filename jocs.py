import robot # El robot serveix per a la funció dins dels jocs

def janken():
    # PEDRA PAPER TISORA
    print("\n--- Pedra, Paper, Tisora ---")
    
    # Tipus de dificultats
    print("1. El primer que arribi a 3 victòries")
    print("2. El millor a 5 rondes")
    mode = input("Escull una dificultat (1 o 2): ") 
    
    if mode == '1':
        limit_victories = 3 
        limit_rondes = None # No hi ha límit de rondes ja que es al primer que arribi a 3/5 victòries
    
    elif mode == '2':
        limit_victories = None
        limit_rondes = 5 # No hi ha límit de rondes ja que es al primer que arribi a 3/5 victòries
    else:
        print("Opció incorrecta! Tornant al menú principal.")
        return
    
    # Contadors, això serà útil per a les funcions de joc, quan l'usuari o la màquina arribi a 3/5 victòries, el joc acabarà
    usuari = 0
    maquina = 0
    ronda = 0
    
    while True:
        print("\n--- Nova Ronda ---")
        tir_usuari = input("Escriu pedra, paper o tisora: ").lower() # El .lower() serveix per a que no hi hagi problemes amb majúscules/minúscules

        if tir_usuari not in ("pedra", "paper", "tisora"): # El not in serveix per a comprovar si la tirada de l'usuari és vàlida
            print("Tirada incorrecta! Torna-ho a provar.")
            continue # El continue serveix per a tornar al principi del bucle si l'entrada és incorrecta
    
        tir_maquina = robot.random.choice(["pedra", "paper", "tisora"]) # La màquina fa la seva tirada
        print("El robot ha triat:", tir_maquina)
        
        # Resultats de la ronda
        if tir_usuari == tir_maquina:
            print("Empat!")
        elif (tir_usuari == "pedra" and tir_maquina == "tisora") or \
             (tir_usuari == "paper" and tir_maquina == "pedra") or \
             (tir_usuari == "tisora" and tir_maquina == "paper"):
            usuari += 1
            print("Has guanyat aquesta ronda!")
            
        else:
            maquina += 1
            print("El robot ha guanyat aquesta ronda!")
        
        ronda += 1
        print(f"Puntuació - Tu: {usuari}, Robot: {maquina}") # La f serveix per a formatar cadenes i inserir variables dins d'elles
    
        if limit_victories is not None: 
            if usuari == limit_victories or maquina == limit_victories:
                break # Break serverix per a sortir del bucle quan un dels dos arribi al límit de victòries
            
        if mode == '2' and limit_rondes == 5:
            if ronda >= limit_rondes:
                break # Break serverix per a sortir del bucle quan s'arribi al límit de rondes
    
    # GUANYADOR FINAL
    print("\n--- RESULTAT FINAL ---")
    if usuari > maquina:
        print("Felicitats! Has guanyat el joc!")
    elif maquina > usuari:
        print("El robot ha guanyat el joc! Millor sort la pròxima vegada.")
    else:
        print("El joc ha acabat en empat!")
    
    print("Gràcies per jugar a Pedra, Paper, Tisora!\n")
    print("-------------------------\n")
    print("Tornant al menú principal...")
    


def nana():
    print("--- Endevinar el Número ---")
    numero_secret = robot.random.choice(range(1, 101)) 
    intents = 0
    
    while True: # Aquest es el bucle principal del joc, quan arrbe al break, el joc s'acaba 
  
        try:
            # Posem dintre del bucle el input per a que l'usuari pugui anar provant fins a endevinar el número
            numero_usuari = int(input("Escull un número entre l'1 i el 100: ")) # Hem posat el int() per a convertir l'entrada de l'usuari en un número enter
            
        except ValueError:
            print("Entrada incorrecta. Si us plau, introdueix només un número enter.")
            continue # Torna al principi del bucle sense augmentar els intent, en el cas de que l'usuari introdueixi una entrada no vàlida

        intents += 1 # Hem creat aquesta variable per a comptar els intents que fa l'usuari

        if numero_usuari < numero_secret:
            print("El número és més alt!")
            continue  # Torna al principi del bucle per a que l'usuari pugui provar de nou
        elif numero_usuari > numero_secret:
            print("El número és més baix!")
            continue  # Torna al principi del bucle per a que l'usuari pugui provar de nou
        elif numero_usuari == numero_secret:
            print(f"Felicitats! Has endevinat el número! T'ha costat, {intents}, intents endevinar-lo.")
            break  # En el final usarem 'break' per sortir del bucle i acabar el joc