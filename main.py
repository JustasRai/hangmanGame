import random


def get_random_word_from_wordlist():
    wordlist = []
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word


def get_some_letters(word):
    letters = []
    temp = '_' * len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp


def draw_hangman(chances):
    if chances == 0:
        print("----------")
        print("   ( )-|  ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 1:
        print("----------")
        print("   ( )-   ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 2:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("   / \     ")
    elif chances == 3:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("   /       ")
    elif chances == 4:
        print("----------")
        print("   ( )    ")
        print("  - | -    ")
        print("           ")
    elif chances == 5:
        print("----------")
        print("   ( )    ")
        print("    |      ")
        print("           ")
    elif chances == 6:
        print("----------")
        print("   ( )    ")
        print("           ")
        print("           ")


def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    chances = 7
    found = False
    while 1:
        if chances == 0:
            print(f"Pralaimėjai!, žodis buvo: {word}")
            break
        print("=== Spėk žodį ===")
        print(temp, end='')
        print(f"\t(žodis turi {len(word)} raides.)")
        print(f"Gyvybių skaičius: {chances}")
        character = input("Įvesk raidę: ")
        if len(character) > 1 or not character.isalpha():
            print("Rašyk po vieną raidę")
            continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(f"\nLaimėjai !!! Žodis buvo: {word}")
            print(f"Atspėjai iš {7 - chances} karto")
            break
        else:
            draw_hangman(chances)
        print()


print("===== Kartuvių žaidimas =====")
while 1:
    choice = input("Ar nori žaisti kartuves? (y/n): ")
    if 'y' in choice.lower():
        start_hangman_game()
    elif 'n' in choice.lower():
        print('Išeinama...')
        break
    else:
        print("Įvestas netinkamas simbolis...Bandyk vėl")
    print("\n")
