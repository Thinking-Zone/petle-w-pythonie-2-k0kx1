import random

def zgadnij_pogode():
    odpowiedz = ["tak", "nie"]
    prawidlowa_odpowiedz = random.choice(odpowiedz)
    
    while true:
        odpowiedz_uytkownika = input("czy dzisiaj pada descz? (tak/nie): ").lower()
    
    if odpowiedz_uzytkownika not in odpowiedz:
        print("proszę, odpowiedz 'tak' lub 'nie'.")
        continue
    
    if odpowiedz_uzytkownika == prawidlowa_odpowiedz:
        print("gratulacje! zgadłeś poprawnie.")
        break
    else:
        print("niestety, to nie jest poprawna odpowiedź. Spróbuj ponownie.")
        
        gadnij_pogode()

