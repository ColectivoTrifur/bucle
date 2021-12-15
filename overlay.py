import time
from PIL import Image, ImageDraw, ImageFont
import mpv

player = mpv.MPV()

player.loop = True
player.play('./drunken_fist.mkv')
player.wait_until_playing()

font = ImageFont.truetype('DejaVuSans.ttf', 40)

while not player.core_idle:
    print("here")
    time.sleep(0.5)
    overlay = player.create_image_overlay()

    for pos in range(0, 500, 5):
        ts = player.time_pos
        if ts is None:
            break

        img = Image.new('RGBA', (400, 150),  (255, 255, 255, 0))
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'Hello World', font=font, fill=(0, 255, 255, 128))
        d.text((10, 60), f't={ts:.3f}', font=font, fill=(255, 0, 255, 255))

        overlay.update(img, pos=(2*pos, pos))
        time.sleep(0.05)

    overlay.remove()
