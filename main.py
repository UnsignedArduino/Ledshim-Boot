import math
import time
import socket

import ledshim

ledshim.set_clear_on_exit()


# https://forum.micropython.org/viewtopic.php?t=7615#p43401
def map_val(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def is_connected():
    try:
        sock = socket.create_connection(("1.1.1.1", 53))
    except OSError:
        return False
    else:
        sock.close()
        return True


scan = []
for intensity in range(round(ledshim.NUM_PIXELS / 2)):
    scan.append(map_val(intensity, 0, ledshim.NUM_PIXELS / 2 - 1, 64, 255))
for intensity in range(round(ledshim.NUM_PIXELS / 2)):
    scan.append(map_val(intensity, 0, ledshim.NUM_PIXELS / 2 - 1, 255, 64))

delta = 0

last_try = time.time()

while True:
    for px in range(ledshim.NUM_PIXELS):
        index = (px + delta) % (ledshim.NUM_PIXELS - 1)
        ledshim.set_pixel(px, scan[index], 0, 0)

    ledshim.show()

    delta += 1
    time.sleep(0.025)

    if time.time() - last_try > 3:
        last_try = time.time()
        print("Testing internet connection...")
        if is_connected():
            print("Connected!")
            break
        else:
            print("Failed to find internet connection!")

ledshim.set_all(0, 255, 0)
ledshim.show()

time.sleep(3)

for intensity in range(255, 0, -16):
    ledshim.set_all(0, intensity, 0)
    ledshim.show()
    time.sleep(0.025)
