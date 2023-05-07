import pyautogui as pg
import time
time.sleep(1)
url = 'https://www.youtube.com/watch?v=1TPuf-xFmWI&ab_channel=VladMiller'

# Открываем браузер
pg.press("win")
time.sleep(0.2)
pg.write('chrome', 0.1)

pg.press('enter')
time.sleep(1)

pg.write(url, 0.01)
pg.press('enter')
time.sleep(0.4)
pg.press('space')