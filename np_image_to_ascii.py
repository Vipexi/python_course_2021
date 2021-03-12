#! /usr/bin/python3

from PIL import Image
import numpy as np
import urllib.request

#urllib.request.urlretrieve('http:/upload.wikimedia.org/wikipedia/commons/3/30/ROS_Crystal_Logo.jpg','ros_logo.jpg')
Image.open('ROS_Crystal_Logo.png')
img = Image.open('ROS_Crystal_Logo.png').convert('L').resize((80,80))
img.save('ROS_Crystal_Logo.png')

np_image = np.array(img)
asciis = ['','*','#','o','0']

for index_x in range(80):
    print("")
    for index_y in range(80):
        if np_image[index_x,index_y] > 200:
            print(asciis[0], end='')
        elif np_image[index_x,index_y] > 160:
            print(asciis[1], end='')
        elif np_image[index_x,index_y] > 120:
            print(asciis[2], end='')
        elif np_image[index_x,index_y] > 60:
            print(asciis[3], end='')
        else:
            print(asciis[4], end='')
