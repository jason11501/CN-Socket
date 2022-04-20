# import socket

# HOST = "127.0.0.1"  # IP adress server
# PORT = 65433        # port is used by the server

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = (HOST, PORT)
# print("Client ket noi den server voi port: " + str(PORT))
# client.connect(server_address)
# try:
# 	while True:
# 		msg = input('Client: ')
# 		client.sendall(bytes(msg, "utf8"))
# 	# client.sendall(b"This is the message from client")
# except KeyboardInterrupt:
# 	client.close()
# finally:
# 	client.close()



# nickname = input("chon nickname 3 chu cai: ")
# u = os.path.expanduser('/Users/jsn/Desktop/usernames.txt')
# with open(u,'r') as u:
# 	usernameLists = u.readlines()
# while nickname in usernameLists:
# 	ans = input("member or rookie ?: ")
# 	if ans == 'member':
# 		password = input("password?: ")
# 		if password == nickname[5:]:
# 			pass
# 		else:
# 			nickname = input("vui long nhap lai nickname khac: ")
# 	else:
# 		nickname = input("vui long nhap lai nickname khac: ")
# 	print("nickname da ton tai, yeu cau dangKi")

# if nickname not in usernameLists:
# 	with open(u,'a') as u:
# 		u.write(u'{nickname}\n')
# 		print(u'[DA LUU]{nickname} vao usernames.txt')

# def write():
# 	while True:
# 		if stop_thread:
# 			break
# 		message = f'{nickname[:3]}: {input("")}'
# 		if message[len(nickname[:3])+2:].startswith('/'):
# 			if nickname == 'admin':
# 				if message[len(nickname[:3])+2:].startswith('/kick'):
# 					client.send(f'KICK {message[len(nickname[:3])+2+6:]}'.encode('ascii'))
# 				elif message[len(nickname[:3])+2:].startswith('/ban'):
# 					client.send(f'BAN {message[len(nickname[:3])+2+5:]}'.encode('ascii'))
# 			else:
# 				print("Cau lenh chi duoc thuc thi duoi quyen admin")
# 		else:
# 			client.send(message.encode('ascii'))
# def receive():
# 	while True:
# 		global stop_thread
# 		if stop_thread:
# 			break
# 		try:
# 			message = client.recv(1024).decode('ascii')
# 			if message == 'NICK':
# 				client.send(nickname.encode('ascii'))
# 				next_message = client.recv(1024).decode('ascii')
# 				if next_message == 'PASS':
# 					client.send(password.encode('ascii'))
# 					if client.recv(1024).encode('ascii') == 'REFUSE':
# 						print("sai mat khau")
# 						stop_thread = True
# 				elif next_message == 'BAN':
# 					print("truy cap bi tu choi vi ban da bi cam")
# 					client.close()
# 					stop_thread = True

# 			else:
# 				print(message)
# 		except:
# 			connected = False
# 			print('[MAT KET NOI] server')
# 			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 			print('[KET NOI LAI] server..')
# 			while not connected:
# 				try:
# 					client.connect(server_address)
# 					connected = True
# 					print('[KET NOI LAI] thanh cong')
# 				except socket.error :
# 					time.sleep(2)




# print("Client ket noi den server voi port: " + str(PORT))
# client.connect(server_address)
# connected = True
# stop_thread = False

# receive_thread = threading.Thread(target = receive)
# receive_thread.start()
# write_thread = threading.Thread(target = write)
# write_thread.start()
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# HOST = "127.0.0.1"
# PORT = 65434

# clientSocket.connect((HOST,PORT))

# window=Tk()
# window.title("ket noi toi "+HOST+":"+str(PORT))

# txtMessages=StringVar()
# txtMessages=Text(window,width=50)
# txtMessages.grid(row=0,column=0,padx=10,pady=10)

# txtYourMessage=Entry(window,width=50)
# txtYourMessage.insert(0,"Go vao day")
# txtYourMessage.grid(row=1,column=0,padx=10,pady=10)

# def send():
# 	clientMessage=txtMessages.get()
# 	txtMessages.insert(END,"\n"+"ban: "+clientMessage)
# 	clientSocket.send(clientMessage.encode("utf-8"))

# btnSendMessage=Button(window,text="gui",width=20,comman=send)
# btnSendMessage.grid(row=2,column=0,padx=10,pady=10)

# def receive():
# 	while True:
# 		serverMessage=clientSocket.recv(1024).decode("utf-8")
# 		print(serverMessage)
# 		txtMessages.insert(END,"\n"+serverMessage)
# recvThread=Thread(target=receive)
# recvThread.daemon=True
# recvThread.start()

# window.mainloop()

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter,os
# import importlib
# moduleName='mysql'
# importlib.import_module(moduleName)










def receive():
	while True:
		try:
			msg = client_socket.recv(BUFSIZ).decode("utf8")
			msg_list.insert(tkinter.END, msg)
		except OSError:
			break
def send(event=None):
	msg = my_msg.get()
	my_msg.set("")
	client_socket.send(bytes(msg, "utf8"))
	if msg == "{quit}":
		client_socket.close()
		top.quit()
	
	nextcmd=input('Go lenh yeu cau server(list all/goal [id])\n (LUU Y: database đang rỗng, có search cũng vô ích =))), phải insert dữ liệu với quyền admin trước khi làm điều này): ')#
	if nextcmd=='list all':#
		os.system('sudo python3 /Users/jsn/Desktop/listallcmdorsearchcmd.py')#
	elif nextcmd[:4]=='goal':
		os.system('sudo python3 /Users/jsn/Desktop/listallcmdorsearchcmd.py')
	# client_socket.sendall(bytes(nextcmd, "utf8"))#
	# if msg[:5] == "score ":

def on_closing(event=None):
	my_msg.set("{quit}")
	send()

top = tkinter.Tk()
top.title("Giao tiep")

messages_frame = tkinter.Frame(top)

my_msg = tkinter.StringVar()
my_msg.set("Đổi dòng này thành tên")

scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Gui", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)
HOST = '127.0.0.1'
PORT = 12342
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()