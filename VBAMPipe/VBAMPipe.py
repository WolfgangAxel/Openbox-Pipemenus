#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VBAMPipe.py
#  
#  2016 Keaton Brown <linux.keaton@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  

# This script operates under the assumption that you have a directory
# with a bunch of .gba files (henceforth referred to as /GameBoy).
# It also assumes that you have a gba_bios.bin file in that directory.
# If you don't have the gba_bios.bin, delete "--bios="+gamedir+"gba_bios.bin"
# in the command below.

# Paste the full path to your /GameBoy folder inbetween the single quotes
gamedir=''

## Imports
from os import popen
import re

## Menu building
print "<openbox_pipe_menu>"
# Because I'm both inconsistent and lazy
if gamedir[-1] != '/':
	gamedir=gamedir+'/'
gamedir=gamedir.replace('&','&amp;')
for game in popen("ls "+gamedir+"*.g*").readlines():
  # Get the name of the game from the ls output
	name = re.match('(?i)'+gamedir+'(.*).g.*',game).group(1).replace('&','&amp;')
	print '  <item label="'+name+'">'
	print '    <action name="Execute">'
  # Kill pulseaudio, launch the game, then restart pulseaudio.
  # Pulse has always caused vbam to sporatically crash for me
	print "      <execute>sh -c \"pulseaudio -k; vbam --opengl-nearest --pause-when-inactive --flash-size=1 --bios="+gamedir+"gba_bios.bin --rtc '"+game[:-1].replace('&','&amp;')+"';pulseaudio --start\"</execute>"
	print "    </action>"
	print "  </item>"

print "</openbox_pipe_menu>"
