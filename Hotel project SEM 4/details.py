from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from mysql.connector import cursor
from time import strftime
from datetime import datetime



class DetailsRoom:
        def __init__(self,root):
                self.root = root
                self.root.title(" Room Booking ")
                self.root.geometry("1295x550+230+220")
            
                ###############################Title###################################
                lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman bold",15),bg='black',fg="gold",bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1290,height=50)

                ##################################logo###############################
                img2 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\logohotel.png")
                img2=img2.resize((100,40),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lbl = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
                lbl.place(x=5,y=2,width=100,height=40)
                
                #######################Label Frame######################

                labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
                labelframeleft.place(x=5,y=50,width=540,height=350)

                #Floor
                lbl_floor= Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_floor.grid(row=0,column=0,sticky=W)

                self.var_floor=StringVar()


                entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",12,"bold"))
                entry_floor.grid(row=0,column=1,sticky=W)

                #Room No
                lbl_RoomNo= Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_RoomNo.grid(row=1,column=0,sticky=W)

                self.var_roomNo = StringVar()

 
                entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=("arial",12,"bold"))
                entry_RoomNo.grid(row=1,column=1,sticky=W)

                #Room Type
                lbl_RoomType= Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_RoomType.grid(row=2,column=0,sticky=W)

                self.var_RoomType = StringVar()
 
                entry_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",12,"bold"))
                entry_RoomType.grid(row=2,column=1,sticky=W)


        #########################buttons###################
                button_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                button_frame.place(x=0,y=200,width=411,height=35)


                btnadd=Button(button_frame,command=self.add_data,text="Add",font=("arial",12),bg="black",fg="gold",width=10)
                btnadd.grid(row=0,column=0,padx=1)

                btnupdate=Button(button_frame,command=self.update,text="Update",font=("arial",12),bg="black",fg="gold",width=10)
                btnupdate.grid(row=0,column=1,padx=1)

                btnDelete=Button(button_frame,command=self.rdelete,text="Delete",font=("arial",12),bg="black",fg="gold",width=10)
                btnDelete.grid(row=0,column=2,padx=1)

                btnReset=Button(button_frame,command=self.reset,text="Reset",font=("arial",12),bg="black",fg="gold",width=10)
                btnReset.grid(row=0,column=3,padx=1)

###############################Table Frame Search##############


                table_frame=LabelFrame(self.root,bd=2,text="Show Room details",relief=RIDGE,font=("arial",12,"bold"),padx=2)
                table_frame.place(x=600,y=55,width=600,height=350)

                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


                self.room_table =ttk.Treeview(table_frame,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)

                 
                self.room_table.heading("Floor",text="Floor")
                self.room_table.heading("RoomNo",text="Room No")
                self.room_table.heading("RoomType",text="Room Type")
                
               
                
                self.room_table["show"]="headings"

                self.room_table.column("Floor",width=100)
                self.room_table.column("RoomNo",width=100)
                self.room_table.column("RoomType",width=100)
               
                
                self.room_table.pack(fill=BOTH,expand=1)
                self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()

        def add_data(self):
                if self.var_floor.get()=="" or self.var_RoomType.get()=="":
                        messagebox.showerror("Error","All fields are mandatory",parent=self.root)
                else:
                        try:


                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                self.var_floor.get(),
                                self.var_roomNo.get(),
                                self.var_RoomType.get(),
                                ))
                                
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                
                                messagebox.showinfo("Success","New Room added")
                        except Exception as es:
                                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)


        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from details ")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.room_table.delete(*self.room_table.get_children())
                        for i in rows:
                                self.room_table.insert("",END,values=i)
                        conn.commit()
                        conn.close()



        def get_cursor(self,event=""):
                cursor_row = self.room_table.focus()
                content=self.room_table.item(cursor_row)
                row=content["values"]


                self.var_floor.set(row[0]),
                self.var_roomNo.set(row[1]),
                self.var_RoomType.set(row[2]),

         ##########Updatae#################
        def update(self):
                if self.var_floor.get()=="":
                        messagebox.showerror("Error","Please enter Floor number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        my_cursor.execute("update details set Floor=%s,RoomType=%s,where RoomNo = %s",(self.var_floor.get(),self.var_RoomType.get(),self.var_roomNo.get()))

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update ","New Room details updated successfully",parent=self.root)
                

        #######Delete###########################
        def rdelete(self):
                cdelete = messagebox.askyesno("Hotel Management System","Do you want to delete this Room data?",parent=self.root)
                if cdelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        query = "delete from details where RoomNo=%s"
                        value = (self.var_roomNo.get(),)
                        my_cursor.execute(query,value)

                else:
                        if not rdelete:
                                return
                
                conn.commit()
                self.fetch_data()
                conn.close()


        def reset(self):
              
                self.var_floor.set(""),
                self.var_roomNo.set(""),
                self.var_RoomType.set(""),
        
    












































































if __name__ == '__main__':
    root = Tk()
    obj =DetailsRoom(root)
    root.mainloop()