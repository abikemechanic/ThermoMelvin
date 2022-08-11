import os.path
from PIL import Image, ImageDraw, ImageFont

if not os.name == 'nt':
    # import epd_image_2in13_V2 as image_drawer
    pass
else:
    from win_image_2in13_V2 import WindowsImage as ImageDraw


if __name__ == '__main__':
    print("Starting e-paper display")
    img = ImageDraw()

    img.add_text('yellow')
    img.show_image()


