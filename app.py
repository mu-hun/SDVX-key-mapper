import keyboard
import mouse

lock = {'x': 200, 'y': 200}

left_knob = {'left': 'q', 'right': 'w'}
right_knob = {'left': 'o', 'right': 'p'}


def register_mouse_hook():
    while True:
        mouse.move(lock['x'], lock['y'], duration=0.01)

        if keyboard.is_pressed('shift'):
            break
        else:
            x, y = mouse.get_position()
            if x == lock['x']:
                keyboard.release(left_knob['left'])
                keyboard.release(left_knob['right'])
            elif x < lock['x']:
                keyboard.press(left_knob['left'])

            elif x > lock['x']:
                keyboard.press(left_knob['right'])

            if y == lock['y']:
                keyboard.release(right_knob['left'])
                keyboard.release(right_knob['right'])
            if y < lock['y']:
                keyboard.press(right_knob['left'])

            elif y > lock['y']:
                keyboard.press(right_knob['right'])


keyboard.add_hotkey('p+i', register_mouse_hook)
keyboard.wait()
