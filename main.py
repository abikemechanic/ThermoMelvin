import os
import time
import datetime

if not os.name == 'nt':
    from image_2in13_V2_epd import EPDImage as MessageDisplay
else:
    from image_2in13_V2_win import WindowsImage as MessageDisplay

if __name__ == '__main__':
    print("Starting e-paper display")
    img = MessageDisplay()

    # now = datetime.datetime.now()
    # img.add_text(f'{now.hour}:{now.minute}, {now.month}\\{now.day}\\{now.year}')
    # img.show_image()

    img.mqtt.mqtt_client.loop_forever()
