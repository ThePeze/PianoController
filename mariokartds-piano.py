import mido
import keyboard

with mido.open_input() as inport:
    for message in inport:
        if(str(message).startswith("note_on")):
            match message.note:
                case 48:
                    keyboard.press("left")
                    print("Left")
                case 52:
                    keyboard.press("right")
                    print("Right")
                case 72: 
                    keyboard.press("x")
                    print("Accelerate")
                case 74:
                    keyboard.press("z")
                    print("Brake")
                case 76:
                    keyboard.press("w")
                    print("Drift")
                case 73:
                    keyboard.press("q")
                    print("Item")
                case _:
                    print("No Action")

        elif(str(message).startswith("note_off")):
            match message.note:
                case 48:
                    keyboard.release("left")
                    print("Left")
                case 52:
                    keyboard.release("right")
                    print("Right")
                case 72: 
                    keyboard.release("x")
                    print("Accelerate")
                case 74:
                    keyboard.release("z")
                    print("Brake")
                case 76:
                    keyboard.release("w")
                    print("Drift")
                case 73:
                    keyboard.release("q")
                    print("Item")

# If this doesn't work, try changing the values.
# Check the values of your noteswith test-input.py