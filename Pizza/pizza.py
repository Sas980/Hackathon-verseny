pizzak = ['Margaréta', 'Hawaii', 'Pepperoni']
feltek = ['Extra Sajt', 'Gomba', 'Szalámi']
italok = ['Kóla', 'Sprite', 'Ásványvíz']
meretek = ['Kis', 'Médium', 'Nagy']
bot = 'Bot:'

def chatbot_valasz(uzenet, rendeles, meretek):
    valasz = ''
    repeat = True
    if 'Rendel' in uzenet or 'Menü' in uzenet:
        valasz += f'{bot} Rendelhető pizzák: ' + ', '.join(pizzak) + '\n'
        valasz += f'{bot} Rendelhető feltétek: ' + ', '.join(feltek) + '\n'
        valasz += f'{bot} Rendelhető italok: ' + ', '.join(italok) + '\n'
    elif any(pizza in uzenet for pizza in pizzak):
        print(f"{bot} Remek választás!\n")
        meret = input(f'{bot} Kis, médium vagy nagy legyen?').title()
        if any(meret in meretek for meretek in meretek):
            if 'Kis' in meret:
                pizza = next((pizza for pizza in pizzak if pizza in uzenet), None)
                print(f'{bot} {meret} {pizza} hozzáadva a rendeléshez.')
                pizza = meret + ' ' + pizza
                rendeles['pizzak'].append(pizza)
                print(f"{bot}Kérsz extra feltétet, pizzát vagy italt?")
            elif 'Médium' in meret:
                pizza = next((pizza for pizza in pizzak if pizza in uzenet), None)
                print(f'{bot} {meret} {pizza} hozzáadva a rendeléshez.')
                pizza = meret + ' ' + pizza
                rendeles['pizzak'].append(pizza)
                print(f"{bot}Kérsz extra feltétet, pizzát vagy italt?")
            elif 'Nagy' in meret:
                pizza = next((pizza for pizza in pizzak if pizza in uzenet), None)
                print(f'{bot} {meret} {pizza} hozzáadva a rendeléshez.')
                pizza = meret + ' ' + pizza
                rendeles['pizzak'].append(pizza)
                print(f"{bot}Kérsz extra feltétet, pizzát vagy italt?")
        else:
            print(f'{bot} Ilyen méret nincs!\n{bot} Rendelhető méretek: ' + ', '.join(meretek) + '\n')

    elif any(feltet in uzenet for feltet in feltek):
        feltet = next((feltet for feltet in feltek if feltet in uzenet), None)
        rendeles['feltetek'].append(feltet)
        print(f'{bot} {feltet} hozzáadva a rendeléshez.')
        print("Kérsz extra feltétet, pizzát vagy italt?")
    elif any(ital in uzenet for ital in italok):
        ital = next((ital for ital in italok if ital in uzenet), None)
        rendeles['italok'].append(ital)
        print(f'{bot} {ital} hozzáadva a rendeléshez.')
        print(f"{bot}Kérsz extra feltétet, pizzát vagy italt?")
    elif 'Kész' in uzenet or 'Köszönöm' in uzenet:
        valasz += f'{bot} A rendelés elkészült:\n'
        valasz += f'{bot} Pizzák: ' + ', '.join(rendeles['pizzak']) + '\n'
        valasz += f'{bot} Feltétek: ' + ', '.join(rendeles['feltetek']) + '\n'
        valasz += f'{bot} Italok: ' + ', '.join(rendeles['italok']) + '\n'
        valasz += f'{bot} Végösszeg: ' + str(vegosszeg_szamolas(rendeles)) + ' Ft\n'
    else:
        if 'köszönöm' not in uzenet:
            valasz += f'{bot} Sajnálom, nem értem a kérést. Kérlek, próbálj meg rendelni vagy lezárni a rendelést.\n'
    return valasz, repeat



def vegosszeg_szamolas(rendeles):
    arak = {
        'Kis Margaréta': 2500,
        'Médium Margaréta': 2700,
        'Nagy Margaréta':3500,
        'Kis Hawaii': 2700,
        'Médium Hawaii': 2900,
        'Nagy Hawaii': 3700,
        'Kis Pepperoni': 2600,
        'Médium Pepperoni': 2800,
        'Nagy Pepperoni': 3600,
        'Extra Sajt': 200,
        'Gomba': 150,
        'Szalámi': 250,
        'Kóla': 300,
        'Sprite': 300,
        'Ásványvíz': 200
    }

    osszeg = sum(arak[item] for item in rendeles['pizzak'] + rendeles['feltetek'] + rendeles['italok'])
    return osszeg


rendeles = {
    'pizzak': [],
    'feltetek': [],
    'italok': []
}

print(f'{bot} Üdvözöllek a pizzarendelő chatbotban!\n'
f'{bot} Rendelhető pizzák: ' + ', '.join(pizzak) + '\n'
f'{bot} Rendelhető feltétek: ' + ', '.join(feltek) + '\n'
f'{bot} Rendelhető italok: ' + ', '.join(italok) + '\n')
print(f'{bot} Kezdjük a rendelést!')
repeat = True
while repeat:
    uzenet = input('Felhasználó: ')
    uzenet = uzenet.title()
    valasz, repeat = chatbot_valasz(uzenet, rendeles, meretek)
    print(valasz)
    if 'Kész' in uzenet or 'Köszönöm' in uzenet:
        print(f'{bot} Köszönöm a rendelést! A rendelési állomány elkészült.')
        break