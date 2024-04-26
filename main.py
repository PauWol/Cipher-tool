from ciphers import decrypt_caesar_all, caesar_cipher_encrypt, decrypt_substitution_all, substitution_cipher_encrypt
from process import has_meaning_partly
import random
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    print(Fore.BLUE + "Welcome to the Cipher Tool!" + Style.RESET_ALL)
    while True:
        print("\nOptions:")
        print("1. " + Fore.GREEN + "Encrypt with Caesar Cipher" + Style.RESET_ALL)
        print("2. " + Fore.GREEN + "Encrypt with Substitution Cipher" + Style.RESET_ALL)
        print("3. " + Fore.RED + "Decrypt with Caesar Cipher" + Style.RESET_ALL)
        print("4. " + Fore.RED + "Decrypt with Substitution Cipher" + Style.RESET_ALL)
        print("5. " + Fore.YELLOW + "Decrypt Auto Mode" + Style.RESET_ALL)
        print("6. " + Fore.MAGENTA + "Exit" + Style.RESET_ALL)
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            plaintext = input("Enter the text to encrypt with Caesar Cipher: ")
            shift = int(input("Enter the shift value (1-26): "))
            ciphertext = caesar_cipher_encrypt(plaintext, shift)
            print(Fore.CYAN + "Encrypted text:", ciphertext + Style.RESET_ALL)

        elif choice == '2':
            plaintext = input("Enter the text to encrypt with Substitution Cipher: ")
            shift = random.randint(1, 26)
            ciphertext = substitution_cipher_encrypt(plaintext, shift)
            print(Fore.CYAN + "Encrypted text:", ciphertext + Style.RESET_ALL)

        elif choice == '3':
            ciphertext = input("Enter the text to decrypt with Caesar Cipher: ")
            shift = int(input("Enter the shift value (1-26): "))
            decrypted = decrypt_caesar_all(ciphertext)
            print(Fore.CYAN + "Possible decrypted texts:")
            for text in decrypted:
                print(text)

        elif choice == '4':
            ciphertext = input("Enter the text to decrypt with Substitution Cipher: ")
            decrypted = decrypt_substitution_all(ciphertext)
            print(Fore.CYAN + "Possible decrypted texts:")
            for text in decrypted:
                print(text)

        elif choice == '5':
            ciphertext = input("Enter the text to decrypt with Auto Mode: ")
            decrypted_caesar = decrypt_caesar_all(ciphertext)
            decrypted_substitution = decrypt_substitution_all(ciphertext)
            print(Fore.CYAN + "Possible decrypted texts with Caesar Cipher:")
            print(has_meaning_partly(decrypted_caesar))
            print(Fore.CYAN + "Possible decrypted texts with Substitution Cipher:")
            print(has_meaning_partly(decrypted_substitution))

        elif choice == '6':
            print(Fore.MAGENTA + "Goodbye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 6." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
