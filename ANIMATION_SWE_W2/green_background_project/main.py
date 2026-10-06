from PIL import Image

def key(img:Image, min:float, max:float) -> Image:
    mask=Image.new("L",img.size)
    for x in range(0,img.width):
        for y in range(0,img.height):
            pixel=img.getpixel((x,y))
            alpha = (pixel[1] - (pixel[0]+pixel[2]) * 0.5) / 255.0 # To calculate how green a pixel is relative to R and B channels
            alpha = (alpha - min) / ( max - min) # Whether a pixel lies in the range of green pixel values
            alpha = 1 - alpha # Flipping a pixel to show how ungreen it is
            if alpha > 1: # If a pixel is super ungreen it becomes white. The more ungreen it is, the higher the value
                alpha = 1
            if alpha < 0: # If a pixel is super green, it becomes black. THe more green, the lower the value. 
                alpha = 0
            mask.putpixel((x,y), int(alpha *255))
    return mask

# To calculate edge values 
def blendRGB(fg,bg,a)->tuple:
    return(
        int(fg[0]*a+bg[0]*(1-a)), 
        int(fg[1]*a+bg[1]*(1-a)),
        int(fg[2]*a+bg[2]*(1-a)),                
    )

def over(fg,bg,mask)->Image:
    result =Image.new("RGB",bg.size)
    for x in range(0,bg.width):
        for y in range(0,bg.height):
            maskVal=mask.getpixel((x,y))/255
            fgpixel=fg.getpixel((x,y))
            bgpixel=bg.getpixel((x,y))
            opppixel=blendRGB(fgpixel,bgpixel,maskVal)
            result.putpixel((x,y),opppixel)
    return result

def main():
    fg = Image.open("green.jpg")
    bg= Image.open("background.jpg")
    mask = key(fg,0.04, 0.1)
    result = over(fg,bg,mask)
    result.show()

if __name__ == "__main__":
    main()
