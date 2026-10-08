# Piano Controller 🎹

A collection of Python scripts that lets you use a **MIDI keyboard as a controller for different games**.

Each script listens for notes played on a MIDI keyboard and converts those notes into keyboard or mouse inputs for a specific game. This makes it possible to play games such as Geometry Dash, Tetris, Mario Kart DS, and Grand Theft Auto V using a piano or MIDI keyboard.

> **⚠️ Disclaimer:** I did **not use AI to write the code in this project**. I'm also not particularly good at programming, so the code is definitely not perfect and there are probably better ways to do almost everything here.
>
> The scripts are written in Python, which means they aren't exactly optimized for speed. They would probably run faster if they were rewritten in **C++**, but I don't plan on doing that. If you want to improve the code, rewrite it, optimize it, or do whatever else you want with it, **go for it!**

## How it works

The scripts use the [`mido`](https://mido.readthedocs.io/) Python library to listen for MIDI input.

When you press a key on your MIDI keyboard:

1. The MIDI keyboard sends a MIDI message.
2. `mido` receives the message.
3. The script checks which MIDI note was played.
4. That note is mapped to a keyboard or mouse action.
5. The corresponding input is sent to the game.

For example, in the Tetris script, playing MIDI note `61` sends the **Down Arrow** key, while MIDI note `62` sends **Left Arrow**.

The exact MIDI note numbers depend on your keyboard and how the script was configured.

---

## Requirements

You will need:

* Python 3
* A MIDI keyboard or other MIDI input device
* The required Python packages
* A game that accepts the keyboard/mouse inputs being simulated

### Python packages

Most scripts require:

```bash
pip install mido keyboard
```

The GTA V script additionally requires:

```bash
pip install pydirectinput
```

You may also need to install/configure a MIDI backend for `mido`, depending on your operating system and setup.

---

## Finding your MIDI note numbers

If the scripts don't work with your MIDI keyboard, the first thing you should do is run:

```bash
python test-input.py
```

Then play different keys on your MIDI keyboard.

The program will print the MIDI note number for each key you press.

For example:

```text
60
61
62
63
64
```

You can then use those values to change the note mappings in the individual game scripts.

This is particularly useful because different MIDI keyboards may have different ranges or configurations.

---

# Scripts

## `geometrydash-piano.py`

Controls **Geometry Dash** using a MIDI keyboard.

The script is relatively simple: whenever a MIDI note is pressed, it presses the **Space** key. When the note is released, it releases Space.

### Controls

| MIDI input | Game input |
| ---------- | ---------- |
| Any note   | Space      |

This allows a MIDI keyboard to control the jumping action in Geometry Dash.

---

## `tetris-piano.py`

Controls Tetris using a MIDI keyboard.

The script maps specific MIDI notes to movement and other controls.

### Controls

| MIDI note | Action       |
| --------: | ------------ |
|      `61` | Down         |
|      `62` | Left         |
|      `63` | Up           |
|      `64` | Right        |
|      `65` | Drop / Space |

If these notes don't match your MIDI keyboard, use `test-input.py` and change the values in the script.

---

## `mariokartds-piano.py`

Controls **Mario Kart DS** using a MIDI keyboard.

The script uses MIDI note presses and releases to control the game's keyboard inputs.

### Controls

| MIDI note | Action     | Key         |
| --------: | ---------- | ----------- |
|      `48` | Left       | Left Arrow  |
|      `52` | Right      | Right Arrow |
|      `72` | Accelerate | X           |
|      `74` | Brake      | Z           |
|      `76` | Drift      | W           |
|      `73` | Item       | Q           |

As with the other scripts, these MIDI note values may need to be changed depending on your keyboard.

---

## `grandtheftautoV-piano.py`

Controls **Grand Theft Auto V** using a MIDI keyboard.

This is the most complicated script in the project because it controls both the keyboard and mouse.

It uses:

* `keyboard` for keyboard input
* `pydirectinput` for mouse input

### Keyboard controls

| MIDI note | Action       | Key   |
| --------: | ------------ | ----- |
|      `59` | Sprint       | Shift |
|      `62` | Move Left    | A     |
|      `63` | Move Forward | W     |
|      `64` | Move Back    | S     |
|      `65` | Move Right   | D     |
|      `67` | Enter Car    | F     |

### Mouse controls

| MIDI note | Action                    |
| --------: | ------------------------- |
|      `77` | Shoot / Left Mouse Button |
|      `79` | Aim / Right Mouse Button  |
|      `83` | Look Left                 |
|      `84` | Look Down                 |
|      `85` | Look Up                   |
|      `86` | Look Right                |

The look controls use relative mouse movement rather than holding a keyboard key.

---

## `test-input.py`

A simple utility for checking the MIDI note values produced by your keyboard.

It doesn't control a game. Instead, it prints the note number whenever a MIDI message is received.

Run it with:

```bash
python test-input.py
```

Then press keys on your MIDI keyboard.

This is the easiest way to figure out which values you need to use when modifying the other scripts.

---

# Configuration

The scripts currently use:

```python
with mido.open_input() as inport:
```

This opens a MIDI input device and listens for messages from it.

If you have multiple MIDI devices connected, you may need to modify the code to select a specific MIDI input port.

You can use Mido to inspect the available MIDI ports, for example:

```python
import mido

print(mido.get_input_names())
```

Then you can specify the desired input when opening the port.

---

# Customizing the controls

The controls are intentionally fairly easy to modify.

For example, this section of `tetris-piano.py`:

```python
case 61:
    keyboard.press_and_release("down")
```

means that MIDI note `61` triggers the Down Arrow key.

You could change it to another MIDI note:

```python
case 60:
    keyboard.press_and_release("down")
```

or change the action entirely:

```python
case 60:
    keyboard.press_and_release("space")
```

The same basic idea applies to the other scripts.

---

# Important notes

### MIDI note numbers

The numbers in the scripts are **MIDI note numbers**, not necessarily the names of the keys printed on your piano.

If a script doesn't respond correctly, check the values using:

```bash
python test-input.py
```

### Key presses and releases

Some scripts distinguish between `note_on` and `note_off`.

For example, in the Geometry Dash script:

* MIDI note pressed → Space is pressed
* MIDI note released → Space is released

This allows the game to receive an input for the same duration as the MIDI note.

### Game compatibility

The scripts simulate keyboard and mouse input rather than directly communicating with the games.

Because of this, compatibility can depend on:

* The operating system
* The game
* How the game handles keyboard/mouse input
* Permissions
* Other software running at the same time

---

# Project status

**This project is no longer actively developed.**

I originally made these scripts as a way to experiment with controlling games using a MIDI keyboard. They work as examples, but they aren't intended to be a polished or highly optimized framework.

If you want to:

* Fix bugs
* Optimize the scripts
* Add more games
* Add configuration files
* Improve MIDI device selection
* Rewrite the project
* Convert it to C++
* Make the code less terrible

**Please do!**

Anyone is welcome to use the code as a starting point and build upon it.

---

# Contributing

Since I don't plan on actively developing this project, there is no strict development roadmap.

If you want to improve the project, feel free to fork it and make whatever changes you think are useful.

Some things that could be improved include:

* Better MIDI device selection
* A shared input/mapping system instead of duplicated code
* Configuration files for key mappings
* Better error handling
* Better cross-platform support
* More games
* More efficient input handling
* A proper GUI
* Rewriting performance-critical parts in C++

Pull requests and forks are welcome.

---

# License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.

You are free to use, modify, and redistribute this software under the terms of the GPLv3. Any modified or redistributed versions must comply with the terms of the license.

See the [`LICENSE`](LICENSE) file for the full license text.


---

# Final disclaimer

This project was made for experimentation and entertainment.

The code is provided **as-is**, without any guarantee that it will work correctly, efficiently, or at all on your particular setup.
