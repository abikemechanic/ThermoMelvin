import os
import time

if not os.name == 'nt':
    from image_2in13_V2_epd import EPDImage as MessageDisplay
else:
    from image_2in13_V2_win import WindowsImage as MessageDisplay


if __name__ == '__main__':
    print("Starting e-paper display")
    img = MessageDisplay()

    img.add_text('yellow')
    img.show_image()
    time.sleep(5)
    img.clear()


