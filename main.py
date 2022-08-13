import os

if not os.name == 'nt':
    from epd_image_2in13_V2 import EPDImage as MessageDisplay
else:
    from win_image_2in13_V2 import WindowsImage as MessageDisplay


if __name__ == '__main__':
    print("Starting e-paper display")
    img = MessageDisplay()

    img.add_text('yellow')
    img.show_image()


