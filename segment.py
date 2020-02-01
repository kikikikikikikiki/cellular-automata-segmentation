from matplotlib.image import imread
from matplotlib.image import imsave
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from skimage import measure
from PIL import Image, ImageFont, ImageDraw
import math

ex = []
ey = []
ez = []
colorimage = np.zeros((1000,1000,3), dtype="uint8")
nopix = []
noshade = []
rgb = []

rr = []
gg = []
bb = []
def colorrange(shades, macks):
    m = macks
    d = m/6
    r = 0 
    g = 0 
    b = 0
    if shades <= d:
        r = 255
        g = math.sin((shades/(2*d))*math.pi)*255
        b = 0
        
    elif shades >= d and shades < 2*d:
        r = math.sin((shades/(2*d))*math.pi)*255
        g = 255
        b = 0
        
    elif shades >= 2*d and shades < 3*d:
        r = 0
        g = 255
        b = -math.sin((shades/(2*d))*math.pi)*255
        
    elif shades >= 3*d and shades < 4*d:
        r = 0
        g = -math.sin((shades/(2*d))*math.pi)*255
        b = 255
        
    elif shades >= 4*d and shades < 5*d:
        r = math.sin((shades/(2*d))*math.pi)*255
        g = 0
        b = 255
        
    elif shades >= 5*d and shades <= 6*d:
        r = 255
        g = 0
        b = math.sin((0.5*math.pi)+(shades/(2*d))*math.pi)*255
    return((abs(r),abs(g),abs(b)))
    #rr.append(r)
    #gg.append(g)
    #bb.append(b)
"""    
for soe in range(100):
    colorrange(5*(1000000/6)+(1000000/(6*100))*soe)
print(rr)
print(gg)
print(bb)
"""    
    
font = ImageFont.truetype("C:/Users/OOP/Desktop/font/ebrima.ttf",50)
for x in range(600):
    str_num = "000" + str(x+2)
    file_name = str("anti") + str_num[-4:] + ".png"
    #img = imread(file_name)
    img = Image.open(file_name)
    img = np.array(img)
    
    blur1 = ndimage.gaussian_filter(img, sigma=10)
    blur = ndimage.gaussian_filter(img, sigma=15)
    #blur = blur1*blur2
    
    result = Image.fromarray(blur.astype(np.uint8)).convert('RGB')
    im1 = result.save("blur"+file_name) 
    #imsave("blur"+file_name, im)


    blobs = blur > blur.mean()
    all_labels = measure.label(blobs)
    blobs_labels = measure.label(blobs, background=0)
    eh = np.uint8(blobs_labels)

    result = Image.fromarray(eh.astype(np.uint8)).convert('RGB')
    im1 = result.save("segment"+file_name) 
    #plt.imshow(blobs_labels)
    #im = Image.fromarray(eh).convert('RGB')
    
    for x in range(1000):
        for y in range(1000):
            for z in range(1):
                if eh[x][y][z] not in ex:
                    ex.append(eh[x][y][z])
    for shade in range(len(ex)):
        rgb.append(shade%3)
        
    for shade in ex:
        for x in range(1000):
            for y in range(1000):
                for z in range(1):
                    if not eh[x][y][z] == 0:
                        if eh[x][y][z] == shade:
                            nopix.append(shade)
    for shade in ex:
        noshade.append(nopix.count(shade))
       #print(nopix.count(shade))
    #print(noshade)
    nopix.clear()             
    #zp = zip(rgb,ex)
    con = 0
    maksu = 419988
    for x in range(1000):
        for y in range(1000):
            for z in range(1):
                if not eh[x][y][z] == 0:
                    for shade,nosh in zip(ex, noshade):
                        noshturn = colorrange(nosh, maksu)
                        if eh[x][y][z] == shade:
                            #print(colorrange(shade))
                            for va in noshturn:
                                colorimage[x][y][con] = va
                                con+=1
                            con = 0

    
    
    """
    for x in range(1000):
        for y in range(1000):
            for z in range(1):
                if not eh[x][y][z] == 0:
                    for rg,shade in zip(rgb,ex):
                        if eh[x][y][z] == shade:
                            #print(shade)
                            colorimage[x][y][rg] = 255
    """
                    
    #imsave("zzda"+file_name, eh)#,  cmap="Greens", vmin=1, vmax=2)
    #colorimage = colorimage*blur
    wtext = Image.fromarray(colorimage.astype(np.uint8))
    draw = ImageDraw.Draw(wtext)
    #print(ex)
    counter =  0
    numofblobs = len(ex)-1
    print(numofblobs)

    draw.text((0,0), f"{numofblobs} Blobs", (255,255,255), font=font)
    draw = ImageDraw.Draw(wtext)
    noshade.clear()
    ex.clear()
    #imsave("zzdaa"+file_name, colorimage)
    wtext.save("coloured"+file_name)
    colorimage.fill(0)
    

