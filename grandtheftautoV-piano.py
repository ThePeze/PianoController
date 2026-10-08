import mido
import keyboard
import pydirectinput

pydirectinput.FAILSAFE = False

with mido.open_input() as inport:
    for message in inport:
        print(message.note)
        if(str(message).startswith("note_on")):
            match message.note:
                case 59:
                    keyboard.press("shift")
                    print("Sprint")
                case 62:
                    keyboard.press("a")
                    print("Left")
                case 63:
                    keyboard.press("w")
                    print("Forward")
                case 64:
                    keyboard.press("s")
                    print("Back")
                case 65:
                    keyboard.press("d")
                    print("Right")
                case 67:
                    keyboard.press("f")
                    print("Enter Car")
                case 77:
                    pydirectinput.mouseDown()
                    print("Shooting")
                case 79:
                    pydirectinput.mouseDown(button='right')
                    print("Aiming")
                case 83:
                    pydirectinput.moveRel(-100, 0, relative='true')
                    print("Look Left")
                case 84:
                    pydirectinput.moveRel(0, 100, relative='true')
                    print("Look Down")
                case 85:
                    pydirectinput.moveRel(0, -100, relative='true')
                    print("Look Up")
                case 86:
                    pydirectinput.moveRel(100, 0, relative='true')
                    print("Look Right")
        elif(str(message).startswith("note_off")):
            match message.note:
                case 59:
                    keyboard.release("shift")
                case 62:
                    keyboard.release("a")
                case 63:
                    keyboard.release("w")
                case 64:
                    keyboard.release("s")
                case 65:
                    keyboard.release("d")
                case 67:
                    keyboard.release("f")
                case 77:
                    pydirectinput.mouseUp()
                case 79:
                    pydirectinput.mouseUp(button='right')

# If this doesn't work, try changing the values.
# Check the values of your noteswith test-input.py