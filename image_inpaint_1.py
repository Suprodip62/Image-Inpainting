import numpy as np
import cv2 as cv
import sys

# from tkinter import *
#
# root = Tk()
# root.title("Cursors")
# root.geometry("500x550")
# # root.iconbitmap('c:/guis/exe/codemy.ico')
# root.config(cursor="circle")
#
# my_button = Button(root, text="Button", cursor="fleur")
# my_button.pack(pady=20)
#
# root.mainloop()



# list = ["arrow","circle","clock","cross","dotbox","exchange","fleur","heart","man","mouse","pirate","plus","shuttle","sizing","spider","spraycan","star","target","tcross","trek",]

# Ed
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os

from PIL import Image
import PIL

root = tk.Tk()
root.title("Inpaint Image")
apps = []
line_size = 5

def addApp():
    for widget in frame.winfo_children():
        widget.distroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("jpg files", "*jpg"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def inpaint():
    for app in apps:
        f = open("save.txt", "w")
        f.write(app)


        # Read image in color mode

        f = open("save.txt", "r")
        # path = f.read()


        path = app

        path2 = 'C:/Users/Asus/PycharmProjects/Image_Inpaint'

        # path = 'Resources/download.jpg'

        img = cv.imread(path, cv.IMREAD_COLOR)
        img2 = img

        if img is None:
            print("Fail to load image file : {}".format(img))
            return
        img_mask = img.copy()

        inpaintMask = np.zeros(img.shape[0:2], np.uint8)

        sketch = Sketcher('image', [img_mask, inpaintMask], lambda: ((255, 255, 255), 255))

        while True:
            ch = cv.waitKey(0)

            if ch == 27:
                cv.destroyAllWindows()
                break
            if ch == ord('t'):
                res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_TELEA)
                # cv.imshow("Inpaint output using FMM", res)

                # out = open('output.txt', 'w')
                # out.write(res)

                # cv.imwrite(res, img2)
                # print("Image is saved color")
                # cv.imwrite(os.path2.join(path2, res), img)
                # cv.waitKey(0)

                # im1 = Image.open(r"Resources/download.jpg")
                # im1 = im1.save(res)

                color_coverted2 = cv.cvtColor(res, cv.COLOR_BGR2RGB)
                pil_image2 = Image.fromarray(color_coverted2)
                pil_image2.save("C:/Users/Asus/PycharmProjects/Image_Inpaint/result.jpg")
                pil_image2.show()

                # im1 = Image.open(r"Resources/download.jpg")
                # im1 = im1.save(pil_image2)


            if ch == ord('n'):
                res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_NS)
                cv.imshow("Inpaint output using NS", res)

            if ch == ord('r'):
                img_mask[:] = img
                inpaintMask[:] = 0
                sketch.show()
            print("Completed")


# canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
# canvas.pack()
canvas = Canvas(root, width = 800, height = 500)
canvas.pack()

img = PhotoImage(file="Banner-of-Inpaint.png")
canvas.create_image(20,20, anchor=NW, image=img)


frame = tk.Frame(root, bg="white")
frame.place(relwidth="0.4", relheight="0.1", relx=0.3, rely=0.65)
# frame.place(relwidth="0.8", relheight="0.8", relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open Image", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Show Image", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

execute = tk.Button(root, text="Inpaint", padx=10, pady=5, fg="white", bg="#263D42", command=inpaint)
execute.pack()

# root.mainloop()

# with open('save.txt', 'w') as f:
#     for app in apps:
#         f.write(app)
# Ed





class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv.imshow(self.windowname, self.dests[0])
        # cv.imshow(self.windowname + ": Mask", self.dests[1])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)

        if event == cv.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv.EVENT_LBUTTONUP:
            self.prev_pt = None
        if self.prev_pt and flags & cv.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv.line(dst, self.prev_pt, pt, color, line_size)
            self.dirty = True
            self.prev_pt = pt
            self.show()


# def main():
#     print("Usage : Python Inpaint ")
#     print("Keys : ")
#     print("t- inpaint using FMM")
#     print("n- inpaint using NS Technique")
#     print("r- reset the inpaint mask")
#     print("ESC - exit")
    #
    # # Read image in color mode
    #
    # # path = 'save.txt'
    # f = open("save.txt", "r")
    # path = f.read()
    #
    # # path = 'Resources/download.jpg'
    #
    # img = cv.imread(path, cv.IMREAD_COLOR)
    #
    # if img is None:
    #     print("Fail to load image file : {}".format(img))
    #     return
    # img_mask = img.copy()
    #
    # inpaintMask = np.zeros(img.shape[0:2], np.uint8)
    #
    # sketch = Sketcher('image', [img_mask, inpaintMask], lambda: ((255, 255, 255), 255))





    # while True:
    #     ch = cv.waitKey(0)
    #
    #     if ch == 27:
    #         break
    #     if ch == ord('t'):
    #         res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_TELEA)
    #         cv.imshow("Inpaint output using FMM", res)
    #         # with open('output.txt', 'w') as f:
    #             # for app in apps:
    #             #     f.write(res)
    #
    #     if ch == ord('n'):
    #         res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_NS)
    #         cv.imshow("Inpaint output using NS", res)
    #
    #     if ch == ord('r'):
    #         img_mask[:] = img
    #         inpaintMask[:] = 0
    #         sketch.show()
    #     print("Completed")


# if __name__ == '__main__':
#     main()
#     cv.destroyAllWindows()


root.mainloop()

# print("Package imported")