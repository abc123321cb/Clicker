import time

from pynput import keyboard
import pyperclip


c = keyboard.Controller()
speed = 0.005

def type_string(control, string):
    print(string, end='')
    print()
    for s in string:
        control.press(s)
        time.sleep(speed)



def on_press(key):


    if key == keyboard.Key.delete:
        data = pyperclip.paste() + "\n"
        question = data[0:data.find("\n")]
        answers = [1,2,3,4]
        data = data[data.find("\n")+1:]
        for i in range(4):
            answers[i] = data[0:data.find("\n")]
            data = data[data.find("\n") + 1:]
            if answers[i][1] == ")":
                answers[i] = answers[i][3:]


        global c
        type_string(c,question)
        c.press(keyboard.Key.tab)
        time.sleep(speed)
        c.press(keyboard.Key.tab)
        time.sleep(speed)
        c.press(keyboard.Key.tab)
        time.sleep(speed)
        c.press(keyboard.Key.tab)
        time.sleep(speed)
        type_string(c,answers[0])
        for s in answers[1:]:
            type_string(c,s)




def on_release(key):
    if(key == keyboard.Key.esc):
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


