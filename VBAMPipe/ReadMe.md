# VBAMPipe
I figured out that Pulseaudio would randomly hiccup and cause VBA-M to crash on my system. Tired of needing to kill it, start my game, then remembering to restart it afterwards, I wrote a script to manage it for me (Random-Projects -> VBAM-Bash-Menu). That script got overhauled in Python and turned into a pipe menu.

This pipe menu assumes you have one directory where you store all of your .gb* files. It also assumes that you have a gba_bios.bin inside of that folder. Feel free to fork this if you feel the need for recursive searches or whatever else.

## Requirements
* VBA-M
* a "GameBoy" directory
 * contains all your .gb* files
 * contains a gba_bios.bin
* PulseAudio (causing random crashing of VBA-M)

## Instructions
After the first comment block, paste the full path to your "GameBoy" directory inbetween the single-quotes after `gamedir`.

If you want to remove the bios requirement, just delete `--bios="+gamedir+"gba_bios.bin` from the `<execute>` line.
