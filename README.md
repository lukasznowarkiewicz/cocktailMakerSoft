# CocktailMakerSoft

## Overview
This project includes a Python application with a graphical interface for a cocktail maker machine, as well as firmware for the Raspberry Pi Pico, which controls the physical devices within the machine.

## Files and Directories:
- `PicoFirmware`: Contains the firmware for the Raspberry Pi Pico as an Arduino IDE project.
- `Drinks`: Contains images of the drinks.
- `recipes.json`: A configuration file that includes all the drink recipes in the form of commands sent to the Pi Pico, along with paths to their respective icons.
- `main.py`: Contains the main Python application.


## Libraries used:
- `customtkinter`: A library that extends `tkinter` with additional widgets and a modern look for creating GUI applications.
- `os`: Provides a way to use operating system dependent functionality like reading or writing to the filesystem.
- `json`: Used for parsing and outputting JSON data, useful for handling configuration files like `recipes.json`.
- `PIL` (Python Imaging Library), accessed via `from PIL import Image`: A library for opening, manipulating, and saving many different image file formats.
- `functions`: A custom module, presumably containing specific functions used across the application.


