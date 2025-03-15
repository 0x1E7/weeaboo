# WEEABOO v5.1.0
![](weeaboo.gif)

## WEEABOO exploitation script for game
**LMB + RMB** - *Spin curosr on tight circle*\
**MOUSE 4** - *Spam spacebar*\
**MOUSE 5** - *Spam spacebar + ctrl*

## Installation and Requirements

```
1. Install Python 3.12+ (Important! Older versions may run slower with sleep function!)
2. When installing add python to path!
3. Clone/download this repo
4. In repo folder run:
    python -m pip install -r requirements.txt

    OR

    pip install pywin32
    pip install keyboard

5. Run weeaboo.py

X. OR DOWNLOAD ZIP FROM RELEASES AND RUN _START.bat (This zip file contains Python3.13, win32api and keyboard libs)
```

## About config
<sub>*Delay for mouse cursor rotation.*</sub>\
**circle_speed = 0.0001**\
<sub>*How many points calculate in circle? Try around 20-80.*</sub>\
**points = 30**\
<sub>*Circle spin radius.*</sub>\
**circle_radius = 1.3**\
<sub>*Spam spacebar delay*</sub>\
**bh_mouse4_delay = 0.01**\
<sub>*Superglide delay, perfect value is:* **10 / YOUR_FPS_LOCK** *(0.004 ok for 240 fps lock)*</sub>\
**sg_mouse5_delay = 0.004**\
<sub>*Key press check time*</sub>\
**keypress_detect = 0.01**


## Changelog v5.1.0
**[**+**]** *Math function to calculate perfect circle*
**[**+**]** *Due to math func you can setting up float value for circle*
