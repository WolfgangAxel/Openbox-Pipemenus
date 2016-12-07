#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ConkyPipe.py
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
# with a bunch of .conkyrc files (henceforth referred to as /conky).
#             Default assumption is ~/.config/conky)
# It also assumes that you have conky set up to open ~/.conkyrc
# This script is somewhat limited since it only allows for one conky
# to be loaded. It works for my needs, if it doesn't for you, feel
# free to suggest an update.

conkyDir = '~/.config/conky'

from os import popen
from re import match

print("""<openbox_pipe_menu>
  <item label="Restart">
    <action name="Execute">
      <execute>sh -c "killall conky; conky -c .conkyrc"</execute>
    </action>
  </item>
  <item label="Kill">
    <action name="Execute">
      <execute>killall conky</execute>
    </action>
  </item>
  <separator/>""")
for item in popen('ls '+conkyDir+'/*.conkyrc').readlines():
	rip = match("(.*)[/](.*).conkyrc",item)
	path = rip.group(1)
	name = rip.group(2)
	print '  <item label="'+name.replace('&','&amp;').replace("'","&apos;").replace("_","__")+'">'
	print '    <action name="Execute">'
	print "      <execute>sh -c 'ln -f -s "+path+"/"+name.replace('&','&amp;').replace("'","&apos;")+".conkyrc ~/.conkyrc &amp;&amp; killall conky; conky -c .conkyrc'</execute>"
	print "    </action>"
	print "  </item>"
print "</openbox_pipe_menu>"
