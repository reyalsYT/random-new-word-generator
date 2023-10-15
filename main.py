import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
doubleConsonants = ['bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tr', 'tw']

for i in range(10): # for loop to create 10 outputs
    randomWord = []
    for x in range(random.randint(2, 5)):
        letter = random.randint(0,25)

        if alphabet[letter] in vowels: # check if two vowels printed in a row
            try:
                if randomWord[-1] in vowels:
                    letter = random.randint(0, 20)
                    randomWord.append(consonants[letter])
            except:
                pass

        # no repeat consonants
        if alphabet[letter] in consonants:
            try:
                while alphabet[letter] == randomWord[-1]:
                    letter = random.randint(0, 20)
            except:
                pass
        
        # no consonants in a row
        if alphabet[letter] in consonants and len(randomWord) > 0:
            if randomWord[-1] in consonants:
                letter = random.randint(0, 4)
                randomWord.append(vowels[letter])

        randomWord.append(alphabet[letter])
            
    
    # printing randomWord string
    z = 0
    for letter in randomWord:
        print(randomWord[z], end='')
        z += 1

    print()

    # TODO 
    # why do a's generate in pairs?
