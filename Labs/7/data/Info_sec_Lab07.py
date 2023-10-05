import random
import string

def rusOrAng(text):
    if text[0] in string.ascii_lowercase:
        return string.ascii_lowercase+string.digits
    else:
        return "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"+string.digits

def key_create(s, alf):
    k = "".join(random.choice(alf) for i in range(s))
    return k

def Hex_coder(cod):
    return " ".join(hex(ord(i))[2:] for i in cod)

def string_coder(text, k):
    return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(text, k))

def find_plaintext(text, fragment):
    key_length = len(fragment)
    possible_keys = []
    for i in range(len(text) - key_length + 1):
        key = [chr(ord(c) ^ ord(k)) for c, k in zip(text[i:i + key_length], fragment)]
        intact_plaintext = string_coder(text, key)
        if fragment in intact_plaintext:
            possible_keys.append(''.join(key))
    return possible_keys


plaintext = input("Введите открытый текст: ")
size = len(plaintext)
leng = rusOrAng(plaintext)
key = key_create(size, leng)
print(f"Ключ: {key}", f"Ключ в 16 бит: {Hex_coder(key)}", sep='\n')

ciphertext = string_coder(plaintext, key)
print(f"Зашифрованный текст: {ciphertext}", f"Зашифрованный текст в 16 бит: {Hex_coder(ciphertext)}", sep='\n')

decryptedtext = string_coder(ciphertext, key)
print("Расшифрованный текст:", decryptedtext)

known_fragment = input("Введите фрагмент открытого текста: ")
possible_keys = find_plaintext(ciphertext, known_fragment)
print("Возможные ключи для шифротекста:", possible_keys)
