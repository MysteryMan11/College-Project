import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title(" Food Classification")

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
label_l1 = tk.Label(root, text=" Food Classification",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=64, height=2)
label_l1.place(x=0, y=0)

img = Image.open('r.jpg')
img = img.resize((100,70), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=25, y=10)

# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

label_l2 = tk.Label(root, text="___ About us ___",font=("Times New Roman", 30, 'bold'),
                    background="#EEEE00", fg="black", width=60, height=3)
label_l2.place(x=0, y=90)

img1 = Image.open('l1.png')
img1 = img1.resize((701,455), Image.ANTIALIAS)
logo_image1 = ImageTk.PhotoImage(img1)

logo_label1 = tk.Label(root, image=logo_image1)
logo_label1.image = logo_image1
logo_label1.place(x=1, y=230)


label_l2 = tk.Label(root, text="___ Food Classification ___",font=("Times New Roman", 20, 'bold'),
                    background="#006400", fg="white", width=40, height=2)
label_l2.place(x=706, y=232)
label_l2 = tk.Text(root,font=("Times New Roman", 15, 'italic'),
                    background="brown", fg="white", width=64, height=17)
label_l2.place(x=706, y=301)



Fact=""" 
*****************************************************************************
        
        Motivation for this System comes  Researchers can use the data collected by the system to study trends and patterns in eating habits.
        \n  Users can receive personalized recommendations for healthier food choices based on the classification results.
*****************************************************************************
"""

label_l2.insert(tk.END, Fact)

# def reg():
#     from subprocess import call
#     call(["python","registration.py"])
#     root.destroy()

def home():
    from subprocess import call
    call(["python","GUI_Main.py"])
    
    
def window():
  root.destroy()
  
  
def con():
    from subprocess import call
    call(["python","contact_us.py"])
  
# def about():
#     from subprocess import call
#     call(["python","about_us.py"])
    
    
    
button1 = tk.Button(label_l1, text="Home", command=home, width=6, height=1,font=('times 15 bold underline'),bd=0, bg="#006400", fg="white")
button1.place(x=180, y=50)

button2 = tk.Button(label_l1, text="Exit",command=window,width=6, height=1,font=('times 15 bold underline'), bd=0,bg="#006400", fg="white")
button2.place(x=255, y=50)

button4 = tk.Button(root, text="Contact us", command=con, width=10, height=1,font=('times', 15, ' bold'),bg="#006400", fg="white")
button4.place(x=180, y=150)


# button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
# button1.place(x=150, y=110)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)


label_l1 = tk.Label(root, text="** Food Classification **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=50, height=2)
label_l1.place(x=0, y=800)


root.mainloop()