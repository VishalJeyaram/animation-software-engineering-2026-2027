from PIL import Image, ImageDraw
from random import randint
import math

# Commands to remember
# uv add nccapy 
# uv add flake8
# uv add black
# uv init intro

def main():
    # starter_code()

    # show_downloaded_image()

    # draw_new_image()

    # forLoopPractice()

    # while_loop_practice()

    # Drawing a bunch of boxes and circles
    size = (640, 480)
    bgCol = (110, 0, 200)
    im = Image.new("RGB", size, bgCol)
    draw = ImageDraw.Draw(im)
    # fgCol = (255,255,255)

    for x in range(100, 500, 100):
        for y in range(100, 500, 100):
            fgCol = (randint(0, 256), randint(0, 256), randint(0, 256))
            draw_a_box(draw, fgCol, x, y, 50, 50)
            draw_a_circle_manual_method(draw, fgCol, x + 25, y + 25, 25)
    im.show()
    im.save("result.jpg")


def starter_code():
    print("Hello from intro!")


def show_downloaded_image():
    im = Image.open("Spider-Man.jpg")
    im.show()
    im.save("result.jpg")


def draw_new_image():
    size = (640, 480)
    bgCol = (110, 0, 200)
    im = Image.new("RGB", size, bgCol)

    draw = ImageDraw.Draw(im)
    points = ((100, 100), (200, 100))
    fgCol = (255, 255, 255)
    draw.point(points, fgCol)

    im.show()
    im.save("result.jpg")


def draw_a_box(
    draw, fgCol: tuple[float], x: float, y: float, w: float, h: float
) -> None:
    print("Drawing a Box")
    lines = ((x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y))
    draw.line(lines, fgCol)


def for_loop_practice():
    for i in range(1, 10):
        print(i)


def while_loop_practice():
    i = 0
    while i < 10:
        print(i)
        i += 1


def draw_a_circle_fast_method(draw):
    bounding_box = (100, 100, 300, 300)
    # Draw the circle (an ellipse with equal width and height)
    draw.ellipse(bounding_box, outline="blue", fill="lightblue")


def draw_a_circle_manual_method(draw, col, cx, cy, rad):
    deltaDeg: int = int(360 / rad)
    deltaRad = deltaDeg / 360 * 2 * math.pi
    for thetaDeg in range(0, 360, deltaDeg):
        thetaRad = thetaDeg / 360 * 2 * math.pi
        x = cx + rad * math.cos(thetaRad)
        y = cy + rad * math.sin(thetaRad)
        x1 = cx + rad * math.cos(thetaRad + deltaRad)
        y2 = cy + rad * math.sin(thetaRad + deltaRad)
        draw.line(((x, y), (x1, y2)), col)


if __name__ == "__main__":
    main()
