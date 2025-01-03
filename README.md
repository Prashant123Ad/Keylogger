# Keylogger
This Python script is a basic keylogger that captures keyboard events and sends the keystrokes to a remote server.
# Keylogger with Remote Server

## Description

This Python script is a basic keylogger that captures keyboard events (key presses) and sends the keystrokes to a remote server. It uses the `keyboard` module to monitor key presses and the `socket` module to transmit the captured data over a network. The keylogger connects to a specified IP address and port to send the keystroke data until the "Esc" key is pressed.

> **Important Note**: This keylogger is for educational purposes only. Unauthorized use is illegal and unethical. Always obtain proper consent before using or distributing such tools.

## Features
- Listens for keyboard events (key presses).
- Sends captured keystrokes to a remote server.
- Stops logging when the "Esc" key is pressed.

## Requirements
- Python 3.x
- `keyboard` module (can be installed via pip)
- `socket` module (comes with Python by default)

## Installation

1. **Clone this repository** or download the script.
   ```bash
   git clone https://github.com/Prashant123Ad/Keylogger.git

2. Install required modules:
    ```bash
   pip install keyboard

Usage

1. Start the Keylogger

Modify the host and port variables in the keylogger script with the IP address and port of your server.

Run the keylogger script:

   ```bash
   python victim.py
```
2. Start the Server

Run the server script to receive keystrokes:

```bash
python server.py
```

The keylogger will start capturing and sending the keystrokes to the server.
Stop the Keylogger

3. Press the "Esc" key to stop logging and terminate the keylogger.
Disclaimer

This keylogger is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit consent from users before monitoring any device or system. Misuse of this code can have serious legal consequences.

License

This project is open-source. You are free to use, modify, and distribute it for educational purposes, but you must respect privacy and legal guidelines.
