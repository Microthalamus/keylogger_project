from cryptography.fernet import Fernet

key = Fernet.generate_key()
file = open("file_encryption", "wb")
file.write(key)
file.close()