import mido
import keyboard

with mido.open_input() as inport:
    for message in inport:
        if(str(message).startswith("note_on")):
            keyboard.press("space")
            print("pressed space")
        elif(str(message).startswith("note_off")):
            keyboard.release("space")
            print("released space")