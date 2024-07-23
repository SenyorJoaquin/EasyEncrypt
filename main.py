from cryptography.fernet \
    import Fernet

Encryption_key = b'YqTB_howySGJEtWqDYMaES51iJkk5O7z4ENQ_6zWCiY='

cipher = Fernet(Encryption_key)

print(" EasyEncrypt by Joaquin Tolentino is not for commercial use, malicious use, nor to be used for personal gains."
      "\n Even though the program itself is already complete, Further development is still needed."
      "\n Use with CAUTION and DO NOT test using IMPORTANT Files. Open ReadMe file for usage instructions.\n \n")

print("▄███▄   ██      ▄▄▄▄▄ ▀▄    ▄ ▄███▄      ▄   ▄█▄    █▄▄▄▄ ▀▄    ▄ █ ▄▄     ▄▄▄▄▀")
print("█▀   ▀  █ █    █     ▀▄ █  █  █▀   ▀      █  █▀ ▀▄  █  ▄▀   █  █  █   █ ▀▀▀ █")
print("██▄▄    █▄▄█ ▄  ▀▀▀▀▄    ▀█   ██▄▄    ██   █ █   ▀  █▀▀▌     ▀█   █▀▀▀      █")
print("█▄   ▄▀ █  █  ▀▄▄▄▄▀     █    █▄   ▄▀ █ █  █ █▄  ▄▀ █  █     █    █        █")
print("▀███▀      █           ▄▀     ▀███▀   █  █ █ ▀███▀    █    ▄▀      █      ▀")
print("          █                           █   ██         ▀              ▀")
print("         ▀")

user_file = input("What's the name of the file you want to encrypt: ")
encrypt_decrypt = input("Do you want to encrypt or decrypt? [E/D] ")

with open(user_file, "rb") as ef:
    data = ef.read()

if encrypt_decrypt == "E":
    confirm1 = input("Are you sure you want to encrypt the file? [Yes/No]")
    if confirm1 == 'Yes':
        encrypted_data = cipher.encrypt(data)
        with open(user_file + ".encrypted", "wb") as ef:
            ef.write(encrypted_data)
    else:
        exit()


elif encrypt_decrypt == "D":

    confirm2 = input("Are you sure you want to decrypt the file? [Yes/No]")
    if confirm2 == 'Yes':
        decrypted_data = cipher.decrypt(data)
        with open(user_file + ".decrypted", 'wb') as df:
            df.write(decrypted_data)
    else:
        exit()

else:
    print("Invalid response, Do you want to encrypt or decrypt? [E/D] (case sensitive)")
