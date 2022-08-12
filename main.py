import os

if not os.name == 'nt':
    # import epd_image_2in13_V2 as MessageDisplay
    pass
else:
    from win_image_2in13_V2 import WindowsImage as MessageDisplay


if __name__ == '__main__':
    print("Starting e-paper display")
    img = MessageDisplay()

    img.add_text('yellow')
    img.show_image()


