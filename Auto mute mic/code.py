import snir
import os
import time
import keyboard
import win32gui
from selenium import webdriver
import pyautogui

os.system("taskkill /F /IM chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
})
driver = webdriver.Chrome(options=options)
driver.get("index.html")
WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
hwnd_active = win32gui.GetForegroundWindow()
time.sleep(3)
while 1:
    time.sleep(0.1)
    label = driver.find_element_by_id("myHeader").text
    print(label)
    if label == "chair":
        pyautogui.press("numlock")
        snir.click_sound1()
        print(snir.bright_red("waiting for numlock press"))
        keyboard.wait("numlock")
