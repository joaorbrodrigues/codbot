
# Call of Dragons Bot (codbot)

**Disclaimer 1** : This bot is just for testing purposes. Using it can get you banned (obviously).

**Disclaimer 2** : I'm not a professional developer so my code might seem a bit chaotic.

**Disclaimer 3** : Many things are hard-coded and need a lot of work to improve. Example: I have 5 marches at the game, so I check if there are 5 marches before gathering resources. If you have less, you'll have to adapt it.

## Whay you need to run:

* **Knowledge**: Coding and using Google
* **OS**: Windows (but you can get it to work in Mac as well I guess)
* **Python**: Version 3.11.3 (I didn't test it in previous versions)
* **Where to run**: IDLE (comes with Python) / Pycharm (the one I used) - you must run as administrator so the clicks work.
* **Emulator**: MEmu play (https://www.memuplay.com/)
* **Screen Resolution**: 1280 x 720 - 460dpi (if you change it, the mapping will need some manual setup, but it's doable)
* **Key Mapping File**: [download here](https://drive.google.com/file/d/1j4PC_CH3IMvBgHq0b1kAvI2VhePAVrVl/view?usp=sharing) and import to MEmu
* **Packages**: 

|Name|Version|
| ----------- | ----------- |
|EasyProcess|1.1|
|MouseInfo|0.1.3|
|Pillow |9.5.0|
|PyAutoGUI|0.9.54|
|PyGetWindow|0.0.9|
|PyMsgBox|1.0.9|
|PyRect|0.2.0|
|PyScreeze|0.1.29|
|entrypoint2|1.1|
|mss|9.0.1|
|numpy|1.24.3|
|opencv-python|4.7.0.72|
|pip|22.3.1|
|pyclick|0.0.2|
|pyperclip|1.8.2|
|pyscreenshot|3.1|
|python3-xlib|0.15|
|pytweening|1.0.7|
|setuptools|65.5.1|
|six|1.16.0|
|wheel|0.38.4|
|xlib|0.21|

## Features Implemented:

* ✅ Collect resources inside the castle (they must be visible when you press Space twice)
* ✅ Tap the help button
* ✅ Donations
* ✅ Claim Gifts
* ✅ Checks if the game crashed then restarts it
* ✅ Gather (if you have free marches)

## Backlog:

* ☑️ Gather all types of resources
* ☑️ Training
* ☑️ Checking notifications before opening menus (just alliance menu missing)
* ☑️ Reading and claiming emails
* ☑️ Auto-building?