from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from mysql.connector import cursor
from time import strftime
from datetime import datetime



class Roombooking:
        def __init__(self,root):
                self.root = root
                self.root.title(" Room Booking ")
                self.root.geometry("1295x550+230+220")

                #####################Variables####################

                self.var_contact = StringVar()
                self.var_checkout = StringVar()
                self.var_checkin = StringVar()
                self.var_roomtype = StringVar()
                self.var_roomavailable = StringVar()
                self.var_meal = StringVar()
                self.var_noofdays = StringVar()
                self.var_paidtax = StringVar()
                self.var_actualtotal = StringVar()
                self.var_total = StringVar()
 

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

                labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("times new roman bold",12),padx=2)
                labelframeleft.place(x=5,y=50,width=425,height=490)
                 
                ################labels and entry######################

                #Customer Contact
                lbl_cust_contact= Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_cust_contact.grid(row=0,column=0,sticky=W)

 
                entry_contact = ttk.Entry(labelframeleft,width=20,textvariable = self.var_contact,font=("arial",12,"bold"))
                entry_contact.grid(row=0,column=1,sticky=W)

                # Fetch Data button

                btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.Fetch_contacts,font=("arial",10),bg="black",fg="gold",width=8)
                btnFetchData.place(x=343,y=4)

                #Check in data
                check_in_data = Label(labelframeleft,text="Check in Data",font=("arial",12),padx=2,pady=6)
                check_in_data .grid(row=1,column=0,sticky=W)

 
                txtcheck_in_data = ttk.Entry(labelframeleft,width=29,textvariable = self.var_checkin,font=("arial",12))
                txtcheck_in_data.grid(row=1,column=1)

                #Check out Data

                lbl_Check_out= Label(labelframeleft,text="Check Out Data",font=("arial",12),padx=2,pady=6)
                lbl_Check_out.grid(row=2,column=0,sticky=W)

 
                txtcmname = ttk.Entry(labelframeleft,width=29,textvariable = self.var_checkout,font=("arial",12))
                txtcmname.grid(row=2,column=1)

                #Room Type
                label_RoomType = Label(labelframeleft,text="Room Type",font=("arial",12),padx=2,pady=6)
                label_RoomType.grid(row=3,column=0,sticky=W)

                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
                my_cursor.execute("select RoomType from details ")
                ide=my_cursor.fetchall()

                combo_RoomType = ttk.Combobox(labelframeleft,textvariable = self.var_roomtype,font=("arial",12),width=27,state="readonly")
                combo_RoomType["value"] =ide
                combo_RoomType.current(0)
                combo_RoomType.grid(row=3,column=1)

                #Available Room 

                lblRoomAvailable= Label(labelframeleft,text="Available Room",font=("arial",12),padx=2,pady=6)
                lblRoomAvailable.grid(row=4,column=0,sticky=W)

 

                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
                my_cursor.execute("select RoomNo from details ")
                rows=my_cursor.fetchall()

                combo_RoomNo = ttk.Combobox(labelframeleft,textvariable = self.var_roomavailable,font=("arial",12),width=27,state="readonly")
                combo_RoomNo["value"] =rows
                combo_RoomNo.current(0)
                combo_RoomNo.grid(row=4,column=1)

                #Meal
                lblMeal= Label(labelframeleft,text="Meal",font=("arial",12),padx=2,pady=6)
                lblMeal.grid(row=5,column=0,sticky=W)

 
                txtMeal = ttk.Entry(labelframeleft,width=29,textvariable = self.var_meal,font=("arial",12))
                txtMeal.grid(row=5,column=1)


                #No of Days
                lblNoOfDays= Label(labelframeleft,text="Number of days : ",font=("arial",12),padx=2,pady=6)
                lblNoOfDays.grid(row=6,column=0,sticky=W)

 
                txtNoOfDays = ttk.Entry(labelframeleft,textvariable = self.var_noofdays,width=29,font=("arial",12))
                txtNoOfDays.grid(row=6,column=1)

                #Paid tax
                lblNoOfDays= Label(labelframeleft,text="Paid Tax",font=("arial",12),padx=2,pady=6)
                lblNoOfDays.grid(row=7,column=0,sticky=W)

 
                txtNoOfDays = ttk.Entry(labelframeleft,textvariable = self.var_paidtax,width=29,font=("arial",12))
                txtNoOfDays.grid(row=7,column=1)

                #Sub Total
                lblNoOfDays= Label(labelframeleft,text="Sub Total",font=("arial",12),padx=2,pady=6)
                lblNoOfDays.grid(row=8,column=0,sticky=W)

 
                txtNoOfDays = ttk.Entry(labelframeleft,textvariable = self.var_actualtotal,width=29,font=("arial",12))
                txtNoOfDays.grid(row=8,column=1)

                #Total Cost
                lblNoOfDays= Label(labelframeleft,text="Total Cost",font=("arial",12),padx=2,pady=6)
                lblNoOfDays.grid(row=9,column=0,sticky=W)

 
                txtNoOfDays = ttk.Entry(labelframeleft,textvariable = self.var_total,width=29,font=("arial",12))
                txtNoOfDays.grid(row=9,column=1)
        

        ########################Bill Button##################

                btnBill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",12),bg="black",fg="gold",width=10)
                btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #######################Buttons###########################

                button_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                button_frame.place(x=0,y=400,width=411,height=35)


                btnadd=Button(button_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10)
                btnadd.grid(row=0,column=0,padx=1)

                btnupdate=Button(button_frame,command=self.update,text="Update",font=("arial",12),bg="black",fg="gold",width=10)
                btnupdate.grid(row=0,column=1,padx=1)

                btnDelete=Button(button_frame,text="Delete",command=self.rdelete,font=("arial",12),bg="black",fg="gold",width=10)
                btnDelete.grid(row=0,column=2,padx=1)

                btnReset=Button(button_frame,text="Reset",command=self.reset,font=("arial",12),bg="black",fg="gold",width=10)
                btnReset.grid(row=0,column=3,padx=1)
            

                ################Image##################
                img3 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\bed.jpg")
                img3=img3.resize((520,300),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                lbl = Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
                lbl.place(x=760,y=55,width=520,height=200)


            ###############################Table Frame Search##############


                table_frame=LabelFrame(self.root,bd=2,text="View Details And Search System",relief=RIDGE,font=("arial",12),padx=2)
                table_frame.place(x=435,y=280,width=860,height=260)

                searchbar= Label(table_frame,text="Search By  ",font=("arial",12),fg="black")
                searchbar.grid(row=0,column=0,sticky=W,padx=2)

                self.search_var = StringVar()

                search = ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
                search["value"] =("Contact","Room")
                search.current(0)
                search.grid(row=0,column=1,padx=2)

                self.txt_search=StringVar()

                txtsearch = ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",12))
                txtsearch.grid(row=0,column=2,padx=2)

                btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",12),bg="black",fg="gold",width=10)
                btnsearch.grid(row=0,column=3,padx=1)

                btnShowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",12),bg="black",fg="gold",width=10)
                btnShowall.grid(row=0,column=4,padx=1)

                #######################Show Data Table#################


                details_frame=Frame(table_frame,bd=0,relief=RIDGE)
                details_frame.place(x=0,y=50,width=860,height=180)

                scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)


                self.room_table =ttk.Treeview(details_frame,column=("Contact","Check In","Check Out","Room Type","Room Available","Meal","No of Days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.room_table.xview)
                scroll_y.config(command=self.room_table.yview)

                
                self.room_table.heading("Contact",text="Contact")
                self.room_table.heading("Check In",text="Check In")
                self.room_table.heading("Check Out",text="Check Out")
                self.room_table.heading("Room Type",text="Room Type")
                self.room_table.heading("Room Available",text="Room Available")
                self.room_table.heading("Meal",text="Meal")
                self.room_table.heading("No of Days",text="No of Days")
               
                
                self.room_table["show"]="headings"

                self.room_table.column("Contact",width=100)
                self.room_table.column("Check In",width=100)
                self.room_table.column("Check Out",width=100)
                self.room_table.column("Room Type",width=100)
                self.room_table.column("Room Available",width=100)
                self.room_table.column("Meal",width=100)
                self.room_table.column("No of Days",width=100)
                
                self.room_table.pack(fill=BOTH,expand=1)

                self.fetch_data()
                self.room_table.bind("<ButtonRelease-1>",self.get_cursor)



            #add Data
                
        def add_data(self):
                if self.var_contact.get()=="" or self.var_checkin.get()=="":
                        messagebox.showerror("Error","All fields are mandatory",parent=self.root)
                else:
                        try:


                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomavailable.get(),
                                self.var_meal.get(),
                                self.var_noofdays.get()))
                                
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                
                                messagebox.showinfo("Success","Room Booked")
                        except Exception as es:
                                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)
        ##########Fetch Data#################
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from room ")
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


                self.var_contact.set(row[0]),
                self.var_checkout.set(row[1]),
                self.var_checkin.set(row[2]),
                self.var_roomtype.set(row[3]),
                self.var_roomavailable.set(row[4]),
                self.var_meal.set(row[5]),
                self.var_noofdays.set(row[6])

        ##########Updatae#################
        def update(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error","Please enter mobile number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s,where Contact=%s",(self.var_checkin.get(),self.var_checkout.get(),self.var_roomtype.get(),self.var_roomavailable.get(),self.var_meal.get(),self.var_noofdays.get(),self.var_contact.get()))

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update ","Room details updated successfully",parent=self.root)


        #######Delete###########################
        def rdelete(self):
                cdelete = messagebox.askyesno("Hotel Management System","Do you want to delete this data?",parent=self.root)
                if cdelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        query = "delete from room where Contact=%s"
                        value = (self.var_contact.get(),)
                        my_cursor.execute(query,value)

                else:
                        if not rdelete:
                                return
                
                conn.commit()
                self.fetch_data()
                conn.close()


        ###########Reset######################
        def reset(self):
              
                self.var_contact.set(""),
                self.var_checkin.set(""),
              
                self.var_checkout.set(""),
                self.var_roomtype.set(""),
                self.var_roomavailable.set(""),
                
                self.var_meal.set(""),
                
                self.var_noofdays.set("")

                self.var_total.set("")
                self.var_paidtax.set("")
                self.var_actualtotal.set("")

                
                # x=random.randint(1000,10000)
                # self.var_ref.set(str(x))
######################All Data fetch###################

        def Fetch_contacts(self):
                if self.var_contact.get()=="":
                        messagebox.showerror("Error","Please enter valid phone number",parent=self.root)
                
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        query = ("select Name from customer where Mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        rows=my_cursor.fetchone()


                        if rows==None:
                                messagebox.showerror("Error","Number Not found",parent=self.root)
                        
                        else:
                                conn.commit()
                                conn.close()


                                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                                showDataFrame.place(x=455,y=55,width=300,height=180)

                                lblname=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                                lblname.place(x=0,y=0)


                                lbl=Label(showDataFrame,text=rows,font=("arial",12))
                                lbl.place(x=90,y=0)

                                #Gender
                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                query = ("select Gender from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                rows=my_cursor.fetchone()

                                
                                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                                lblGender.place(x=0,y=30)


                                lbl2=Label(showDataFrame,text=rows,font=("arial",12))
                                lbl2.place(x=90,y=30)

                                #Email
                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                query = ("select Email from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                rows=my_cursor.fetchone()

                                lblEmail =Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                                lblEmail.place(x=0,y=60)


                                lbl3=Label(showDataFrame,text=rows,font=("arial",12))
                                lbl3.place(x=90,y=60)


                                #Country
                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                query = ("select Nationality from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                rows=my_cursor.fetchone()

                                lblCountry =Label(showDataFrame,text="Country:",font=("arial",12,"bold"))
                                lblCountry.place(x=0,y=90)


                                lbl4=Label(showDataFrame,text=rows,font=("arial",12))
                                lbl4.place(x=90,y=90)

                                #Address
                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                query = ("select Address from customer where Mobile=%s")
                                value=(self.var_contact.get(),)
                                my_cursor.execute(query,value)
                                rows=my_cursor.fetchone()

                                lblAddress =Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                                lblAddress.place(x=0,y=120)


                                lbl5=Label(showDataFrame,text=rows,font=("arial",12))
                                lbl5.place(x=90,y=120)


        #####################Search System################
        def search(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
 
                my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%" + str(self.txt_search.get())+ "%'")

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.room_table.delete(*self.room_table.get_children())
                        for i in rows:
                                self.room_table.insert("",END,value=i)
                        conn.commit()
                        
                conn.close()

        def total(self):
                inDate = self.var_checkin.get()
                outDate = self.var_checkout.get()
                inDate = datetime.strptime(inDate,"%d/%m/%Y")
                outDate  = datetime.strptime(outDate,"%d/%m/%Y")
                self.var_noofdays.set(abs(outDate - inDate).days)

                if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)



                elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Single"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)


                elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Luxury"):
                        q1=float(600)
                        q2=float(1000)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)

                elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Double"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)


                elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Duplex"):
                        q1=float(500)
                        q2=float(1000)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)

                
                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                        q1=float(600)
                        q2=float(800)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)


                elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
                        q1=float(300)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)


                elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
                        q1=float(100)
                        q2=float(200)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)

                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                        q1=float(800)
                        q2=float(900)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)

                elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Duplex"):
                        q1=float(800)
                        q2=float(700)
                        q3=float(self.var_noofdays.get())
                        q4=float(q1+q2)
                        q5=float(q3+q4)
                        tax="Rs"+str("%.2f"%((q5)*0.10))
                        st ="Rs"+str("%.2f"%((q5)))
                        tt = "Rs"+str("%.2f"%(q5+((q5)*0.1)))
                        self.var_paidtax.set(tax)
                        self.var_actualtotal.set(st)
                        self.var_total.set(tt)



















































































if __name__ == '__main__':
    root = Tk()
    obj =Roombooking(root)
    root.mainloop()