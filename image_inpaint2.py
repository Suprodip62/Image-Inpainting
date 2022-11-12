# import cv2
# import numpy as np
#
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)
#
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
#
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog, Text
# import os
#
# root = tk.Tk()
# root.title("Inpaint Image")
#
# frame = Frame(root)
# image = PhotoImage(file='C:/Users/Asus/PycharmProjects/Image_Inpaint/Banner-of-Inpaint.png')
# button = Button(frame, image=image)
# button.pack()
# frame.pack()
# root.mainloop()


from tkinter import *
root = Tk()
canvas = Canvas(root, width = 800, height = 500)
canvas.pack()
img = PhotoImage(file="Banner-of-Inpaint.png")
canvas.create_image(20,20, anchor=NW, image=img)
mainloop()