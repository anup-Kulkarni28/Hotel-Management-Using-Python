from tkinter import*
from PIL import Image,ImageTk 
from customer import Cust_Window
from room import Roombooking
from details import DetailsRoom



class HotelManagementSystem:
        def __init__(self,root):
                self.root = root
                self.root.title("Hotel Management System")
                self.root.geometry("1500x800")

###############################1st image #########################
                img1 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\hotel1.png")
                img1=img1.resize((1500,140),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                lbl = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
                lbl.place(x=0,y=0,width=1500,height=140)


##################################logo###############################
                img2 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\logohotel.png")
                img2=img2.resize((250,140),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lbl = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
                lbl.place(x=0,y=0,width=230,height=140)
###############################Title###################################
                lbl_title=Label(self.root,text="HOTEL MANAGMENT SYSTEM",font=("times new roman bold",40),bg='black',fg="gold",bd=4,relief=RIDGE)
                lbl_title.place(x=0,y=140,width=1500,height=50)

                #####################main frame#########################

                main_frame = Frame(self.root,bd=4,relief=RIDGE)
                main_frame.place(x=0,y=190,width=1500,height=620)


                ########################Menu############################
                lbl_menu=Label(main_frame,text="MENU",font=("times new roman bold",20),bg='black',fg="gold",bd=4,relief=RIDGE)
                lbl_menu.place(x=0,y=0,width=230)

                ########################Button Frame####################
                button_frame = Frame(main_frame,bd=4,relief=RIDGE)
                button_frame.place(x=0,y=35,width=228,height=190)


                cust_button = Button(button_frame,text="CUSTOMER",command=self.cust_details,font=("times new roman bold",14),bg='black',fg="gold",bd=0,width=22,cursor="hand1")
                cust_button.grid(row=0,column=0,pady=1)


                room_button = Button(button_frame,text="ROOM",font=("times new roman bold",14),command=self.roombooking,bg='black',fg="gold",bd=0,width=22,cursor="hand1")
                room_button.grid(row=1,column=0,pady=1)


                details_button = Button(button_frame,command=self.details_room,text="DETAILS",font=("times new roman bold",14),bg='black',fg="gold",bd=0,width=22,cursor="hand1")
                details_button.grid(row=2,column=0,pady=1)


                # report_button = Button(button_frame,text="REPORT",font=("times new roman bold",14),bg='black',fg="gold",bd=0,width=22,cursor="hand1")
                # report_button.grid(row=3,column=0,pady=1)


                # logout_button = Button(button_frame,text="LOGOUT",font=("times new roman bold",14),bg='black',fg="gold",bd=0,width=22,cursor="hand1")
                # logout_button.grid(row=4,column=0,pady=1)


        ###################right side Image##################


                img3 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\slide3.jpg")
                img3=img3.resize((1310,800),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                lbl = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
                lbl.place(x=225,y=0,width=1310,height=800)


        ###############down Images#############################


                img4 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\mypic.jpg")
                img4=img4.resize((230,210),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                lbl = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
                lbl.place(x=0,y=225,width=230,height=210)

                img5 = Image.open(r"C:\Users\kulka\OneDrive\Desktop\Hotel project\hotel_images\hotel_images\khana.jpg")
                img5=img5.resize((230,190),Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                lbl = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
                lbl.place(x=0,y=420,width=230,height=190)

        def cust_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Cust_Window(self.new_window)


        def roombooking(self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooking(self.new_window)

        def details_room(self):
                self.new_window=Toplevel(self.root)
                self.app=DetailsRoom(self.new_window)

































if __name__ =="__main__":
        root=Tk()
        obj = HotelManagementSystem(root)
        root.mainloop()