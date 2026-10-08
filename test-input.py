import mido

with mido.open_input() as inport:
    for message in inport:
        print(message.note)

# Here you can test your midi device to determine the values of the individual notes
        
                        