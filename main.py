import os.path
import sys
from PIL import Image, ImageDraw, ImageFont

if not os.name == 'nt':
    from waveshare_epd import epd2in13_V2


print("Hello, World")
