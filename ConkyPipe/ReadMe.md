# ConkyPipe
A pipe menu for easily switching conkys, somewhat similar to Bunsen's Conky Chooser, but as a menu.

This script operates under the assumption that you have a directory with a bunch of .conkyrc files. It also assumes that you have conky set up to open `~/.conkyrc`. Each menu item will use `ln` to link `~/.conkyrc` to whichever conky file you designate.

This script is somewhat limited since it only allows for one conky to be loaded. It works for my needs, if it doesn't for you, feel free to suggest an update.

## Requirements
* "Conky" folder; contains all *.conkyrc files
* Conky; loads `~/.conkyrc` on boot

## Instructions
 * Use the `-d` argument to define your Conky folder if you keep them somewhere other than `~/.config/conky`. If `~/.config/conky` doesn't exist and -d isn't used, `~` will be used.
 * Use the `-e` argument to define your preferred editor for the "Edit" menu item. Default is `x-terminal-emulator editor`. 
  * NOTE: Use this argument last, as it interprets the rest of the command line as the editor command
 * `-h` will print a help dialog in the terminal or cause the pipe to break if you call it in the menu.

## Examples
`python3 ConkyPipe.py` will assume all defaults.

`python3 ConkyPipe.py -d ~/Rice/Conky` will scan `~/Rice/Conky` for your `.conkyrc` files.

`python3 ConkyPipe.py -d ~/Rice/Conky -e geany -i -s -p` will scan the same as above, and also set `geany -i -s -p` as the editor command for the "Edit" menu item.
