import pyautogui
from time import sleep
from random import randint

screen_size = pyautogui.size()
click_x, click_y = (screen_size[0] / 2, screen_size[1] * 0.6)
timer = 0

print("Charging up auto clicker!!! (this may take about 3-5 seconds)")
sleep(randint(3, 5))

print("Autoclicker activated!!! Now watch the destruction...")

pyautogui.moveTo(click_x, click_y)
while timer < 100:
	pyautogui.click()
