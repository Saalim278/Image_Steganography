from tkinter import *
from PIL import Image, ImageTk
import os
from stegano import lsb
from tkinter import filedialog, messagebox

# Create the main application window
win = Tk()
win.geometry("700x480")
win.config(bg="black")

# Function to open an image file
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(), 
                                           title= 'Select Image File',
                                           filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.txt")))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    Lframe1.configure(image=img)
    Lframe1.image = img

def save_img():
    hide_msg.save("saved_data.png")
    messagebox.showinfo("Success", "Image saved successfully as 'saved_data.png'.")

def hide_data():
    global hide_msg
    password = code.get()
    if password == "1234":

        msg = text1.get(1.0, END)
        hide_msg = lsb.hide(open_file, msg)
        messagebox.showinfo("Success", "Data hidden successfully in the image.")
    elif password == "":
        messagebox.showerror("Error", "Please enter a secret key.")
    else:
        messagebox.showerror("Error", "Incorrect secret key. Please try again.")
        code.set("")  # Clear the entry field for the secret key
    

def show_data():
    password = code.get()
    if password == "":
        messagebox.showerror("Error", "Please enter a secret key.")
    elif password != "1234":
        messagebox.showerror("Error", "Incorrect secret key. Please try again.")
        code.set("")  # Clear the entry field for the secret key
    if password == "1234":
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0, END)
        text1.insert(END, show_msg)


# Create a logo image
logo = PhotoImage(file="logo.png")
Label(win, image=logo, bd=0 ).place(x=150, y=0)

# Heading 
Label(win, text="Steganography", font=("Arial", 20, "bold"), fg="white", bg="black").place(x=200, y=0)

# Frame 1
frame1 = Frame(win, width=250, height=250,bd=5, bg="white")
frame1.place(x=40, y=100)
Lframe1 = Label(frame1, bg="white")
Lframe1.place(x=0, y=0)

# Frame 2
frame2 = Frame(win, width=250, height=250,bd=5, bg="white")
frame2.place(x=400, y=100)
text1 = Text(frame2, font='ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=250, height=250)

# Label for Secret key
Label(win, text="Enter Secret Key:", font=("Arial", 15, "bold"), fg="white", bg="black").place(x=40, y=370)

# Entry Widget for Secret Key
code = StringVar()
entry = Entry(win, textvariable=code, bd=2, font=("Arial", 15), show="*").place(x=220, y=370, width=200, height=30)

# Buttons for Encoding and Decoding
# Open Image Button
open_button = Button(win, text="Open Image", font=("Arial", 15, "bold"), fg="white", bg="grey", cursor='hand2', command=open_img).place(x=40, y=420, width=150, height=40)

# Save Image Button
save_button = Button(win, text="Save Image", font=("Arial", 15, "bold"), fg="white", bg="grey", cursor='hand2', command=save_img).place(x=200, y=420, width=150, height=40)

# Hide Image Button
hide_button = Button(win, text="Hide data", font=("Arial", 15, "bold"), fg="white", bg="grey", cursor='hand2', command=hide_data).place(x=360, y=420, width=150, height=40)

# Show Image Button
show_button = Button(win, text="Show data", font=("Arial", 15, "bold"), fg="white", bg="grey", cursor='hand2', command=show_data).place(x=520, y=420, width=150, height=40)



mainloop()