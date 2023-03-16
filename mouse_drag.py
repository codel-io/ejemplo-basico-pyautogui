import pyautogui

# dibujando las esquinas del cuadrado
pyautogui.moveTo(200, 270, 1)
pyautogui.click()
pyautogui.moveTo(500, 270, 1)
pyautogui.click()
pyautogui.moveTo(500, 570, 1)
pyautogui.click()
pyautogui.moveTo(200, 570, 1)
pyautogui.click()
pyautogui.moveTo(200, 270, 1)


# dibujando el cuadrado
pyautogui.dragTo(500,270, 1, button='left')
pyautogui.dragTo(500,570, 1, button='left')
pyautogui.drag(-300, 0, 1, button='left')

# dibujando la última línea utilizando otras funciones
pyautogui.mouseDown()
pyautogui.mouseUp(x=200, y=270, duration=1)