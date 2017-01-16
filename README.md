# Openbox-Pipemenus
Homegrown pipe menus of various usages. Per-menu instructions are found in the appropriate ReadMes. Menus use Python 3.5+, but other packages may be required; individual package requirements are listed in the appropriate ReadMes.

## General instructions
To add a pipe menu to your menu, first download one of the scripts (to a logical folder, such as `~/bin/pipes` perhaps). Next, open `~/.config/openbox/menu.xml` and add the following line wherever it seems logical to you: `<menu execute="python3 '/PATH/TO/THIS/FILE/PIPE.py'" id="PIPE" label="PIPE"/>`, replacing `PIPE` and `/PATH/TO/THIS/FILE/` with whatever is necessary.

Alternatively, if you use ObMenu, go to Add->Pipemenu, change the Label to whatever you want the menu entry to be called, change the Id to something unique (such as the filename of the pipe), and change the Execute to `python3 '/PATH/TO/THIS/FILE/PIPE.py'`, once again replacing `PIPE` and `/PATH/TO/THIS/FILE/` with whatever is necessary.
