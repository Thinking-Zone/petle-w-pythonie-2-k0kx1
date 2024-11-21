import random


pogoda = random.choice(['pada', 'nie pada'])


while input("czy pada deszcz? (pada/nie pada): ") != pogoda:
    print("nie zgadłeś, spróbuj jeszcze ra.")

print("brawo! zgadłeś!")
