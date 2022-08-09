from typing import Union
import keyboard
import mouse

lock = {'x': 200, 'y': 200}

left_knob = {'left': 'q', 'right': 'w'}
right_knob = {'left': 'o', 'right': 'p'}


def handle_mouse_hook(event: Union[mouse.ButtonEvent, mouse.WheelEvent, mouse.MoveEvent]):
    if 'x' in event and 'y' in event:
        if event.x < lock['x']:
            keyboard.send(left_knob['left'])
        elif event.x > lock['x']:
            keyboard.send(left_knob['right'])

        if event.y < lock['y']:
            keyboard.send(right_knob['left'])
        elif event.y > lock['y']:
            keyboard.send(right_knob['right'])


def register_mouse_hook():
    mouse.hook(handle_mouse_hook)

    while True:
        if keyboard.is_pressed('shift') and keyboard.is_pressed('p') and keyboard.is_pressed('i') and keyboard.is_pressed('e'):
            mouse.unhook_all()
            break
        else:
            mouse.move(lock['x'], lock['y'])


keyboard.add_hotkey('shift+p+i', register_mouse_hook)
keyboard.wait()
