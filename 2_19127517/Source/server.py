
# print("Dang cho Client")
# conn, addr = s.accept()
# try:
#     print("Duoc ket noi boi ", addr)
#     while True:
#         data = conn.recv(1024)
#         if data == "":
#             print("Detect client close")
#             break
#         if data == "list all":
#             with open('/Users/jsn/Desktop/file.txt',"rb") as file:
#                 data=file.read(1024)
#             while data:
#                 conn.send(data)
#                 print(f"[DA GUI] {data!r}")
#                 data = file.read(1024)
#                 print("[DA GUI FILE]")
#         if len(data)> 0:
#             print("Server recv: " + data.decode("utf8"))
# except KeyboardInterrupt:
#     conn.close()
#     s.close()
# finally:
#     conn.close()
#     s.close()
# import socket
# import threading
# import os
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     username="root",
#     password="",
#     database ="livescore"
#     )

# mycursor = mydb.cursor()
# mycursor.execute("DROP TABLE IF EXISTS livescore")
# print("da xoa bang livescore")

# mycursor.execute("""CREATE TABLE livescore(id int auto_increment primary key, time varchar(4), nameteam1 varchar(25), nameteam2 varchar(25), score varchar(4), goal int, redcard int, yellowcard int""")
# print("table created")
# sql="INSERT INTO livescore(id, time, nameteam1, nameteam2, score, goal, redcard, yellowcard) values(%s, %s, %s, %s, %s, %s, %s, %s)"

# val=[
#     ('01', '13p', 'Everton', 'Burnley', '1-2', '1', '0', '0'),
#     ('02', '24p', 'Fulham', 'ManchesterCity', '0-3', '0', '0', '0'),
#     ('03', '32p', 'Southampoon', 'Brighton&HoveAlbion','1-2', '1', '0', '0'),
#     ('04', '37p', 'LeicesterCity', 'SheffieldUnited', '5-0', '5', '0', '0')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "[DA LUU]")
# print()

# def searchByID():
#     nextcmd= input('nhap <score [id]> tai day: ')
#     if nextcmd:
#         mycursor.execute("SELECT * FROM livescore l WHERE nextcmd[6:]=l.id")
#         print (l)
# f = os.path.expanduser('/Users/jsn/Desktop/bans.txt')
# l = os.path.expanduser('/Users/jsn/Desktop/file.txt')

# HOST = "127.0.0.1"
# PORT = 65431
# filename="file.txt"

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)







#             msg = message
#             if msg.decode('ascii').startswith('KICK'):
#                 if nicknames[clients.index(client)] == 'admin':
#                     name_to_kick = msg.decode('ascii')[5:]
#                     kick_user(name_to_kick)
#                 else:
#                     client.send("cau lenh bi tu choi".encode('ascii'))
#             elif msg.decode('ascii').startswith('BAN'):
#                 if nicknames[clients.index(client)] == 'admin':
#                     name_to_ban = msg.decode('ascii')[4:]
#                     kick_user(name_to_ban)
#                     with open(f,'a'):
#                         f.write(f'{name_to_ban}\n')
#                     print(f'{name_to_ban} da bi cam')
#                     pass
#                 else:
#                     client.send("cau lenh bi tu choi".encode('ascii'))
#             elif msg.decode('ascii').startswith('exit'):
#                 s.sendall('Thong bao ngung ket noi tu Server gui cho toan bo Client dang co ket noi kha dung')
#                 clients.pop(len(clients)+1)
#                 s.shutdown(socket.SHUT_RDWR)
#                 s.close()
#                 time.sleep(4)
#             elif msg.decode('ascii').startswith("list all"):
#                 #cach1 | show all from .txt
#                 s.send(b"Da nhan yeu cau xem toan bo danh sach")
#                 with open(l,'wb') as file:
#                     print('Dang mo file, xin cho chut..')
#                     print("Dang nhan du lieu.. ")
#                 while True:
#                     scoreLiveLists = file.read()#data=s.recv(1024)
#                     print(f'toan bo ds tran day \n {scoreLiveLists}')
#                     if not scoreLiveLists:
#                         print('Ko phai danh sach scorelive')
#                         break
#                 #cach2
#                 # mycursor.execute("SELECT * FROM livescore")
#                 # myresult = mycursor.fetchall()

#                 # for x in myresult:
#                 #     print(x)
#             elif msg.decode('ascii').startswith('score'):
#                 searchByID()
#             else:










#     with open(f,'r') as f:
#         bans = f.readlines()
#     if nickname+'\n' in bans:
#         client.send('BAN'.encode('ascii'))
#         client.close()
#         #continue

#     if nickname == 'admin':
#         client.send('PASS'.encode('ascii'))
#         password = client.recv(1024).decode('ascii')

#         if password != 'adminpass':
#             client.send('REFUSE'.encode('ascii'))
#             client.close()
#             # continue

# def kick_user():
#     if name in nicknames:
#         name_index = nicknames.index(name)
#         client_to_kick = clients[name_index]
#         clients.remove(client_to_kick)
#         client_to_kick.send('ban bi kick boi admin'.encode('ascii'))
#         client_to_kick.close()
#         nicknames.remove(name)
#         broadcast(f'{name} bi kick boi admin'.encode('ascii'))

# print("server dang lang nghe..")
# receive()
# import socket
# import threading

# h='127.0.0.1'
# p=65434

# server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind((h,p))
# server.listen()

# clients=[]
# nicknames=[]

# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def receive():
#     while True:
#         client, address=server.accept()
#         print(f'da ket noi voi {str(address)}')

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
# import mysql#

def duyet():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s da ket noi" % client_address)
        client.send(bytes("vay tay chao", "utf8"))
        addresses[client] = client_address
        Thread(target=trinhXuLi, args=(client,)).start()
def trinhXuLi(client):
    name = client.recv(1024).decode("utf8")
    welcome = 'xin chao %s' % name
    os.system('sudo python3 /Users/jsn/Desktop/register.py')
    if name == 'admin':
        os.system('sudo python3 /Users/jsn/Desktop/mysql.py')

        client.send(bytes(welcome, "utf8"))
        msg = "%s da co the giao tiep!" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = name
        while True:
            msg = client.recv(1024)
            if msg != bytes("{quit}", "utf8"):
                broadcast(msg, name+": ")
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s da mat ket noi" % name, "utf8"))
                break
    else:
        client.send(bytes(welcome, "utf8"))
        msg = "%s da co the giao tiep!" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = name

        while True:
            msg = client.recv(1024)
            if msg != bytes("{quit}", "utf8"):
                broadcast(msg, name+": ")
            else:
                client.send(bytes("{quit}", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s da mat ket noi" % name, "utf8"))
                break

def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

clients = {}
addresses = {}

h = '127.0.0.1'
p = 12342


SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((h,p))

if __name__ == "__main__":
    SERVER.listen(5)
    print("Dang cho..")
    thre = Thread(target=duyet)
    thre.start()
    thre.join()
    SERVER.close()