# WEEABOO v5.0.3
![](weeaboo.gif)

## WEEABOO exploitation script for game
**LMB + RMB** - *Spin curosr on tight circle*\
**MOUSE 4** - *Spam spacebar*\
**MOUSE 5** - *Spam spacebar + ctrl*

## Installation and Requirements

```
1. Install Python 3.10+
2. When installing add python to path!
3. Clone/download this repo
4. In repo folder run:
    python -m pip install -r requirements.txt

    OR

    pip install pywin32
    pip install keyboard

5. Run weeaboo.py
```

## About config
<sub>*Delay for mouse cursor rotation. (0 = random between 0.0015 - 0.005)*</sub>\
**circle_delay = 0**\
<sub>*Circle spin radius multiplier*</sub>\
**circle_multiplier = 2**\
<sub>*Spam spacebar delay*</sub>\
**bh_mouse4_delay = 0.01**\
<sub>*Superglide delay, perfect value is:* **10 / YOUR_FPS_LOCK** *(0.004 ok for 240 fps lock)*</sub>\
**sg_mouse5_delay = 0.004**\
<sub>*Key press check time*</sub>\
**keypress_detect = 0.1**


## Changelog v5.0.3
**[**+**]** *CPU load fix*