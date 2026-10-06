# Import statement for PIL
from PIL import Image


# key function
# Usage: To convert coloured foreground image to black and white, white for the face and body, and black for the background
def key(img: Image, min: float, max: float) -> Image:
    mask = Image.new("L", img.size)  # Defining mask image of the same size as the image itself
    for x in range(0, img.width):  # For loop to iterate through every pixel in the x direction (width of the image)
        for y in range(0, img.height):  # For loop to iterate through every pixel in the y direction (height of the image)
            pixel = img.getpixel((x, y))  # Command to obtain the colour of the current pixel using its x and y coordinates in the current iteration of the nested For loop
            alpha = (pixel[1] - (pixel[0] + pixel[2]) * 0.5) / 255.0  # To calculate how green a pixel is relative to R and B channels
            alpha = (alpha - min) / (max - min)  # Alpha value determines whether a pixel lies in the range of green pixel values
            alpha = (1 - alpha)  # This flips the alpha value to now indicate how ungreen a pixel is. If it is super ungreen, it will be higher. If it is super green, it will be lower.
            if (alpha > 1):  # If a pixel is super ungreen, its alpha value increases, and it becomes white. The more ungreen it is, the higher the value of alpha
                alpha = 1  # If alpha is more than 1, it is set to 1
            if (alpha < 0):  # If a pixel is super green, its alpha value decreases, and it becomes black. The more green it is, the lower the value of alpha
                alpha = 0  # If alpha is less than 0, it is set to 0
            mask.putpixel((x, y), int(alpha * 255))  # if alpha is 1, 1 X 255 = 255 (white for the foreground), if alpha is 0, 0 X 255 = 0 (black for foreground). If alpha isn't 1 or 0, it will be for the edges and will have a random value between 0 and 1 and will multiply by 255 to scale it by that factor (used in the blendRGB function)
    return mask


# blendRGB function
# To calculate edge colour values. If the pixel is black, a will be 0 and the bg colour will be applied. If the pixel is white, a will be 1 and the fg colour will be applied. If it is neither, the resultant colour will be a mix of the fg and bg to smoothen the edges.
def blendRGB(fg, bg, a) -> tuple:
    return (
        int(fg[0] * a + bg[0] * (1 - a)),  # Red channel
        int(fg[1] * a + bg[1] * (1 - a)),  # Green channel
        int(fg[2] * a + bg[2] * (1 - a)),  # Blue channel
    )


# over function
# Usage: To paint the background pixels and foreground pixels over the black and white pixels respectively
def over(fg, bg, mask) -> Image:
    result = Image.new("RGB", bg.size)  # Defining a blank result image which is the final image that will be painted over
    for x in range(0, bg.width):  # For loop to iterate through every pixel in the x direction (width of the image)
        for y in range(0, bg.height):  # For loop to iterate through every pixel in the y direction (height of the image)
            maskVal = (mask.getpixel((x, y)) / 255)  # Getting every mask pixel's colour and dividing it by 255. If it is white, it will be 255/255 = 1. If it is black, it will be 0/255 = 0. If it is between, it will be on the edges between the fg and bg and will have an arbitrary value.
            fgpixel = fg.getpixel((x, y))  # Getting every foreground colour pixel
            bgpixel = bg.getpixel((x, y))  # Getting every background colour pixel
            opppixel = blendRGB(fgpixel, bgpixel, maskVal)  # Calling the blendRGB function
            result.putpixel((x, y), opppixel)  # Inserting the final pixel colours into the result image to complete it.
    return result


def main():
    fg = Image.open("green.jpg")  # variable to store foreground image pixels
    bg = Image.open("background.jpg")  # variable to store background image pixels
    mask = key(fg, 0.04, 0.1)  # mask variable to store black and white mask pixels
    result = over(fg, bg, mask)  # result variable to store final image
    result.show()  # display the final image


if __name__ == "__main__":
    main()  # Entry point of the application
