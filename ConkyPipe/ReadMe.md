#ConkyPipe
A pipe menu for easily switching conkys, somewhat similar to Bunsen's Conky Chooser, but as a menu.

This script operates under the assumption that you have a directory with a bunch of .conkyrc files. It also assumes that you have conky set up to open ~/.conkyrc. This script is somewhat limited since it only allows for one conky to be loaded. It works for my needs, if it doesn't for you, feel free to suggest an update.

## Requirements
* "Conky" folder; contains all *.conkyrc files
* Conky; loads `~/.conkyrc` on boot

## Instructions
Below the first comment block, paste the path to your "conky" folder inbetween the single quotes to define `conkyDir`. Unlike my other pipes, this can have `~`, since all the commands used are able to deal with it.
