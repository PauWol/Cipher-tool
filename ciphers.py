from collections import Counter

def caesar_cipher_encrypt(plaintext, shift):
    """
    Encrypts the plaintext using the Caesar cipher (Vershiebeverfahren).

    Parameters:
    - plaintext (str): The plaintext to be encrypted.
    - shift (int): The number of positions to shift each letter in the alphabet.

    Returns:
    - ciphertext (str): The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine the new character after shifting
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            ciphertext += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    """
    Decrypts the ciphertext encrypted using the Caesar cipher (Vershiebeverfahren).

    Parameters:
    - ciphertext (str): The ciphertext to be decrypted.
    - shift (int): The number of positions the letters were shifted during encryption.

    Returns:
    - plaintext (str): The decrypted plaintext.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine the original character before shifting
            original_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26) + ord('a' if char.islower() else 'A'))
            plaintext += original_char
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    return plaintext

def decrypt_caesar_all(ciphertext):
    r = {'method':'caesar','ciphertext':{'text':[]}}
    for i in range(26):
        r['ciphertext']['text'].append(caesar_cipher_decrypt(ciphertext,i))
    return r

def substitution_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def substitution_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_substitution_all(ciphertext):
    r = {'method':'caesar','ciphertext':{'text':[]}}
    for i in range(26):
        r['ciphertext']['text'].append(caesar_cipher_decrypt(ciphertext,i))
    return r

def vigenere_cipher_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            key_index = i % key_length
            shift = ord(key[key_index].lower()) - 97
            if plain_text[i].islower():
                encrypted_text += chr((ord(plain_text[i]) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += chr((ord(plain_text[i]) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenere_cipher_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            key_index = i % key_length
            shift = ord(key[key_index].lower()) - 97
            if encrypted_text[i].islower():
                decrypted_text += chr((ord(encrypted_text[i]) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(encrypted_text[i]) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text

def brute_force_caesar_cipher(ciphertext):
    results = []
    for shift in range(26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                else:
                    decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        results.append(decrypted_text)
    return results

def frequency_analysis(ciphertext):
    letter_freq = Counter(ciphertext.lower())
    most_common_letter = letter_freq.most_common(1)[0][0]
    shift = ord(most_common_letter) - ord('e')  # Assuming 'e' is the most common letter in English
    return letter_freq , most_common_letter , shift

def known_plaintext_attack(plaintext, ciphertext):
    key = ""
    for i in range(len(ciphertext)):
        key_char = chr(((ord(ciphertext[i]) - ord(plaintext[i])) % 26) + ord('A'))
        key += key_char
    return key

def most_likely_letter(ciphertext):
    letter_freq = Counter(ciphertext.lower())
    most_common_letter = letter_freq.most_common(1)[0][0]
    return most_common_letter