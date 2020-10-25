from hashlib import sha256
import os.path

while True:
    if os.path.isfile("data_file.txt"):
        print("Enter your PIN:")
        provided_pin = str(input())
        with open("data_file.txt", "r+") as file:
            pin_in_hash = file.read()
            file.close()
        if pin_in_hash == sha256(provided_pin.encode("utf-8")).hexdigest():
            print("Padlock open")
            break
        else:
            print("Provided PIN is incorrect")
    else:
        print("Set new PIN for your padlock:")
        pin = str(input())
        print("Enter PIN again:")
        retype_pin = str(input())
        if pin == retype_pin:
            print("PIN was set successfully")
            with open("data_file.txt", "w+") as file:
                file.write(sha256(pin.encode("utf-8")).hexdigest())
                file.close()
                break
        else:
            print("Provided PINS differs")
