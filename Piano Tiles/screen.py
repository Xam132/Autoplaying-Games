import pyautogui
from PIL import ImageGrab
import numpy as np
import matplotlib.pyplot as plt
import time
import mss

# link : https://magictiles3.co/

pyautogui.FAILSAFE = True
# Minimize it for now
pyautogui.click(890, 19)

img = np.array(ImageGrab.grab())
plt.imshow(img)
plt.show()

# The game window location
x1, x2 = 1300, 1600
y1, y2 = 550, 551
loc = [0, 100, x2 - x1 - 100, x2 - x1]

# sct is BGR not RGB
sct = mss.mss()
monitor = {"top": y1, "left": x1, "width": x2 - x1 + 1, "height": y2 - y1}
print("here")

img = np.array(sct.grab(monitor))
# plt.imshow(img)
# plt.show()

# Find start / replay location
for x in loc:
	pixel = img[0, x, :3]
	print(pixel)
	if tuple(pixel) == (198, 159, 54):
		pyautogui.click(x1 + x, y1)
		break

# Click black tiles
for _ in range(10000):
	img = np.array(sct.grab(monitor))
	for x in loc:
		pixel = img[0, x, :3]
		print(pixel)
		if np.all(pixel < 25):  # Dark pixel
			pyautogui.click(x1 + x, y1)
			break
