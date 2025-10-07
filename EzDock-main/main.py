import board
import digitalio
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard 
from adafruit_hid.keycode import Keycode  

ports = [board.GP15, board.GP14, board.GP13, board.GP12]
funcs = ["copy", "paste", "cut", "vscode"]

interface = Keyboard(usb_hid.devices)


for port in range(len(ports)):
    funcs[port] = digitalio.DigitalInOut(ports[port])
    funcs[port].direction = digitalio.Direction.INPUT
    funcs[port].pull = digitalio.Pull.DOWN

bindings = {0: (Keycode.LEFT_CONTROL, Keycode.C), 1: (Keycode.LEFT_CONTROL, Keycode.V)}

while True:
    for i in range(len(ports)):
        
        if i == 0 and funcs[i].value == True:
            interface.press(bindings[i][0], bindings[i][1])
            print("copy pressed")
            interface.release(bindings[i][0], bindings[i][1])
            time.sleep(0.1)      
            
        if i == 1 and funcs[i].value:
            interface.press(bindings[i][0], bindings[i][1])
            print("paste pressed")
            interface.release(bindings[i][0], bindings[i][1])
            time.sleep(0.1)
    
    
    time.sleep(0.1)
