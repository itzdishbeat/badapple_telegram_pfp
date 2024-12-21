# badapple_telegram_pfp

Change your Telegram profile picture with a frame-by-frame animation of "Bad Apple" or your custom frames!

## Description

badapple_telegram_pfp is a Python project that allows you to automatically change your Telegram profile picture (PFP) to create an animated effect. By default, it uses the frames from the famous "Bad Apple" animation, but you can also use your own custom frames.

## Features

- Automatically changes your Telegram profile picture at regular intervals
- Comes with pre-loaded "Bad Apple" animation frames
- Supports custom frame animations by adding your own images to the "frames" folder
- Easy to set up and run

## Requirements

- Python 3.6+
- Telethon library
- A Telegram account
- Telegram API ID and Hash (obtainable from https://my.telegram.org)

## Installation

1. Clone this repository:
   `git clone https://github.com/itzdishbeat/badapple_telegram_pfp.git`

2. Navigate to the project directory:
   `cd badapple_telegram_pfp`

3. Install the required dependencies:
   `pip install -r requirements.txt`

4. Insert your Telegram API ID and hash (obtainable from https://my.telegram.org) inside installpfp.py file

5. Run the project:
   `python installpfp.py`

If you want to use your custom animation, insert your .jpg images into frames folder and run command:
`python clearframes.py`
