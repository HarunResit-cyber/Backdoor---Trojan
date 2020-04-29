import os
import socket
import platform

s = socket.socket()
port = 8080
host = input(str("Please enter the server's host: "))
s.connect((host,port))
print("\nConnected to the server\n")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved! \n")
    if command == "view_cwd":
        files = os.getcwd()
        s.send(files.encode())
        print("")
        print("Command has been executed")
        print("")
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed")
        print("")
    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sended succesufly")
        print("")
    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed")
        print("")
    elif command == "send_file":
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()
    else:
        print("Error: Command didn't worked!")
