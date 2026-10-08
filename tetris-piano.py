import mido
import keyboard

with mido.open_input() as inport:
    for message in inport:
        print(message.note)
        if(str(message).startswith("note_on")):
            match message.note:
                case 61:
                    keyboard.press_and_release("down")
                    print("down")
                case 62:
                    keyboard.press_and_release("left")
                    print("Left")
                case 63: 
                    keyboard.press_and_release("up")
                    print("Up")
                case 64:
                    keyboard.press_and_release("right")
                    print("right")
                case 65:
                    keyboard.press_and_release("space")
                    print("drop")
                case _:
                    print("No Action")

# If this doesn't work, try changing the values.
# Check the values of your noteswith test-input.py