import nfc
import binascii
import time
from datetime import datetime
import user_list
import os

if not os.path.exists("log"):
    os.mkdir("log")


clf = nfc.ContactlessFrontend('usb')
print(clf, "\n")

users = user_list.users

while True:
    print("Please scan your card....")
    
    tag = clf.connect(rdwr={'targets': ['212F', '424F'], 'on-connect': lambda tag: False})
    id=binascii.hexlify(tag.idm)
    id = id.decode()
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    if id in users.keys():
        username = users[id]
        message = f"Hi, {username} !"
    else:
        username = "unknown"
        message = f"You are not registered."

    print(now, id, username)
    print(message, "\n")
    
    today = now.strftime("%Y_%m_%d")
    filepath = f"log/{today}.txt"
    
    if os.path.exists(filepath):
        mode="a"
    else:
        mode="x"
    
    f = open(filepath, mode)
    f.write(f"{now_str}\t{username}\n")
    f.close()
    time.sleep(3)