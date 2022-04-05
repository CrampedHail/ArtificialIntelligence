import json
import random


def generate_new_records(size):
    prefixes = ["Artefaktyczny", "Legendarny", "Epicki", "Rzadki", "Niepospolity", "Niespotykany", "Pospolity", "Slaby", "Zniszczony", "Tepy", "Rdzawy", "Elegancki"]
    prefixes_mn = ["Artefaktyczne", "Legendarne", "Epickie", "Rzadkie", "Niepospolite", "Niespotykane", "Pospolite", "Slabe", "Zniszczone", "Tepe", "Rdzawe", "Eleganckie"]
    prefixes_f = ["Artefaktyczna", "Legendarna", "Epicka", "Rzadka", "Niepospolita", "Niespotykana", "Pospolita", "Slaba", "Zniszczona", "Tepa", "Rdzawa", "Elegancka"]
    sword_names = ["Miecz Jednoreczny", "Czopesz", "Kosiarz", "Topor Jednoreczny", "Kostur", "Szczerbinator",
                   "Morgensztern", "Patelnia", "Kazoo", "Halabarda", "Rozdzka", "Dzida", "Luk", "Kusza", "Katapulta", "Balista", "Trebusz", "Taran"]
    suffixes = ["Ognia", "Lodu", "Mroku", "Swiatlosci", "Gniewu", "Odwagi", "Chwaly", "Ziemi", "Wiatru", "Nekromacji", "Sily", "Slabosci"]

    data = {
        'helmets': [
            {
                'name': '',
                'armor': '',
                'price': ''
            }
        ],
        'chestplates': [
            {
                'name': '',
                'armor': '',
                'price': ''
            }
        ],
        'leggings': [
            {
                'name': '',
                'armor': '',
                'price': ''
            }
        ],

        'boots': [
            {
                'name': '',
                'armor': '',
                'price': ''
            }
        ],
        'shields': [
            {
                'name': '',
                'armor': '',
                'price': ''
            }
        ],
        'swords': [
            {
                'name': '',
                'damage': '',
                'price': ''
            }
        ]
    }

    generated_helmets = []
    generated_chestplates = []
    generated_leggings = []
    generated_boots = []
    generated_shields = []
    generated_swords = []

    #helmets
    while(len(generated_helmets) < size):
        generated_helmet = {'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' Helm ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                        'armor': random.randint(125, 225),
                        'price': random.randint(50, 300)}
        if generated_helmet not in generated_helmets:
            generated_helmets.append(generated_helmet)
    #chestplates
    while(len(generated_chestplates) < size):
        generated_chestplate = {'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' Napiersnik ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                            'armor': random.randint(200, 300),
                            'price': random.randint(200, 500)}
        if generated_chestplate not in generated_chestplates:
            generated_chestplates.append(generated_chestplate)
    #leggings
    while(len(generated_leggings) < size):
        generated_legging = {'name': prefixes_mn[random.randint(0, len(prefixes_mn) - 1)] + ' Spodnie ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                         'armor': random.randint(150, 250),
                         'price': random.randint(100, 400)}
        if generated_legging not in generated_leggings:
            generated_leggings.append(generated_legging)
    #boots
    while(len(generated_boots) < size):
        generated_boot = {'name': prefixes_mn[random.randint(0, len(prefixes_mn) - 1)] + ' Trzewiki ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                      'armor': random.randint(125, 225),
                      'price': random.randint(50, 300)}
        if generated_boot not in generated_boots:
            generated_boots.append(generated_boot)
    #shield
    while(len(generated_shields) < size):
        generated_shield = {'name': prefixes_f[random.randint(0, len(prefixes_f) - 1)] + ' Tarcza ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                        'armor': random.randint(150, 250),
                        'price': random.randint(100, 400)}
        if generated_shield not in generated_shields:
            generated_shields.append(generated_shield)
    #sword
    while(len(generated_swords) < size):
        generated_sword = {'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' ' + sword_names[
            random.randint(0, len(sword_names) - 1)] + ' ' + suffixes[random.randint(0, len(suffixes) - 1)],
                       'damage': random.randint(200, 300),
                       'price': random.randint(200, 500)}
        if generated_sword not in generated_swords:
            generated_swords.append(generated_sword)
    
    data['helmets'] = generated_helmets
    data['chestplates'] = generated_chestplates
    data['leggings'] = generated_leggings
    data['boots'] = generated_boots
    data['shields'] = generated_shields
    data['swords'] = generated_swords

    json_string = json.dumps(data)

    with open('items_baza.json', 'w') as outfile:
        json.dump(json_string, outfile, indent=4)


def get_armor(current_eq):
    curr_armor = int(current_eq['helmet']['armor'])
    curr_armor += int(current_eq['chestplate']['armor'])
    curr_armor += int(current_eq['leggings']['armor'])
    curr_armor += int(current_eq['boots']['armor'])
    curr_armor += int(current_eq['shield']['armor'])
    return curr_armor


def get_damage(current_eq):
    return int(current_eq['sword']['damage'])


def get_price(newEQ):
    return int(newEQ['helmet']['price']) + int(newEQ['chestplate']['price']) + int(
        newEQ['leggings']['price']) + int(newEQ['boots']['price']) + int(newEQ['shield']['price']) + int(
        newEQ['sword']['price'])



def find_new_random_eq():
    newEQ = {'helmet': helmets[random.randint(0, len(helmets) - 1)],
             'chestplate': chestplates[random.randint(0, len(chestplates) - 1)],
             'leggings': leggings[random.randint(0, len(leggings) - 1)],
             'boots': boots[random.randint(0, len(boots) - 1)],
             'shield': shields[random.randint(0, len(shields) - 1)],
             'sword': swords[random.randint(0, len(swords) - 1)]}
    currentPrice = 0 + int(newEQ['helmet']['price']) + int(newEQ['chestplate']['price']) + int(
        newEQ['leggings']['price']) + int(newEQ['boots']['price']) + int(newEQ['shield']['price']) + int(
        newEQ['sword']['price'])
    newEQ = {'helmet': newEQ['helmet'],
             'chestplate': newEQ['chestplate'],
             'leggings': newEQ['leggings'],
             'boots': newEQ['boots'],
             'shield': newEQ['shield'],
             'sword': newEQ['sword'],
             'price': currentPrice}
    return newEQ

def show_best_eq_and_compare(bestEQ, enemy):
    print("Best EQ found:")
    print(" "+str(bestEQ))
    print(" Armor: "+str(get_armor(bestEQ)))
    print(" Damage: "+str(get_damage(bestEQ)))
    print(" Price: "+str(get_price(bestEQ)))
    print("Enemy EQ:")
    print(" Armor: "+str(enemy['armor']))
    print(" Damage: "+str(enemy['damage']))

def get_best_random_eq():
    # Początkowe losowe wartości dla bestEQ
    while True:
            curr_eq = find_new_random_eq()
            if get_armor(curr_eq)>enemy['armor'] and get_damage(curr_eq)>enemy['damage']:
                bestEQ = curr_eq
                break
    

    #Pętla losowania i porównywania elementów o 1000000 iteracjach
    for i in range(1000000):
        currentEQ = find_new_random_eq()
        currentArmor = get_armor(currentEQ)
        currentDamage = get_damage(currentEQ)
        currentPrice = get_price(currentEQ)
        if currentArmor > int(enemy['armor']) and currentDamage > int(enemy['damage']):
            if int(bestEQ['price']) > currentPrice:
                bestEQ = {
                    'helmet': currentEQ['helmet'],
                    'chestplate': currentEQ['chestplate'],
                    'leggings': currentEQ['leggings'],
                    'boots': currentEQ['boots'],
                    'shield': currentEQ['shield'],
                    'sword': currentEQ['sword'],
                    'price': currentPrice
                }
    return bestEQ

def check_if_different(currEq, worstEq):
    i = 0
    if currEq['helmet']==worstEq['helmet']: i+=1
    if currEq['chestplate']==worstEq['chestplate']: i+=1
    if currEq['leggings']==worstEq['leggings']: i+=1
    if currEq['boots']==worstEq['boots']: i+=1
    if currEq['shield']==worstEq['shield']: i+=1
    if currEq['sword']==worstEq['sword']: i+=1
    #print(i)
    if i<4: return True
    else: return False

def get_best_harmonic_eq(enemy):
    #Inicjalizacja pamięci Harmonicznej
    HM = []
    HMS = 10
    curr_eq = {
                    'helmet': '',
                    'chestplate': '',
                    'leggings': '',
                    'boots': '',
                    'shield': '',
                    'sword': '',
                    'price': 0
                }
    
    for i in range(HMS):
        while True:
            curr_eq = find_new_random_eq()
            if get_armor(curr_eq)>enemy['armor'] and get_damage(curr_eq)>enemy['damage']:
                HM.append( curr_eq)
                break
    
    print("---Pamięć początkowa-------------------------")
    for i in range(HMS): print("EQ no. "+str(i)+" price: "+str(get_price(HM[i])))
    
    HMCR = 0.7
    PAR = 0.14
    NI = 5000
    r1 = 0
    r2 = 0
    
    for i in range(NI):
        r1 = random.uniform(0, 1)
        #print("Iteracja: "+ str(i))
        if r1<=HMCR:
            #Szukanie w pamięci
            while True:
                curr_eq = {'helmet': HM[random.randint(0, HMS - 1)]['helmet'],
                 'chestplate': HM[random.randint(0, HMS - 1)]['chestplate'],
                 'leggings':  HM[random.randint(0, HMS - 1)]['leggings'],
                 'boots': HM[random.randint(0, HMS - 1)]['boots'],
                 'shield':  HM[random.randint(0, HMS - 1)]['shield'],
                 'sword': HM[random.randint(0, HMS - 1)]['sword']}
                curr_eq['price'] = get_price(curr_eq)
                if int(get_armor(curr_eq))>enemy['armor'] and int(get_damage(curr_eq))>enemy['damage']:
                    #print("Znaleziono EQ Harmonicznie: " + str(curr_eq))
                    break
        else :
            #Szukanie losowo
            while True:
                curr_eq = find_new_random_eq()
                if int(get_armor(curr_eq))>enemy['armor'] and int(get_damage(curr_eq))>enemy['damage']:
                    #print("Znaleziono EQ Losowo: " + str(curr_eq))
                    break
        #podmiana w pamieci
        worst_id = -1
        worst_price = get_price(HM[0])
        for j in range(HMS):
            if HM[j]['price']>=worst_price:
                worst_price = HM[j]['price']
                worst_id = j
        #print("Znaleziono najgorsze EQ: " + str(HM[worst_id]))
        if worst_id>-1:
            #print("true:" + str(worst_id))
            if HM[worst_id]['price']>get_price(curr_eq):
                #print("true")
                if check_if_different(curr_eq, HM[worst_id]):
                    #print("true")
                    HM[worst_id] = curr_eq
                    
                    
    print("---Pamięć końcowa-------------------------")
    for i in range(HMS): print("EQ no. "+str(i)+" price: "+str(get_price(HM[i])))
    #for i in range(HMS): print("EQ no. "+str(i)+" price: "+str(HM[i]))
        

if __name__ == '__main__':
    # Generowanie nowej bazy o 6 razy większej liczbie elementów od podanej w parametrze
    #generate_new_records(10000)

    # Statystyki przeciwnika
    enemy = {
        'armor': 1000,
        'damage': 250
    }

    # Wczytywanie bazy z pliku
    data = json.loads(json.load(open('items_baza.json')))

    # Rozdzielanie list itemów do zmiennych
    helmets = data['helmets']
    chestplates = data['chestplates']
    leggings = data['leggings']
    boots = data['boots']
    shields = data['shields']
    swords = data['swords']
    
    
    # Znajdź najlepsze "harmoniczne" eq
    #bestEQ = get_best_harmonic_eq()
    get_best_harmonic_eq(enemy)
    
    
    # Znajdź najlepsze losowe eq
    #bestEQ = get_random_best_eq()
    
    # Wywietl najlepsze eq i porównaj z enemy
    #show_best_eq_and_compare(bestEQ, enemy)
    
    
