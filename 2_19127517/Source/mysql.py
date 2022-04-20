#import mysql.connector
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
	def __init__(self,root):
		self.root = root
		titlespace = " "
		self.root.title(102* titlespace + "LIVESCORE")
		self.root.geometry("1280x800+300+0")
		self.root.resizable(width = False, height = False)

		MainFrame = Frame(self.root, bd=10,width=700,height=1000,relief=RIDGE,bg='cadet blue')
		MainFrame.grid()

		TitleFrame=Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
		TitleFrame.grid(row=0,column=0)
		TopFrame3=Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
		TopFrame3.grid(row=1,column=0)

		LeftFrame=Frame(TopFrame3,bd=5,width=770,height=400,padx=2,bg='cadet blue',relief=RIDGE)
		LeftFrame.pack(side=LEFT)
		LeftFrame1=Frame(LeftFrame,bd=5,width=600,height=180,padx=2,pady=4,relief=RIDGE)
		LeftFrame1.pack(side=TOP,padx=0,pady=0)

		RightFrame1=Frame(TopFrame3,bd=5,width=100,height=400,padx=2,bg='cadet blue',relief=RIDGE)
		RightFrame1.pack(side=RIGHT)
		RightFrame1a=Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
		RightFrame1a.pack(side=TOP)

		id=StringVar()
		time=StringVar()
		nameteam1=StringVar()
		nameteam2=StringVar()
		score=StringVar()
		goal=StringVar()
		redcard=StringVar()
		yellowcard=StringVar()

		def iExit():
			iExit=tkinter.messagebox.askyesno("LIVESCORE","Ban co muon thoat?")
			if iExit>0:
				root.destroy()
				return
		def addLivescore():
			if id.get()=="" or time.get=="":
				tkinter.messagebox.showerror("LIVESCORE","vui long nhap dung du lieu")
			else:
				mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
				mycursor = mydb.cursor()
				
				mycursor.execute("INSERT INTO livescore values(%s, %s, %s, %s, %s, %s, %s, %s)",(
				
				id.get(),
				time.get(),
				nameteam1.get(),
				nameteam2.get(),
				score.get(),
				goal.get(),
				redcard.get(),
				yellowcard.get()
				))







				id_info=id.get()
				time_info=time.get()
				nameteam1_info=nameteam1.get()
				nameteam2_info=nametam2.get()
				score_info=score.get()
				goal_info=goal.get()
				redcard_info=redcard.get()
				yellowcard_info=yellowcard.get()

				outfile=open('/Users/jsn/Desktop/livescore.txt','a')#
				outfile.write(id_info+' ')
				outfile.write(time_info+' ')
				outfile.write(nameteam1_info+' ')
				outfile.write(nameteam2_info+' ')
				outfile.write(score_info+' ')
				outfile.write(goal_info+' ')
				outfile.write(redcard_info+' ')
				outfile.write(yellowcard_info+'\n')
				outfile.close()









				mydb.commit()
				mydb.close()
				tkinter.messagebox.showinfo("LIVESCORE","[DA LUU] nhap lieu thanh cong")
		def DisplayData():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
			mycursor.execute("SELECT FROM livescore")
			myresult = mycursor.fetchall()
			if len(myresult)!=0:
				self.livescore_records.delete(*self.livescore_records.get_children())
				for row in result:
					self.livescore_records.insert('',END,values=row)
			mydb.commit()
			mydb.close()

		def livescoreInfo():
			viewInfo=self.livescore_records.focus()
			learnerData=self.livescore_records.item(viewInfo)
			row=learnerData['values']
			id.set(row[0])
			time.set(row[1])
			nameteam1.set(row[2])
			nameteam2.set(row[3])
			score.set(row[4])
			goal.set(row[5])
			redcard.set(row[6])
			yellowcard.set(row[7])
		def updateTime():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
				
			mycursor.execute("UPDATE livescore set time=%s WHERE id=%s",(
			time.get(),
			id.get()
			))
			mydb.commit()
			mydb.close()
			tkinter.messagebox.showinfo("LIVESCORE","[DA CAP NHAT] thoi gian")
		def updateScore():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
				
			mycursor.execute("UPDATE livescore set score=%s WHERE id=%s",(
			score.get(),
			id.get()
			))
			mydb.commit()
			mydb.close()
			tkinter.messagebox.showinfo("LIVESCORE","[DA CAP NHAT] ti so")
		def updateGoal():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
				
			mycursor.execute("UPDATE livescore set goal=%s WHERE id=%s",(
			goal.get(),
			id.get()
			))
			mydb.commit()
			mydb.close()
			tkinter.messagebox.showinfo("LIVESCORE","[DA CAP NHAT] su kien: ban thang")
		def updateRed():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
				
			mycursor.execute("UPDATE livescore set redcard=%s WHERE id=%s",(
			redcard.get(),
			id.get()
			))
			mydb.commit()
			mydb.close()
			tkinter.messagebox.showinfo("LIVESCORE","[DA CAP NHAT] su kien: the do")
		def updateYellow():
			mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
			mycursor = mydb.cursor()
				
			mycursor.execute("UPDATE livescore set yellowcard=%s WHERE id=%s",(
			yellowcard.get(),
			id.get()
			))
			mydb.commit()
			mydb.close()
			tkinter.messagebox.showinfo("LIVESCORE","[DA CAP NHAT] su kien: the vang")
		def search():
			try:
				mydb = pymysql.connect(host="127.0.0.1",username="root",password="alpine",database ="livescore")
				mycursor = mydb.cursor()
				mycursor.execute("SELECT * FROM livescore WHERE id=%s",id.get())

				row=mycursor.fetchall()

				id.set(row[0])
				time.set(row[1])
				nameteam1.set(row[2])
				nameteam2.set(row[3])
				score.set(row[4])
				goal.set(row[5])
				redcard.set(row[6])
				yellowcard.set(row[7])

				mydb.commit()
			except:
				tkinter.messagebox.showinfo("LIVESCORE","ko tim thay")
			mydb.close()

		self.lbltitle=Label(TitleFrame, font=('arial',40,'bold'),text="LIVESCORE",bd=7)
		self.lbltitle.grid(row=0,column=0,padx=132)

		self.lblid=Label(LeftFrame1, font=('arial',12,'bold'),text="id",bd=7)
		self.lblid.grid(row=1,column=0,sticky=W,padx=5)
		self.entid=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=id)
		self.entid.grid(row=1,column=1,sticky=W,padx=5)

		self.lbltime=Label(LeftFrame1, font=('arial',12,'bold'),text="time",bd=7)
		self.lbltime.grid(row=2,column=0,sticky=W,padx=5)
		self.enttime=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=time)
		self.enttime.grid(row=2,column=1,sticky=W,padx=5)

		self.lblnameteam1=Label(LeftFrame1, font=('arial',12,'bold'),text="nameteam1",bd=7)
		self.lblnameteam1.grid(row=3,column=0,sticky=W,padx=5)
		self.entnameteam1=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=nameteam1)
		self.entnameteam1.grid(row=3,column=1,sticky=W,padx=5)

		self.lblnameteam2=Label(LeftFrame1, font=('arial',12,'bold'),text="nameteam2",bd=7)
		self.lblnameteam2.grid(row=4,column=0,sticky=W,padx=5)
		self.entnameteam2=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=nameteam2)
		self.entnameteam2.grid(row=4,column=1,sticky=W,padx=5)

		self.lblscore=Label(LeftFrame1, font=('arial',12,'bold'),text="score",bd=7)
		self.lblscore.grid(row=5,column=0,sticky=W,padx=5)
		self.entscore=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=score)
		self.entscore.grid(row=5,column=1,sticky=W,padx=5)

		self.lblgoal=Label(LeftFrame1, font=('arial',12,'bold'),text="goal",bd=7)
		self.lblgoal.grid(row=6,column=0,sticky=W,padx=5)
		self.entgoal=Entry(LeftFrame1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=goal)
		self.entgoal.grid(row=6,column=1,sticky=W,padx=5)

		self.lblredcard=Label(LeftFrame1, font=('arial',12,'bold'),text="red card",bd=7)
		self.lblredcard.grid(row=7,column=0,sticky=W,padx=5)
		self.cboredcard=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=42,state='readonly',textvariable=redcard)
		self.cboredcard['values']=(' ','0','1')
		self.cboredcard.current(0)
		self.cboredcard.grid(row=7,column=1)

		self.lblyellowcard=Label(LeftFrame1, font=('arial',12,'bold'),text="yellow card",bd=7)
		self.lblyellowcard.grid(row=8,column=0,sticky=W,padx=5)
		self.cboyellowcard=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=42,state='readonly',textvariable=yellowcard)
		self.cboyellowcard['values']=(' ','0','1')
		self.cboyellowcard.current(0)
		self.cboyellowcard.grid(row=8,column=1)

		scroll_x=Scrollbar(LeftFrame,orient=HORIZONTAL)

		self.livescore_records=ttk.Treeview(LeftFrame,height=14,columns=("id", "time", "nameteam1", "nameteam2", "score", "goal", "redcard", "yellowcard"),xscrollcommand=scroll_x.set)

		scroll_x.pack(side=RIGHT,fill=Y)

		self.livescore_records.heading("id", text="Live Score ID")
		self.livescore_records.heading("time", text="Time")
		self.livescore_records.heading("nameteam1", text="Name team 1")
		self.livescore_records.heading("nameteam2", text="Name team 2")
		self.livescore_records.heading("score", text="Score")
		self.livescore_records.heading("goal", text="Goal")
		self.livescore_records.heading("redcard", text="Red card")
		self.livescore_records.heading("yellowcard", text="Yellow card")

		self.livescore_records['show']='headings'

		self.livescore_records.column("id", width=70)
		self.livescore_records.column("time", width=70)
		self.livescore_records.column("nameteam1", width=100)
		self.livescore_records.column("nameteam2", width=100)
		self.livescore_records.column("score", width=70)
		self.livescore_records.column("goal", width=100)
		self.livescore_records.column("redcard", width=70)
		self.livescore_records.column("yellowcard", width=70)

		self.livescore_records.pack(fill=BOTH,expand=1)
		self.livescore_records.bind("<ButtonRelease-1>",livescoreInfo)

		self.btnAdd=Button(RightFrame1a, font=('arial',16,'bold'),text="Add",bd=4,pady=1,padx=24,width=8,height=2,command=addLivescore).grid(row=0,column=0,padx=1)
		self.btnSearch=Button(RightFrame1a, font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,width=8,height=2,command=search).grid(row=1,column=0,padx=1)
		self.btnUpdateScore=Button(RightFrame1a, font=('arial',16,'bold'),text="Update score",bd=4,pady=1,padx=24,width=8,height=2,command=updateScore).grid(row=2,column=0,padx=1)
		self.btnUpdateGoal=Button(RightFrame1a, font=('arial',16,'bold'),text="Update goal",bd=4,pady=1,padx=24,width=8,height=2,command=updateGoal).grid(row=3,column=0,padx=1)
		self.btnUpdateRed=Button(RightFrame1a, font=('arial',16,'bold'),text="Update red card",bd=4,pady=1,padx=24,width=8,height=2,command=updateRed).grid(row=4,column=0,padx=1)
		self.btnUpdateYellow=Button(RightFrame1a, font=('arial',16,'bold'),text="Update yellow card",bd=4,pady=1,padx=24,width=8,height=2,command=updateYellow).grid(row=5,column=0,padx=1)
		self.btnExit=Button(RightFrame1a, font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
		self.btnShow=Button(RightFrame1a, font=('arial',16,'bold'),text="list all",bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData).grid(row=7,column=0,padx=1)
		self.btnUpdateTime=Button(RightFrame1a, font=('arial',16,'bold'),text="Update time",bd=4,pady=1,padx=24,width=8,height=2,command=updateTime).grid(row=8,column=0,padx=1)
if __name__=='__main__':
	root=Tk()
	application =ConnectorDB(root)
	root.mainloop()

# mycursor.execute("""CREATE TABLE livescore(id int auto_increment primary key, time varchar(4), nameteam1 varchar(25), nameteam2 varchar(25), score varchar(4), goal int, redcard int, yellowcard int""")
# print("table created")
# sql="INSERT INTO livescore(id, time, nameteam1, nameteam2, score, goal, redcard, yellowcard) values(%s, %s, %s, %s, %s, %s, %s, %s)"

# val=[
# 	('01', '13p', 'Everton', 'Burnley', '1-2', '1', '0', '0'),
# 	('02', '24p', 'Fulham', 'ManchesterCity', '0-3', '0', '0', '0'),
# 	('03', '32p', 'Southampoon', 'Brighton&HoveAlbion','1-2', '1', '0', '0'),
# 	('04', '37p', 'LeicesterCity', 'SheffieldUnited', '5-0', '5', '0', '0')]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "[DA LUU]")
# print()
# 'list all' || show all from .txt


#'score id'
# def searchByID():
# 	nextcmd= input('nhap <score [id]> tai day: ')
# 	if nextcmd:
# 		mycursor.execute("SELECT * FROM livescore l WHERE nextcmd[6:]=l.id")
# 		print (l)
