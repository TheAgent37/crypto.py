from cryptography.fernet import Fernet


print("Welcome to my encryption program!")
print("Currently there is a bug. Saved files updates after exit of the program.\n")

# ? This is the encryption code
def encrypt(key):
    fe = Fernet(key)
    ask_file = input("Select input type: text(t), file(f), back(b): ")

    if ask_file == "t":
        text = input("Enter text for encrypting with random key: ")
        encrypted_text = fe.encrypt(bytes(text, "utf-8"))
        f = open("encrypted.txt", "wb")
        f.write(encrypted_text)
        f.close
        print("Encrypted text will be saved to encrypted.txt\n")
        # return sec()

    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        file = open(f"{path_file}", "rb")
        encrypted_text = fe.encrypt(file.read())
        f = open("encrypted.txt", "wb")
        f.write(encrypted_text)
        f.close
        print("Encrypted text will be saved to encrypted.txt\n")
        # return sec()

    elif ask_file == "b":
        return main()

    else:
        print("\033[31mInvalid input\033[39m")
        return main()


# ? This is the decryption code
def decrypt():
    key = input("Please enter your key: \n")
    ask_file = input("Select input type: text(t), file(f), back(b): ")
    fe = Fernet(key)

    if ask_file == "t":
        text = input("Enter encrypted test: \n")

        decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        f = open("decrypted.txt", "wb")
        f.write(decrypted_text)
        f.close
        print("Decrypted text will be saved to decrypted.txt")
        # return sec()

    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        file = open(f"{path_file}", "rb")
        decrypted_text = fe.decrypt(file.read())
        f = open("decrypted.txt", "wb")
        f.write(decrypted_text)
        f.close
        print("Decrypted text will besaved to decrypted.txt\n")

    elif ask_file == "b":
        main()

    else:
        print("\033[31mInvalid input\033[39m")
        main()


# ? This is the key generator
def keygen():
    key = Fernet.generate_key()
    print("Your random key is generated!\n")

    ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

    if ask_save == "y":
        f = open("keygen.txt", "wb")
        f.write(key)
        f.close
        print("Your key will be saved to keygen.txt")

    elif ask_save == "n":
        print(f"Here is your key{key}")

    else:
        print("\033[31mInvalid input\033[39m")
        main()


# ? This is the secondary function for program
def sec():
    pass
    ask = input("Do you want to go back yes(y), no(n): ")
    if ask == "y":
        main()

    elif ask == "n":
        print("Exiting...")
        exit()

    else:
        print("\033[31mInvalid input\033[39m")


# ? This is the main function for program
def main():
    choise = input(
        "What you want to do? encrypt(e), decrypt(d), key generator(kg), quit(q): "
    )
    if choise == "e":
        has_key = input("Do you have a key yes(y), no(n) back(b): ")

        if has_key == "y":
            key = bytes(input("Please enter your key: "), "utf-8")
            encrypt(key)

        elif has_key == "n":
            print("Program will generate random key for you.")
            key = Fernet.generate_key()
            f = open("key.txt", "wb")
            f.write(key)
            f.close

            print("Your key will be saved to key.txt")
            encrypt(key)

        elif has_key == "b":
            main()

        else:
            print("\033[31mInvalid input\033[39m")
            main()

    elif choise == "d":
        decrypt()

    elif choise == "kg":
        keygen()

    elif choise == "q":
        exit()
    else:
        print("\033[31mInvalid input\033[39m")
        main()


main()
