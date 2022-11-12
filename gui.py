from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Image")
# root.iconbitmap('c:/gui/codemy.ico')

# myLabel = Label(root, text="Image Inpaint")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select a file", filetypes=(("png files", "*png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command = open).pack()

# myLabel.pack()

root.mainloop()

# from tkinter import *
# root = Tk()
# myLabel = Label(root, text="Hello")
# myLabel.pack()
# root.mainloop()