from typing import Final
VERSION: Final = "5.1.0"

from PICTURES import *

from win32api import GetKeyState, mouse_event
from win32con import MOUSEEVENTF_MOVE
from keyboard import press, release

from ctypes import windll, c_long, pointer, sizeof, c_ulong, c_uint, c_wchar, c_short, Structure
from random import choice
from os import remove
from os.path import isfile
from math import pi, sin, cos
from time import sleep
import configparser

GREETING =f"""{choice(PICTURES)}
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ WEEABOO      ┃ LMB + RMB ┃ SPIN CURSOR       ┃
┃ Jitter       ┃    MS4    ┃ SPAM SPACEBAR     ┃
┃ Exploitation ┃    MS5    ┃ SPAM SPACE + CTRL ┃
┗━━━━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛
"""

def SETUP_CMD_FONTS(font_name: str) -> None:
    """
    This function setup cmd fonts,
    just a for nice anime picture UwU
    """
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(Structure):
        _fields_ = [("X", c_short), ("Y", c_short)]

    class CONSOLE_FONT_INFOEX(Structure):
        _fields_ = [("cbSize", c_ulong),
                    ("nFont", c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", c_uint),
                    ("FontWeight", c_uint),
                    ("FaceName", c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 18
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = font_name

    handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetCurrentConsoleFontEx(handle, c_long(False), pointer(font))

def SETUP_CONFIG(config_name: str) -> None:
    """
    Create config file
    """
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'CIRCLE_SPEED', "0.0001")
    config.set('Settings', 'POINTS', "30")
    config.set('Settings', 'CIRCLE_RADIUS', "1.3")
    config.set('Settings', 'BH_MOUSE4_DELAY', "0.05")
    config.set('Settings', 'SG_MOUSE5_DELAY', "0.004")
    config.set('Settings', 'KEYPRESS_DETECT', "0.01")
    with open(config_name, 'w') as config_file:
        config.write(config_file)

def LOAD_CONFIG(config_name: str) -> None:
    """
    Load config file and set variables
    """
    global CIRCLE_SPEED, POINTS, CIRCLE_RADIUS, BH_MOUSE4_DELAY, SG_MOUSE5_DELAY, A_ITERATIONS, B_ITERATIONS, KEYPRESS_DETECT

    config = configparser.ConfigParser()
    config.read(config_name)
    CIRCLE_SPEED = config.getfloat('Settings', 'CIRCLE_SPEED')
    POINTS = config.getint('Settings', 'POINTS')
    CIRCLE_RADIUS = config.getfloat('Settings', 'CIRCLE_RADIUS')
    BH_MOUSE4_DELAY = config.getfloat('Settings', 'BH_MOUSE4_DELAY')
    SG_MOUSE5_DELAY = config.getfloat('Settings', 'SG_MOUSE5_DELAY')
    KEYPRESS_DETECT = config.getfloat('Settings', 'KEYPRESS_DETECT')

def CHECK_CONFIG(config_name: str) -> None:
    """
    Check config file exists
    """
    if isfile(config_name):
        try:
            LOAD_CONFIG(config_name)
        except:
            remove(config_name)
            SETUP_CONFIG(config_name)
            LOAD_CONFIG(config_name)
    else:
        SETUP_CONFIG(config_name)
        LOAD_CONFIG(config_name)

def MAIN(Radius: float | int, SleepTime: float | int) -> None:
    """
    Function Pre-calculates circle with math
    Main logic when pressed MOUSE1 & MOUSE2, MOUSE4, MOUSE5
    """
    CIRCLE_POINTS = []
    STEPS = POINTS  # How many points in circle? This setups with config.ini
    for i in range(STEPS):
        Angle = (2 * pi * i) / STEPS  # Rads
        dx = int(Radius * cos(Angle))  # X
        dy = int(Radius * sin(Angle))  # Y
        CIRCLE_POINTS.append((dx, dy))
    
    STEP = 0

    while True:
        if GetKeyState(0x01) < 0 and GetKeyState(0x02) < 0:
            dx, dy = CIRCLE_POINTS[STEP]
            mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)
            STEP = (STEP + 1) % STEPS

        elif GetKeyState(0x06) < 0:
            press('spacebar')
            release('spacebar')
            sleep(BH_MOUSE4_DELAY)

        elif GetKeyState(0x05) < 0:
            press('spacebar')
            sleep(SG_MOUSE5_DELAY)
            press('ctrl')
            release('spacebar')
            release('ctrl')

        else:
            STEP = 0
            sleep(KEYPRESS_DETECT)
        sleep(SleepTime)  # FIX CPU LOAD

if __name__ == "__main__":
    print(f"WEEABOO Jitter Exploitation v{VERSION}")
    CHECK_CONFIG("config.ini")
    SETUP_CMD_FONTS("NSimSun")
    print(GREETING)
    MAIN(CIRCLE_RADIUS, CIRCLE_SPEED)