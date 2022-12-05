# Ceaser Ciphering
import string
from random import randint

alphabets = list(string.ascii_lowercase)
ALPHABETS = list(string.ascii_uppercase)
numbers = [str(i) for i in range(10)]
characters = ['!', '"', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '@', '#', '\\', ',', '.', '<', '>', '?', '/', '~', '£', ' ']
unicodes = ["\u20A5", "\u20A7"]

spec = ['`', '¬', '|']
key_spec = ['[', ']', '{', '}', ';', ':', '\'', '@', '#']
key_spec2 = [i for i in range(1,10)]


def ceaser_cipher(word):
    KEY = randint(1, 9)
    ciphered = spec[randint(0, len(spec)-1)]
    
    for i in word:
        if i in alphabets:
            i = alphabets[(alphabets.index(i) + KEY) % 26]
        elif i in ALPHABETS:
            i = ALPHABETS[(ALPHABETS.index(i) + KEY) % 26]
        elif i in numbers:
            i = numbers[(numbers.index(i) + KEY) % 10]
        elif i in characters:
            i = characters[(characters.index(i) + KEY) % len(characters)]
        elif i == "\n":
        	i = unicodes[randint(0, len(unicodes) - 1)]
        else:
            pass
        ciphered += i
    KEY = key_spec[(key_spec2.index(KEY) + 7) % 9]
    ciphered += str(KEY)
    return ciphered

def ceaser_decipher(word):
    if word[0] not in spec:
        raise ValueError ("Cannot decipher, word not in cipher")

    KEY = word[-1]
    KEY = key_spec2[(key_spec.index(KEY) - 7) % 9]

    word = word[1:-1]
    deciphered =""

    for i in word:
        if i in alphabets:
            i = alphabets[(alphabets.index(i) - KEY) % 26]
        elif i in ALPHABETS:
            i = ALPHABETS[(ALPHABETS.index(i) - KEY) % 26]
        elif i in numbers:
            i = numbers[(numbers.index(i) - KEY) % 10]
        elif i in characters:
            i = characters[(characters.index(i) - KEY) % len(characters)]
        elif i in unicodes:
        	i = "\n"
        else:
            pass
        deciphered += i
    return deciphered

 