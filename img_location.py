# Python program to convert from openCV2 to PIL

import cv2
from PIL import Image

# Open image using openCV2
opencv_image = cv2.imread("Resources/download.jpg")

# Notice the COLOR_BGR2RGB which means that the color is
# converted from BGR to RGB
color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

# color_coverted2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
# pil_image2 = Image.fromarray(color_coverted2)
# pil_image2.show()

# Displaying the Scanned Image by using cv2.imshow() method
# cv2.imshow("OpenCV Image", opencv_image)

# Displaying the converted image
pil_image = Image.fromarray(color_coverted)
pil_image.show()

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
