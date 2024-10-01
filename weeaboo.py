from typing import Final
VERSION: Final = "5.0.0"

from ctypes import windll, c_long, pointer, sizeof, c_ulong, c_uint, c_wchar, c_short, Structure
from time import sleep
from random import uniform
from os import system, remove
from os.path import isfile
import configparser

try:
    from keyboard import press, release
    from win32api import mouse_event, GetKeyState
except ModuleNotFoundError:
    print("Module not found error, trying to install from pip...")
    system("python -m pip install -r requirements.txt")
    system("cls")
    _ = input("The modules are installed, run the program again\n\nPress any key to close this window...")
    exit()

GREETING_PICTURE = """     
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠄⠄⠈⡀⣔⣶⢟⣫⣶⣾⣿⣿⣿⣿⣿⣿⣿⣛⣳⠶⣶⣤⣇⠤⠤⠄⣐⡂⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠻⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠠⠸⠱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⣬⡻⣿⣿⣿⣶⣦⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠈⠙⠿⠋⠄⠄⠄⠨⣷⣠⣄⣀⣀⣧⠘⡟⢿⣿⡉⠛⠿⣿⣿⣿⣿⣷⣮⡻⣿⣶⣝⠦⡙⠻⣿⣿⣿⣿⣷⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣶⡠⠊⠉⠉⠁⢠⣤⣷⡇⡈⢿⢽⡦⡀⠄⠉⠙⠻⢝⡿⣿⣎⠻⣿⣷⣌⠄⠄⠉⠻⣿⡻⢿⣷⡀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⡴⠋⠄⠄⠄⠄⠄⣿⢻⡿⠐⢀⠘⣎⢻⣮⡂⢄⢄⣀⠄⠄⠄⠙⠳⠜⣿⣿⣧⡀⠄⠄⠄⠛⣦⢻⣇⢢⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠰⠁⠄⠄⠄⠄⠄⠄⠏⣾⠃⢠⣿⣧⢻⡀⠙⠿⣷⣥⣙⠻⣷⣶⣤⣴⡀⠈⢿⣷⠹⡄⠄⠄⠄⠈⠋⡿⢑⠹⣷⣄⡀⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⠇⣠⣿⣿⣿⡄⣇⢳⣤⣈⠙⠻⢿⣶⣝⣻⢿⣷⡆⡈⠁⠄⢳⢐⡠⠄⠄⢀⠇⣾⣷⣿⣿⣿⣷⣤
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣸⣿⣿⣿⣿⣷⢸⠘⠋⣉⣉⣱⣶⣤⣤⣶⣶⣾⣟⠄⠄⣸⡞⣼⣿⣆⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣿⣿⡿⠟⠉⡀⡀⠄⠄⣈⠙⢿⣿⣿⣿⣿⣿⣿⣿⠁⣠⡶⠚⠉⠄⠙⠄⠄⢶⣄⡉⠛⢿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠂⢟⣯⣾⣿⣻⣽⠧⠈⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣾⠉⣠⡰⣄⣿⣶⠄⠄⠈⢻⣿⣷⣦⣬⣝⡛
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿⡿⠟⠉⢀⣀⠠⣶⣶⣶⣤⣯⣿⣿⣿⣿⣿⣿⣼⣇⣣⢷⠇⣛⣋⣴⡆⠄⠄⠻⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠂⠄⠄⠛⢁⢠⡖⣷⢹⣟⢻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣡⣷⣶⡝⣿⣿⣿⣿⣷⢀⡀⠄⠄⢬⣉⣙⣛
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡐⠄⠄⠄⠅⠄⠈⠳⢭⠿⢛⣋⣬⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣧⠹⣿⣿⣷⣶⠖⣴
⠄⠄⣠⠊⠄⠄⠄⠄⠄⠠⢠⠂⠄⠄⠄⠄⢱⣶⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠙⠛⠋⠾⠿
⠄⡰⠁⠄⠄⠄⠄⠄⠄⠄⠘⠄⠐⠄⠈⠠⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣼
⡸⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⠄⠄⠄⢀⣼⣿
⠁⠄⠄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢛⣛⣻⣿⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣽⣿⣌⣿⣿⣿⣿⣿⠄⠄⢀⣾⣿⣿
⠄⠄⠄⠄⠄⠄⠐⠈⠈⠢⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⢠⣿⢿⣫⣶
⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣰⣿⢣⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠠⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⡏⣸⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠁⠂⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿⣿⢀⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠂⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠄⠉⡉⣉⡉⠉⠻⠟⠛⠛⣋⣩⣴⣾⣿⠇⢰⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠤⣀⣴⣿⣷⣮⣝⡻⠋⠄⢸⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⡾⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⢀⣴⣾⣿⣿⣿⣿⣿⡟⠁⡀⣼⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠤⠚⠁⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿⣿⣿⣿⡿⠋⡠⠪⠾⠿⠿⠿⠿⢿⣿
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
    config.set('Settings', 'CIRCLE_DELAY', "0")
    config.set('Settings', 'CIRCLE_MULTIPLIER', "2")
    config.set('Settings', 'BH_MOUSE4_DELAY', "0.01")
    config.set('Settings', 'SG_MOUSE5_DELAY', "0.003")
    with open(config_name, 'w') as config_file:
        config.write(config_file)

def LOAD_CONFIG(config_name: str) -> None:
    """
    Load config file and set variables
    """
    global CIRCLE_DELAY, CIRCLE_MULTIPLIER, BH_MOUSE4_DELAY, SG_MOUSE5_DELAY, A_ITERATIONS, B_ITERATIONS

    config = configparser.ConfigParser()
    config.read(config_name)
    CIRCLE_DELAY = config.getfloat('Settings', 'CIRCLE_DELAY')
    CIRCLE_MULTIPLIER = config.getint('Settings', 'CIRCLE_MULTIPLIER')
    BH_MOUSE4_DELAY = config.getfloat('Settings', 'BH_MOUSE4_DELAY')
    SG_MOUSE5_DELAY = config.getfloat('Settings', 'SG_MOUSE5_DELAY')
    
    A_ITERATIONS = 2 * CIRCLE_MULTIPLIER
    B_ITERATIONS = 1 * CIRCLE_MULTIPLIER

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

def SLEEP(timing: float | int) -> None:
    """
    If the SLEEP function receives a value of 0,
    then it uses a random time between 0.0015 and 0.005
    """
    if timing == 0:
        sleep(uniform(0.0015, 0.005))
    else:
        sleep(timing)

def MSEVENT(DirectionX: int, DirectionY: int) -> None:
    """
    Moves the mouse cursor a specified number of pixels
    """
    mouse_event(0x01, DirectionX, DirectionY)

def MOVE_MOUSE(Vector_ONE: tuple, Vector_TWO: tuple) -> None:
    """
    Function draws a circle with moving the cursor
    """
    for i in range(A_ITERATIONS):
        MSEVENT(Vector_ONE[0], Vector_ONE[1])
    for i in range(B_ITERATIONS):
        MSEVENT(Vector_TWO[0], Vector_TWO[1])

def MAIN() -> None:
    """
    Main logic of programm
    If mouse1 and mouse2 pressed:
        MOVE_MOUSE
        SLEEP
        etc..

    elif mouse4 pressed:
        spam spacebar

    elif mouse5 pressed:
        spam spacebar + ctrl
    """
    while True:
        if GetKeyState(0x01) < 0 and GetKeyState(0x02) < 0:
                MOVE_MOUSE((1, 0), (1, 1))
                SLEEP(CIRCLE_DELAY)
                
                MOVE_MOUSE((0, 1), (-1, 1))
                SLEEP(CIRCLE_DELAY)
                
                MOVE_MOUSE((-1, 0), (-1, -1)) 
                SLEEP(CIRCLE_DELAY)
                    
                MOVE_MOUSE((0, -1), (1, -1))
                SLEEP(CIRCLE_DELAY)
        
        elif GetKeyState(0x06) < 0:
            press('spacebar')
            release('spacebar')
            SLEEP(BH_MOUSE4_DELAY)
        
        elif GetKeyState(0x05) < 0:
            press('spacebar')
            SLEEP(SG_MOUSE5_DELAY)
            press('ctrl')
            release('spacebar')
            release('ctrl')
        else:
            continue
            
if __name__ == "__main__":
    #Entry point
    print(f"WEEABOO Jitter Exploitation v{VERSION}")
    CHECK_CONFIG("config.ini")
    SETUP_CMD_FONTS("NSimSun")
    print(GREETING_PICTURE)
    MAIN()