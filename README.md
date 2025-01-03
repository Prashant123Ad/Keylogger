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


