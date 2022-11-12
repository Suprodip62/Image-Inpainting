import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Inpaint Image")
# root.configure(background='Banner-of-Inpaint.png')
# Banner-of-Inpaint.png

apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.distroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("jpg files", "*jpg"), ("executables", ".exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

# canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
# canvas.pack()

# from tkinter import *
# root = Tk()
canvas = Canvas(root, width = 800, height = 500)
canvas.pack()
img = PhotoImage(file="Banner-of-Inpaint.png")
canvas.create_image(20,20, anchor=NW, image=img)
# mainloop()



# frame = Frame(root)
# frame.grid(row=0)
# photo = PhotoImage(file="Banner-of-Inpaint.png")
# label = Label(frame, image=photo)
# label.image = photo
# label.place(x=0, y=0)


# background = PhotoImage(file = "Banner-of-Inpaint.png")
# background = PhotoImage('file://C:/Users/Asus/PycharmProjects/Image_Inpaint/Banner-of-Inpaint.png')

# frame = tk.Frame(root, bg=background)
frame = tk.Frame(root, bg="white")
frame.place(relwidth="0.4", relheight="0.1", relx=0.3, rely=0.7)

# frame = Frame(root)
# image = PhotoImage(file='C:/Users/Asus/PycharmProjects/Image_Inpaint/Banner-of-Inpaint.png')
# button = Button(frame, image=image)
# button.pack()
# frame.pack()

openFile = tk.Button(root, text="Open Image", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Show Image", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app)