import vgamepad as vg
import socketio
import time

gamepad = vg.VX360Gamepad()

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")
@sio.event
def disconnect():
    gamepad.reset()

strToBtn = {
  'A': vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
  'B': vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
  'X': vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
  'Y': vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
}

@sio.on('btn-control')
def btnControl(data):
    print(data['value'] + ' ' + data['event'])
    if data['event']=='down':
        gamepad.press_button(button=strToBtn[data['value']])
        gamepad.update()
    elif data['event']=='up':
        gamepad.release_button(button=strToBtn[data['value']])
        gamepad.update()
    

sio.connect("http://virgo.wolfdigit.csie.org:3000")
_stop = False
while not _stop:
    time.sleep(0.1)