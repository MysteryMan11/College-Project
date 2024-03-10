import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Food Classification")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="Food Classification",font=("Times New Roman", 30, 'bold'),
                    background="brown", fg="white", width=65, height=2)
label_l1.place(x=0, y=0)

img = Image.open('g1.jpg')
img = img.resize((100,70), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=20, y=10)







label1 = tk.Label(root, text="GOOD FOOD,", font=('times', 45, 'bold'), bg="black", fg="white")
label1.place(x=120, y=150+30)

label2 = tk.Label(root, text="GOOD MOOD!", font=('times', 45, 'bold'), bg="#bfe8ec", fg="#131e3a")
label2.place(x=120, y=250+30)

label2 = tk.Label(root, text="“ There is no sincere love \n than the love of food.", font=('times', 25), bg="brown", fg="#2e777b")
label2.place(x=120, y=350+30)



# using recursion to slide to next image
x = 1

# function to change to next image
# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img,width=1800,height=700)
# 	elif x == 2:
# 		logo_label.config(image=img2,width=1800,height=700)
# 	elif x == 3:
# 		logo_label.config(image=img3,width=1800,height=700)
# 	x = x+1
# 	root.after(2000, move)

# # calling the function
# move()

# frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)


#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def con():
#     from subprocess import call
#     call(["python","contact_us.py"])
#     root.destroy()

# def about():
#     from subprocess import call
#     call(["python","about_us.py"])
    
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()
    
def log():
    from subprocess import call
    call(["python","Login.py"])
    root.destroy()
    
def window():
  root.destroy()
  
  
# button1 = tk.Button(label_l1, text="About us", command=about, width=7, height=1,font=('times 15 bold underline'),bd=0, bg="#FFA500", fg="white")
# button1.place(x=145, y=50)

# button2 = tk.Button(label_l1, text="Contact us",command=con,width=7, height=1,font=('times 15 bold underline'), bd=0, bg="#FFA500", fg="white")
# button2.place(x=245, y=50)

button4 = tk.Button(root, text="Login", command=log, width=12, height=2,font=('times', 15, 'bold '), bg="brown", fg="white", bd=4)
button4.place(x=800, y=300)

button4 = tk.Button(root, text="Registration", command=reg, width=12, height=2,font=('times',15, "bold" ), bg="brown", fg="white", bd=4)
button4.place(x=800, y=200)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=2,font=('times', 15, 'bold' ), bg="brown", fg="white", bd=4)
button3.place(x=800, y=400)

#####################################################################################################################

# button1 = tk.Button(frame_alpr, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="Black", fg="white")
# button1.place(x=150, y=110)

# button2 = tk.Button(frame_alpr, text="Register",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="black", fg="white")
# button2.place(x=150, y=200)

# button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
# button3.place(x=150, y=300)


label_l1 = tk.Label(root, text="** Food Classification @ 2023 **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=2)
label_l1.place(x=0, y=800)


root.mainloop()