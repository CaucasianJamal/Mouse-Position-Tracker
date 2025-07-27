import pyautogui, sys
from pynput.mouse import Listener, Button
import threading
import time

time.sleep(1)
print('right click to quit.')
stop_threads = False

def on_click(x, y, button, pressed):
    global stop_threads
    if button == Button.left:
        if pressed:
            print('Mouse clicked at ({0}, {1})'.format(x, y))
    if button == Button.right:
        if pressed:
            stop_threads = True
        return False

def clickMouse():
    with Listener(on_click=on_click) as listener:
        listener.join()

def mouseCurrentLocation():
    global stop_threads
    while(not stop_threads):
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

if __name__ =="__main__":
    t1 = threading.Thread(target=clickMouse)
    t2 = threading.Thread(target=mouseCurrentLocation)
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("\nDone!")