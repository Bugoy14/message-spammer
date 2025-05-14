import pyautogui
import keyboard
import time


# counter if you want to count the message
counter = 1

message = "Hello World"

# this 2 seconds will give you time to switch your tab
time.sleep(2)
while True:
    pyautogui.typewrite(f"{message} {counter}")
    time.sleep(1)

    # use hotkey if you don't want to send the message right away
    # pyautogui.hotkey('alt', 'enter')
    #           ^^^^^^

    # or you could just use this "enter" to spam the chat immediately
    pyautogui.press('enter')

    # to increment the number inside the message
    counter += 1

    if keyboard.is_pressed('esc'):
        break
    #   exit(0)
    else:
        continue
