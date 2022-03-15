import json
import random


def generate_new_records(size):
    prefixes = ["Artefaktyczny", "Legendarny", "Epicki", "Rzadki", "Niepospolity", "Niespotykany", "Pospolity"]
    prefixes_mn = ["Artefaktyczne", "Legendarne", "Epickie", "Rzadkie", "Niepospolite", "Niespotykane", "Pospolite"]
    prefixes_f = ["Artefaktyczna", "Legendarna", "Epicka", "Rzadka", "Niepospolita", "Niespotykana", "Pospolita"]
    sword_names = ["Miecz Jednoreczny", "Czopesz", "Kosiarz", "Topor Jednoreczny", "Kostur", "Szczerbinator",
                   "Morgensztern", "Patelnia", "Kazoo"]
    suffixes = ["Ognia", "Lodu", "Mroku", "Swiatlosci", "Gniewu", "Odwagi", "Chwaly"]

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

    for i in range(size):
        generated_helmets.append({'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' Helm ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                        'armor': random.randint(125, 225),
                        'price': random.randint(100, 200)})
        generated_chestplates.append({'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' Napiersnik ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                            'armor': random.randint(200, 300),
                            'price': random.randint(300, 400)})
        generated_leggings.append({'name': prefixes_mn[random.randint(0, len(prefixes_mn) - 1)] + ' Spodnie ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                         'armor': random.randint(150, 250),
                         'price': random.randint(200, 300)})
        generated_boots.append({'name': prefixes_mn[random.randint(0, len(prefixes_mn) - 1)] + ' Trzewiki ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                      'armor': random.randint(125, 225),
                      'price': random.randint(100, 200)})
        generated_shields.append({'name': prefixes_f[random.randint(0, len(prefixes_f) - 1)] + ' Tarcza ' + suffixes[
            random.randint(0, len(suffixes) - 1)],
                        'armor': random.randint(150, 250),
                        'price': random.randint(200, 300)})
        generated_swords.append({'name': prefixes[random.randint(0, len(prefixes) - 1)] + ' ' + sword_names[
            random.randint(0, len(sword_names) - 1)] + ' ' + suffixes[random.randint(0, len(suffixes) - 1)],
                       'damage': random.randint(200, 300),
                       'price': random.randint(300, 400)})
    data['helmets'] = generated_helmets
    data['chestplates'] = generated_chestplates
    data['leggings'] = generated_leggings
    data['boots'] = generated_boots
    data['shields'] = generated_shields
    data['swords'] = generated_swords

    json_string = json.dumps(data)

    with open('items_baza.json', 'w') as outfile:
        json.dump(json_string, outfile, indent=4)


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


def get_armor(current_eq):
    curr_armor = int(current_eq['helmet']['armor'])
    curr_armor += int(current_eq['chestplate']['armor'])
    curr_armor += int(current_eq['leggings']['armor'])
    curr_armor += int(current_eq['boots']['armor'])
    curr_armor += int(current_eq['shield']['armor'])
    return curr_armor


def get_damage(current_eq):
    return int(current_eq['sword']['damage'])


def get_price(current_eq):
    return int(current_eq['price'])


if __name__ == '__main__':
    # Generowanie nowej bazy o 6*1000 elementach
    # generate_new_records(1000)

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

    # Początkowe losowe wartości dla bestEQ
    bestEQ = find_new_random_eq()

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
    print("Best EQ found:")
    print(" "+str(bestEQ))
    print(" Armor: "+str(get_armor(bestEQ)))
    print(" Damage: "+str(get_damage(bestEQ)))
    print(" Price: "+str(get_price(bestEQ)))
    print("Enemy EQ:")
    print(" Armor: "+str(enemy['armor']))
    print(" Damage: "+str(enemy['damage']))
