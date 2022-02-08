import subprocess
import time
import pyautogui
import pyscreenshot
import win32api
import win32gui
from playsound import playsound
from pynput.keyboard import Listener, Key
from win32api import GetSystemMetrics
from pyzbar.pyzbar import decode

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
hwnd = win32gui.WindowFromPoint((0, 0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))


def draw_rect(firstx, firsty, x, y):
    for _ in range(35):
        for num in range(firsty, y):
            win32gui.SetPixel(dc, firstx - 1, num, red)
            win32gui.SetPixel(dc, firstx - 2, num, red)
            win32gui.SetPixel(dc, x + 1, num, red)
            win32gui.SetPixel(dc, x + 2, num, red)
        for num in range(firstx - 2, x + 2):
            win32gui.SetPixel(dc, num, firsty + 1, red)
            win32gui.SetPixel(dc, num, firsty, red)
            win32gui.SetPixel(dc, num, y, red)
            win32gui.SetPixel(dc, num, y - 1, red)


def on_press(key):
    if key == Key.ctrl_l:
        global start
        interval = time.time() - start
        if interval < 0.2:
            listener.stop()
        start = time.time()


directory = r"sound effects\\"
print("double click CTRL key to start")
playsound(directory + "startup.wav", block=False)
start = time.time()
listener = Listener(on_press=on_press)
listener.start()
listener.join()
playsound(directory + "first_click.wav", block=False)
firstx, firsty = pyautogui.position()
firsty -= 75
firstx -= 75
x = firstx + 150
y = firsty + 150
if x < firstx:
    tempx, tempy = x, y
    x, y = firstx, firsty
    firstx, firsty = tempx, tempy
draw_rect(firstx, firsty, x, y)
im = pyscreenshot.grab()
im = im.crop((firstx + 1920, firsty, x + 1920, y))
try:
    data = str(decode(im))
    link = data[data.find("http"):data.find(",") - 1]
    print(link)
    assert "http" in link, "this is not a link"
    subprocess.check_call(["start", link], shell=True)
except Exception as e:
    print("first fail", e)
    win32gui.InvalidateRect(hwnd, monitor, True)
    try:
        firsty -= 75
        firstx -= 75
        x = firstx + 300
        y = firsty + 300
        if x < firstx:
            tempx, tempy = x, y
            x, y = firstx, firsty
            firstx, firsty = tempx, tempy
        draw_rect(firstx, firsty, x, y)
        im = pyscreenshot.grab()
        im = im.crop((firstx + 1920, firsty, x + 1920, y))
        try:
            data = str(decode(im))
            link = data[data.find("http"):data.find(",") - 1]
            print(link)
            assert "http" in link, "this is not a link"
            subprocess.check_call(["start", link], shell=True)
        except Exception as e:
            win32gui.InvalidateRect(hwnd, monitor, True)
            print("second fail", e)
            firsty += 200
            firstx += 200
            x = firstx - 100
            y = firsty - 100
            if x < firstx:
                tempx, tempy = x, y
                x, y = firstx, firsty
                firstx, firsty = tempx, tempy
            draw_rect(firstx, firsty, x, y)
            im = pyscreenshot.grab()
            im = im.crop((firstx + 1920, firsty, x + 1920, y))
            try:
                data = str(decode(im))
                link = data[data.find("http"):data.find(",") - 1]
                print(link)
                assert "http" in link, "this is not a link"
                subprocess.check_call(["start", link], shell=True)
            except Exception as e:
                print("third fail", e)
                raise Exception
    except:
        playsound(directory + "negativebeep.wav", block=True)

win32gui.InvalidateRect(hwnd, monitor, True)
