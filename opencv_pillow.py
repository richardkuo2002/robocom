from PIL import Image                                         
import time
start = time.time()
im = Image.open("/Users/richard/Downloads/IMG_5406.JPG")
address = []
for i in range(0,885):
    for j in range(0,498):
        tuple = im.getpixel((i,j))
        if tuple[0]>250 and tuple[1]>250:
            address.append((i,j))
end = time.time()
#print address
print(len(address))
print(end-start)

import time
import cv2
im = cv2.imread("/Users/richard/Downloads/IMG_5406.JPG")
start = time.time()
address = []
for i in range(0,885):
    for j in range(0,498):
        pix = im[i,j]
        if list(pix)[2]>250 and list(pix)[1]>250:
            address.append((i,j))
end = time.time()
#print address
print(len(address))
print(end-start) 