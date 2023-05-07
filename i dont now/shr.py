import pyautogui as pg
import time
url = 'https://www.youtube.com/watch?v=1TPuf-xFmWI&ab_channel=VladMiller'
pg.press('win')
pg.write('edge')
pg.press('enter')
time.sleep(1)
pg.write(url, 0.01)
pg.press('enter')
time.sleep(0.4)
pg.press('space')

