import os
import numpy as np
from PIL import Image
from PIL import ImageColor
import random

"""
Constants
"""
SIZE = 128      # afmetingen van de afbeeldingen op het bladje
BINGO_SIZE = 6      # afmetingen van de bingo map (het bladje)
AANTAL_BESCHIKBAAR = 50 # het aantal afbeeldingen in het mapje met figuurtjes
AANTAL_BLADEN = 10  # het aantal bladjes om uit te delen
DIR_RESULTS = "Bingo blaadjes met figuurtjes/"

"""
Open all the images and store them in a python list
"""
dir = "Figuurtjes/"
ext = ".jpg"

for nieuw_blad in range(AANTAL_BLADEN):
    images = []
    selected = random.sample(range(AANTAL_BESCHIKBAAR),BINGO_SIZE**2)
    for i in selected:
        images.append(Image.open(dir+str(i)+ext))

    """
    Resize the images to squares of size SIZExSIZE
    """
    for i in range(BINGO_SIZE**2):
        width, height = images[i].size
        if(width > height):
            new_image = Image.new('RGB',(width,width),(255,255,255))
            new_image.paste(images[i], box=(0,int((width-height)/2)))
        elif(width < height):
            new_image = Image.new('RGB',(height,height),(255,255,255))
            new_image.paste(images[i], box=(int((height-width)/2),0))
        else:
            new_image = images[i]
        images[i] = new_image
        images[i] = images[i].resize((SIZE,SIZE))
        #images[i].show(str(i))

    """
    Math stuff to make a black line around the images & make a random image with the 25 images randomly placed in the boxes.
    """
    # full border around the images
    output_image = Image.new('RGB', (BINGO_SIZE*SIZE+BINGO_SIZE+1,BINGO_SIZE*SIZE+BINGO_SIZE+1))


    print(selected)
    for i in range(BINGO_SIZE):
        for j in range(BINGO_SIZE):
            output_image.paste(images[i*BINGO_SIZE+j], box=(i*(SIZE+1)+1,j*(SIZE+1)+1))
            
    #output_image.show()
    output_image.save(DIR_RESULTS+"BINGO"+str(nieuw_blad)+".jpg")

