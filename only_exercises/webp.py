from PIL import Image
import os

current_path = os.getcwd()
chdir = "/home/alice/Desktop/LaMer/"

conv_list = os.listdir(chdir+'slides/')

for image in conv_list:
    if image.endswith(".jpeg") or image.endswith(".png") or image.endswith(".jpg"):
        im = Image.open(chdir+'slides/'+image)
        im.save(chdir+f"converted/{image[:-5]}.webp", "webp")