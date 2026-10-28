# Python Keyboard Shortcut Automation

A lightweight Python script that listens for global keyboard shortcuts (hotkeys) in the background and executes predefined system actions using `pynput` and `os`.

## Features

- **Global Hotkey Listener:** Works in the background across the operating system.
- **Custom Actions:**
  - Print a predefined message in the console.
  - Open the current project directory in the system File Explorer.
  - Gracefully stop the listener and exit the application via a shortcut.

## Prerequisites

- Python 3.x
- `pynput` library

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repository-folder>
   ```

2. Install the required package:
   ```bash
   pip install pynput
   ```

## Usage

Run the script from your terminal:

```bash
python main.py
```

### Default Shortcuts

| Shortcut Combination | Action |
| :--- | :--- |
| **`Ctrl + Alt + M`** | Prints a custom message in the console |
| **`Ctrl + Alt + S`** | Opens the current directory in File Explorer |
| **`Ctrl + Alt + Q`** | Stops the listener and exits the program |

*(Note: If you kept `Ctrl + S` for exiting in your code, update the table above accordingly).*

## Built With

- [pynput](https://pypi.org/project/pynput/) - For monitoring and controlling input devices.
- `os` - Python's standard library module for operating system interactions.
