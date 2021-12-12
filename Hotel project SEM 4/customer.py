from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
# from mysql.connector import cursor


class Cust_Window:
        def __init__(self,root):
                self.root = root
                self.root.title(" Customer ")
                self.root.geometry("1295x550+230+220")

                ###############Variables########
                self.var_ref=StringVar()
                x=random.randint(1000,10000)
                self.var_ref.set(str(x))

                self.var_name=StringVar()
                self.var_mother=StringVar()
                self.var_gender=StringVar()
                self.var_post=StringVar()
                self.var_mobile=StringVar()
                self.var_email=StringVar()
                self.var_nationality=StringVar()
                self.var_address=StringVar()
                self.var_id_proof=StringVar()
                self.var_id_number=StringVar()



                ###############################Title###################################
                lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman bold",15),bg='black',fg="gold",bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1290,height=50)

                ##################################logo###############################
                img2 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\logohotel.png")
                img2=img2.resize((100,40),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lbl = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
                lbl.place(x=5,y=2,width=100,height=40)

                #######################Label Frame######################

                labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman bold",12),padx=2)
                labelframeleft.place(x=5,y=50,width=450,height=490)
                
                ################labels and entry######################
                #custref
                lbl_cust_ref= Label(labelframeleft,text="Customer Reference",font=("arial",12,"bold"),padx=2,pady=6)
                lbl_cust_ref.grid(row=0,column=0,sticky=W)

 
                entry_ref = ttk.Entry(labelframeleft,width=25,state="readonly",textvariable=self.var_ref,font=("arial",12,"bold"))
                entry_ref.grid(row=0,column=1)

                #cust name
                cname= Label(labelframeleft,text="Customer Name",font=("arial",12),padx=2,pady=6)
                cname.grid(row=1,column=0,sticky=W)

 
                txtcname = ttk.Entry(labelframeleft,width=25,textvariable=self.var_name,font=("arial",12))
                txtcname.grid(row=1,column=1)

                #mother name 

                cmothername= Label(labelframeleft,text="Mother's Name",font=("arial",12),padx=2,pady=6)
                cmothername.grid(row=2,column=0,sticky=W)

 
                txtcmname = ttk.Entry(labelframeleft,width=25,textvariable=self.var_mother,font=("arial",12,"bold"))
                txtcmname.grid(row=2,column=1)

                #gender combox
                label_gender = Label(labelframeleft,text="Gender : ",font=("arial",12),padx=2,pady=6)
                label_gender.grid(row=3,column=0,sticky=W)

                gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12),width=23,state="readonly")
                gender["value"] =("Male","Female","Other")
                gender.current(0)
                gender.grid(row=3,column=1)


                #postcode 

                postcode= Label(labelframeleft,text="Post code",font=("arial",12),padx=2,pady=6)
                postcode.grid(row=4,column=0,sticky=W)

 
                txtpostcode = ttk.Entry(labelframeleft,width=25,textvariable=self.var_post,font=("arial",12))
                txtpostcode.grid(row=4,column=1)


                #mobile Number
                mnumber= Label(labelframeleft,text="Mobile Number",font=("arial",12),padx=2,pady=6)
                mnumber.grid(row=5,column=0,sticky=W)

 
                txtmnumber = ttk.Entry(labelframeleft,width=25,textvariable=self.var_mobile,font=("arial",12))
                txtmnumber.grid(row=5,column=1)

                #email
                email= Label(labelframeleft,text="Email",font=("arial",12),padx=2,pady=6)
                email.grid(row=6,column=0,sticky=W)

 
                txtemail = ttk.Entry(labelframeleft,width=25,textvariable=self.var_email,font=("arial",12))
                txtemail.grid(row=6,column=1)

                #Nationality
                nation= Label(labelframeleft,text="Country",font=("arial",12),padx=2,pady=6)
                nation.grid(row=7,column=0,sticky=W)

                nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12),width=23,state="readonly")
                nationality["value"] =("INDIA","UK","USA","Other")
                nationality.current(0)
                nationality.grid(row=7,column=1)


                #idproof type combobox
                idproof= Label(labelframeleft,text="ID proof type",font=("arial",12),padx=2,pady=6)
                idproof.grid(row=8,column=0,sticky=W)

                proof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12),width=23,state="readonly")
                proof["value"] =("Adhar Card","Pan Card","Licence")
                proof.current(0)
                proof.grid(row=8,column=1)


                #id Numbers

                idnumber= Label(labelframeleft,text="ID Number",font=("arial",12),padx=2,pady=6)
                idnumber.grid(row=9,column=0,sticky=W)

 
                txtidnumber = ttk.Entry(labelframeleft,width=25,textvariable=self.var_id_number,font=("arial",12))
                txtidnumber.grid(row=9,column=1)

                #Addresses

                address= Label(labelframeleft,text="Address",font=("arial",12),padx=2,pady=6)
                address.grid(row=10,column=0,sticky=W)

 
                txtaddress = ttk.Entry(labelframeleft,width=25,textvariable=self.var_address,font=("arial",12))
                txtaddress.grid(row=10,column=1)

                ########## BUTTONS ###########################

                button_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                button_frame.place(x=0,y=400,width=412,height=40)


                btnadd=Button(button_frame,text="Add",command=self.add_data,font=("arial",12),bg="black",fg="gold",width=10)
                btnadd.grid(row=0,column=0,padx=1)

                btnupdate=Button(button_frame,text="Update",command=self.update,font=("arial",12),bg="black",fg="gold",width=10)
                btnupdate.grid(row=0,column=1,padx=1)

                btnDelete=Button(button_frame,command=self.cdelete,text="Delete",font=("arial",12),bg="black",fg="gold",width=10)
                btnDelete.grid(row=0,column=2,padx=1)

                btnReset=Button(button_frame,command=self.reset,text="Reset",font=("arial",12),bg="black",fg="gold",width=10)
                btnReset.grid(row=0,column=3,padx=1)


                ###############################Table Frame##############


                table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12),padx=2)
                table_frame.place(x=435,y=50,width=860,height=490)

                searchbar= Label(table_frame,text="Search By  ",font=("arial",12),fg="black")
                searchbar.grid(row=0,column=0,sticky=W,padx=2)

                self.search_var = StringVar()

                search = ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
                search["value"] =("Mobile","Ref")
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


                details_frame=Frame(table_frame,bd=2,relief=RIDGE)
                details_frame.place(x=0,y=50,width=860,height=350)

                scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)


                self.Cust_Details_Table =ttk.Treeview(details_frame,column=("Reference","Name","Mother's Name","Gender","Post Code","Mobile Number","Email","Nationality","ID Proof","ID Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.Cust_Details_Table.xview)
                scroll_y.config(command=self.Cust_Details_Table.yview)

                self.Cust_Details_Table.heading("Reference",text="Ref Number")
                self.Cust_Details_Table.heading("Name",text="Name")
                self.Cust_Details_Table.heading("Mother's Name",text="Mother's Name")
                self.Cust_Details_Table.heading("Gender",text="Gender")
                self.Cust_Details_Table.heading("Post Code",text="Post Code")
                self.Cust_Details_Table.heading("Mobile Number",text="Mobile Number")
                self.Cust_Details_Table.heading("Email",text="Email")
                self.Cust_Details_Table.heading("Nationality",text="Nationality")
                self.Cust_Details_Table.heading("ID Proof",text="ID Proof")
                self.Cust_Details_Table.heading("ID Number",text="ID Number")
                self.Cust_Details_Table.heading("Address",text="Address")
                
                self.Cust_Details_Table["show"]="headings"

                self.Cust_Details_Table.column("Reference",width=100)
                self.Cust_Details_Table.column("Name",width=100)
                self.Cust_Details_Table.column("Mother's Name",width=100)
                self.Cust_Details_Table.column("Post Code",width=100)
                self.Cust_Details_Table.column("Mobile Number",width=100)
                self.Cust_Details_Table.column("Email",width=100)
                self.Cust_Details_Table.column("Nationality",width=100)
                self.Cust_Details_Table.column("ID Proof",width=100)
                self.Cust_Details_Table.column("ID Number",width=100)
                self.Cust_Details_Table.column("Address",width=100)
                self.Cust_Details_Table.column("Gender",width=100)
                



                self.Cust_Details_Table.pack(fill=BOTH,expand=1)
                self.fetch_data()
                self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
                


        def add_data(self):
                if self.var_mobile.get()=="" or self.var_mother.get()=="":
                        messagebox.showerror("Error","All fields are mandatory",parent=self.root)
                else:
                        try:


                                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get() ))

                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                
                                messagebox.showinfo("Success","Customer has been added")
                        except Exception as es:
                                messagebox.showerror("Warning",f"Something went wrong:{str(es)}",parent=self.root)



        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from customer")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                        for i in rows:
                                self.Cust_Details_Table.insert("",END,values=i)
                        conn.commit()
                        conn.close()


        def get_cursor(self,event=""):
                cursor_row = self.Cust_Details_Table.focus()
                content=self.Cust_Details_Table.item(cursor_row)
                row=content["values"]


                self.var_ref.set(row[0]),
                self.var_name.set(row[1]),
                self.var_mother.set(row[2]),
                self.var_gender.set(row[3]),
                self.var_post.set(row[4]),
                self.var_mobile.set(row[5]),
                self.var_email.set(row[6]),
                self.var_nationality.set(row[7]),
                self.var_address.set(row[10]),
                self.var_id_proof.set(row[8]),
                self.var_id_number.set(row[9])



        def update(self):
                if self.var_mobile.get()=="":
                        messagebox.showerror("Error","Please enter mobile number",parent=self.root)
                else:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,ID Proof=%s,ID Number=%s,Address=%s where Ref=%s",(self.var_name.get(),self.var_mother.get(),self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get(),self.var_id_proof.get(),self.var_id_number.get(),self.var_address.get(),self.var_ref.get()))

                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Update ","Details updated successfully",parent=self.root)


        def cdelete(self):
                cdelete = messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
                if cdelete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                        my_cursor=conn.cursor()
                        query = "delete from customer where Ref=%s"
                        value = (self.var_ref.get(),)
                        my_cursor.execute(query,value)

                else:
                        if not cdelete:
                                return
                
                conn.commit()
                self.fetch_data()
                conn.close()



        def reset(self):
                # self.var_ref.set(""),
                self.var_name.set(""),
                self.var_mother.set(""),
                # self.var_gender.set(""),
                self.var_post.set(""),
                self.var_mobile.set(""),
                self.var_email.set(""),
                # self.var_nationality.set(""),
                self.var_address.set(""),
                # self.var_id_proof.set(""),
                self.var_id_number.set("")
                
                x=random.randint(1000,10000)
                self.var_ref.set(str(x))

        def search(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="prince@48",database="world") 
                my_cursor=conn.cursor()
 
                my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%" + str(self.txt_search.get())+ "%'")

                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                        for i in rows:
                                self.Cust_Details_Table.insert("",END,value=i)
                        conn.commit()
                        
                conn.close()        









if __name__ == '__main__':
    root = Tk()
    obj =Cust_Window(root)
    root.mainloop()

