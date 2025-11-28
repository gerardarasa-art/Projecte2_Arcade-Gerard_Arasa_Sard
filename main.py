import jocs

def mostrar_menu():
    print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("3. Sortir\n")

def main():
    while True:  # Bucle principal
        mostrar_menu()
        opcio = input("Escull una opció: ").strip().upper() # El .strip() elimina espais innecessaris i el .upper() converteix l'entrada a majúscules

        if opcio == '1':
            jocs.janken()
        elif opcio == '2':
            jocs.nana()
        elif opcio == '3':
            print("Gràcies per jugar! Fins aviat!")
            break # Surt del bucle i acaba el programa
        else:
            print("Opció incorrecta! Torna-ho a provar.")

if __name__ == "__main__": # Usem aquesta condició per a que el codi dins només s'executi quan aquest fitxer és el principal
    main()
