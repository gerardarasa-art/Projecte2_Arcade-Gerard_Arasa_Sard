import robot # El robot serveix per a la funció dins dels jocs
import jocs  # Importem el mòdul jocs que conté els jocs

def mostrar_menu():
    print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
    print("1. Jugar a Pedra, Paper, Tisora")
    print("2. Jugar a Endevinar el Número")
    print("3. Sortir\n")


def janken():
    import jocs
    jocs.janken()


def nana():
    import jocs
    jocs.nana()

def main():
    while True:  # Bucle principal
        mostrar_menu()
        opcio = input("Escull una opció: ").strip().upper()

        if opcio == '1':
            janken()
        elif opcio == '2':
            nana()
        elif opcio == '3':
            print("Gràcies per jugar! Fins aviat!")
            break
        else:
            print("Opció incorrecta! Torna-ho a provar.")

if __name__ == "__main__":
    main()
