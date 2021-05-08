
from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image
import requests
import re
import glob
import os, os.path
import tkinter as tk
import sys

root= tk.Tk()
root.title("Automationing")

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#url label
label1 = tk.Label(root, text='Enter URL Here')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label1)

#crop
label2 = tk.Label(root, text='Enter Crop factor (optional, 50 defaut value)')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 115, window=label2)

#Crop box
entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

#url box
entry2 = tk.Entry (root)
canvas1.create_window(200, 75, window=entry2, width=350)

#The output text
output_text = StringVar()
printerer = tk.Label(root, textvariable = output_text)
printerer.config(font=('helvetica', 10))
canvas1.create_window(200, 270, window=printerer)


def image_process():
    #Loading Data
    URL = entry2.get()
    pixel_cut = entry1.get()
    if pixel_cut == '':
        pixel_cut = '50'

    #Clearing Old Files
    print('Clearing Old Files...')
    output_text.set('Clearing Old Files...')
    root.update()

    files = glob.glob('Photos/*')
    for f in files:
        os.remove(f)

    #url stuffs
    content = requests.get(URL)

    #BeautifulSoup start
    print('Initializing Beautiful Soup...')
    output_text.set('Initializing Beautiful Soup...')
    root.update()

    soup = BeautifulSoup(content.text, 'lxml') #content.text
    body = soup.find("div", {"class" : "fotorama"})
    img = body.find_all('img')

    #Some variable for counting repeats and image naming
    counter = 0
    url_list = []

    #Image scrape loop and saving
    print('Scraping Images...')
    output_text.set('Scraping Images...')
    root.update()

    for src in img:
        url = 'https:' + (src['src']) #the line that I spent hours searching for

        photo = Image.open(requests.get(url, stream = True).raw)
        photo.save('Photos/photo-0' + str(counter) + '.jpeg')
        counter += 1
        #url_list.append(url)

    print('Images Downloaded Successfully')
    output_text.set('Images Downloaded Successfully')
    root.update()

    #Start of Cropping

    #Clearing Old Files
    print('Clearing Old Files')
    output_text.set('Clearing Old Files...')
    root.update()

    files = glob.glob('Cropped/*')
    for f in files:
        os.remove(f)


    counter = 0;


    print('Cropping images...')
    output_text.set('Cropping images...')
    root.update()

    #The Image Cropper
    #This needs two folders, Cropped and Photos on the same directory as the executable
    while counter >= 0:
        current_image = 'photo-0' + str(counter) + '.jpeg'
        current_path = 'Photos/' + current_image
        if os.path.exists(current_path):
        	#To get the image width and height
            im = Image.open(current_path)
            width, height = im.size
            watermark_ratio = ((int(pixel_cut))/(height)) #px/image_height


        	#Crop image according to fixed ratio
            top_crop = height*watermark_ratio
        	#box = (0,0,x,y)
            cropped = im.crop((0, top_crop, width, height))

        	#Saving the file
            cropped = cropped.save('Cropped/' + 'crp_' + current_image)
            counter += 1
        else:
           break

    print('Task Complete.')
    output_text.set('Task Complete.')
    root.update()

#button fuctions
button1 = tk.Button(text='Go!', command=lambda:[image_process()], bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


root.mainloop()
