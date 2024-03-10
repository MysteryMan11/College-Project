import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="pink")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Food Classification using Machine Learning")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('crop5.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text=" Contact Page",font=("Times New Roman", 30, 'bold'),
                    background="#006400", fg="white", width=62, height=2)
label_l1.place(x=0, y=0)

img = Image.open('oral.jpg')
img = img.resize((100,70), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=40, y=10)

# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

label_l2 = tk.Label(root, text="___ Contact us ___",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="black", width=58, height=3)
label_l2.place(x=0, y=90)

img1 = Image.open('m1.jpg')
img1 = img1.resize((715,460), Image.ANTIALIAS)
logo_image1 = ImageTk.PhotoImage(img1)

logo_label1 = tk.Label(root, image=logo_image1)
logo_label1.image = logo_image1
logo_label1.place(x=1, y=231)


# label_l2 = tk.Label(root, text="___ Contact us ___",font=("Times New Roman", 20, 'bold'),
#                     background="#006400", fg="white", width=48, height=2)
# label_l2.place(x=800, y=300)

frame_alpr = tk.LabelFrame(root, text=" --Contact us-- ", width=555, height=400, bd=5, font=('times', 14,'italic'),bg="brown", fg="white")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=745, y=295)


label_l2 = tk.Label(frame_alpr, text="********** \n Call us \n (+91 9876553311,+91 3535353535) \n \n Location \n Pune, Maharashtra \n \n Email - bitmap@gmail.com \n \n  **********",font=("Times New Roman", 20, 'italic'),
                    background="brown", fg="white")
label_l2.place(x=70, y=40)

# label_l2 = tk.Text(root,font=("Times New Roman", 15, 'italic'),
#                     background="#006400", fg="white", width=77, height=14)
# label_l2.place(x=800, y=353)



# Fact=""" 
# *****************************************************************************
        
#         Motivation for this System comes from the agricultural point of view that there is a lot of work for the farmers to be done manually. 
        
#         developing this System is as we say every part of world is developing but we can see that there is no such big achievement or development in soil or crop related issues.
       
#         So we can give preference to this soil field and if we suggest suitable crop to farmers then it is beneficial for them.

# *****************************************************************************
# """

# label_l2.insert(tk.END, Fact)

# def reg():
#     from subprocess import call
#     call(["python","registration.py"])

def home():
    from subprocess import call
    call(["python","GUI_Main.py"])

def window():
  root.destroy()
  
    
# def about():
#     from subprocess import call
#     call(["python","aboutus.py"])
    
    
button1 = tk.Button(root, text="Home", command=home, width=10, height=1,font=('times', 15, ' bold'), bg="#006400", fg="white")
button1.place(x=865, y=245)

button3 = tk.Button(root, text="Exit",command=window,width=10, height=1,font=('times', 15, ' bold '), bg="red", fg="white")
button3.place(x=1010, y=245)
# button2 = tk.Button(label_l1, text="About us",command=about,width=12, height=1,font=('times 15 bold underline'), bd=0,bg="#006400", fg="white")
# button2.place(x=1310, y=50)

# button4 = tk.Button(label_l1, text="Contact us", command=con, width=12, height=1,font=('times 15 bold underline'),bd=0,bg="#006400", fg="white")
# button4.place(x=1430, y=50)



# button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
# button1.place(x=150, y=110)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)


label_l1 = tk.Label(root, text="** Crop Predication System @ 2021 by Bitmap Technology **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=2)
label_l1.place(x=0, y=800)


root.mainloop()