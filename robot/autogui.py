import pyautogui

pyautogui.click(10, 5)
pyautogui.FAILSAFE = False

# 在(200,250)位置点击右键
pyautogui.click(200, 250, button='right')


