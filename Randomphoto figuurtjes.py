import glob, os
from PIL import Image
import random
import WaitKey as W

AANTAL_BESCHIKBAAR = 50

WIDTH, HEIGHT = W.getWidthHeightScreen()

dir = "Figuurtjes/"
ext = ".jpg"

selected = random.sample(range(AANTAL_BESCHIKBAAR),AANTAL_BESCHIKBAAR)

for i in selected:
	image = Image.open(dir+str(i)+ext)
	"""
	Resize the image WIDTHxHEIGHT
	"""
	width, height = image.size
	new_image = Image.new('RGB',(WIDTH,HEIGHT),(255,255,255))
	if(1.0*width/WIDTH > 1.0*height/HEIGHT):
		new_height = int(1.0*height/width*WIDTH)
		image = image.resize((WIDTH,new_height))
		new_image.paste(image, box=(0,int((HEIGHT-new_height)/2)))
	elif(1.0*width/WIDTH < 1.0*height/HEIGHT):
		new_width = int(1.0*width/height*HEIGHT)
		image = image.resize((new_width,HEIGHT))
		new_image.paste(image, box=(int((WIDTH-new_width)/2),0))
	else:
		image = image.resize((WIDTH,HEIGHT))
		new_image = image
	new_image.show()
	char = W.getch()
	if(char == 'q'):
		break
