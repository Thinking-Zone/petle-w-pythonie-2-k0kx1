pada = False
licznik_nie = 0


while not pada:
    odpowiedz = input("czy pada? (tak/nie/nie wiem): ").lower()
    
    if odpowiedz == "tak":
        pada = True
    elif odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "nie wiem":
        print("To sobie pójdzi na zewnątrz i se zoba.")
    else:
        print("nie kumam. Proszę odpowiedz 'tak', 'nie' lub 'nie wiem'.")
        
        
    print(f"liczba odpowiedzi 'nie': {licznik_nie}")    

