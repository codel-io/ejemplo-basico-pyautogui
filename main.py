import pyautogui

pyautogui.moveTo(200, 270, 1)
pyautogui.moveTo(500, 270, 1)
pyautogui.moveTo(500, 570, 1)
pyautogui.moveTo(200, 570, 1)
pyautogui.moveTo(200, 270, 1)


pyautogui.moveTo(200, 270, 1)
pyautogui.drag(300, 0, 1, button='left')


pyautogui.moveTo(200, 270, 1, pyautogui.easeInQuad)
pyautogui.move(50, 60, 1, pyautogui.easeOutQuad)
pyautogui.dragTo(500,270, 1, pyautogui.easeInOutQuad, button='left',)
pyautogui.drag(300, 0, 1, pyautogui.easeInBounce, button='left')