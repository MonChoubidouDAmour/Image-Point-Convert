# Python Image to ASCII Converter

Convert images to ASCII art with Python! Uses a Flasks local server for the interface.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)

## Introduction

This Python script allows you to convert images into ASCII art. It takes an image file as input and generates a text-based representation of the image using ASCII characters, more precesely the 256 permutations of the `0x2800` braille characters.

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MonChoubidouDAmour/Image-Point-Convert.git
2. Start the server (make sure to open the port 5000)
   ```bash
    python server.py
3. Connect to the server at `https://locahost:5000`