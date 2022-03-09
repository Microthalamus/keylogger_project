from cryptography.fernet import Fernet

encrypt_clip = "encrypt_clip.txt"
encrypt_sys = "encrypt_sys.txt"
encrypt_key = "encrypt_key.txt"
encrypted_files = [encrypt_key, encrypt_clip, encrypt_key]
count = 0

key = ""

for d in encrypted_files:
    for e in encrypted_files:
        with open(encrypted_files[count], 'rb') as file:
            data = file.read()
        fernet = Fernet(key)
        decrypt_data = fernet.decrypt(data)

        with open(encrypted_files[count], 'wb') as file:
            file.write(decrypt_data)
        count += 1