#! /usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import urllib.request
import os
import io
#import pyautogui



#urllib.request.urlretrieve('http:/upload.wikimedia.org/wikipedia/commons/3/30/ROS_Crystal_Logo.jpg','ros_logo.jpg')
Image.open('ROS_Crystal_Logo.png')
img = Image.open('ROS_Crystal_Logo.png').convert('L').resize((90,90))
img.save('ROS_Crystal_class.png')

np_image = np.array(img)
asciis = ['"','¤','%','!','&']



class Image_to_ascii:
    """
    Takes in numpy array, print image to ascii chars
    optional parameter:
    asciis = list of chars to use
    """

    def __init__(self, np_image, asciis=None):
        if asciis is None:
            asciis = ['"','¤','%','!','&']
        self.asciis = asciis
        self.np_image = np_image



    def image_to_ascii(self):
       
        for index_x in range(self.np_image.shape[0]):
            print("")
            for index_y in range(self.np_image.shape[1]):
                multiplier = 255//len(self.asciis)
                for current_ascii in range(len(self.asciis)):
                    if self.np_image[index_x, index_y] >= (255 - (current_ascii+1)*multiplier):
                        self.fake_file = io.StringIO()
                        print(self.asciis[current_ascii], end=" ", file=self.fake_file)
                        self.new_file=self.fake_file.getvalue()
                        break
                self.ascii_to_text_file()
                        
        
                        

# https://realpython.com/python-print/ <-- Here I found a link about how to catch a "print".
# So I imported the io library and made the print in to a variable.
# Then I called the ascii_to_text_file function using the self so that the print catching
# variable can be used in there. Then I used "a" to append to the file, because "w"
# overwrited the file everytime when I writed a new letter.
        
                        
    def ascii_to_text_file(self):
        self.ascii_text_file = "ascii.txt"

        try:
            open(self.ascii_text_file,"a").write(self.new_file)
            self.text_to_image()
        except:
            print("file saving failed!")
        
    
    def text_to_image(self):
        image = Image.new("RGB", (400, 400), "blue")
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((10, 10), self.new_file, font=font)   
        image.save('text_image.jpg')

# I got the image saved, but not the way I wanted to.
# I searched high and low, but didn't find any good sources.
# I have never done any real picture manipulations before this course,
# And I don't have a clue how pixels work so it is not an easy task.


    #image_to_ascii(np_image)
    #image_to_ascii(np_image, ['r','5','r'])
    #image_to_ascii(np_image, "Yeeees!!!")
    


Image_to_ascii(np_image).image_to_ascii()

