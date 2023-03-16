import pyautogui

# moviendo el mouse y haciendo click con funciones independientes
pyautogui.moveTo(127, 485, 1) 
pyautogui.click() # click en el 2

pyautogui.moveTo(54, 493, 1)
pyautogui.click() # click en el 1

# moviendo mouse tomando como punto de partida la posición actual
pyautogui.move(62, 42, 1)
pyautogui.click() # click en el .

pyautogui.move(74, -143, 1)
pyautogui.click() # click en el 0

# moviendo el mouse y haciendo click con una sola función
pyautogui.click(x=190, y=392) # click en el 9
pyautogui.click(x=54, y=493) # click en el 1
pyautogui.click(x=127, y=485) # click en el 2
pyautogui.click(x=253, y=392) # click en el /
pyautogui.click(x=48, y=392) # click en el 7
pyautogui.click(x=317, y=510) # click en el =