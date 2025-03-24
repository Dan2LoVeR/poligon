import pyautogui



try:
    location = pyautogui.locateCenterOnScreen('button2.png')
    pyautogui.click(location, clicks=1)
    print('image found')
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')
