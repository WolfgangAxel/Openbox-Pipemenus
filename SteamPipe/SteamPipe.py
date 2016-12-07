#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SteamPipe.py.py
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

# Default is ['~/.steam/steam/steamapps/']
# Add another steamapps folder by adding a comma just before the ] and pasting the directory with quotes around it
# ex. ['~/.steam/steam/steamapps/','/media/MyExternalHardDrive/Steam/steamapps/']
STEAMAPPS = ['~/.steam/steam/steamapps/']

### Menu building begins

from os import popen,path
from re import search

# Begin
print "<openbox_pipe_menu>"

# Check to see if Steam is running, label buttons accordingly
running = popen("ps axf | grep -i steam | grep -v SteamPipe | grep -v grep").read()
if not running:
	print("""  <item label='Steam'>
    <action name='Execute'>
      <execute>steam</execute>
    </action>
  </item>""")
else:
	print("""  <item label='Open Steam'>
    <action name='Execute'>
      <execute>steam</execute>
    </action>
  </item>
  <item label='Quit Steam'>
    <action name='Execute'>
      <execute>steam -shutdown</execute>
    </action>
  </item>""")
if path.exists(path.dirname(path.realpath(__file__))+"/SteamFriendsPipe.py"):
	print '  <menu execute="python '+path.dirname(path.realpath(__file__))+'/SteamFriendsPipe.py" id="steamfriendspipe" label="Chat"/>'
else:
	print("""  <menu id="steamchat" label="Chat">
    <item label="Open Friends">
      <action name="execute">
        <execute>steam steam://open/friends</execute>
      </action>
    </item>
    <item id="statusOnline" label="Status: Online">
      <action name="execute">
        <execute>steam steam://friends/status/online</execute>
      </action>
    </item>
    <item id="statusOnline" label="Status: Busy">
      <action name="execute">
        <execute>steam steam://friends/status/busy</execute>
      </action>
    </item>
    <item id="statusOnline" label="Status: Offline">
      <action name="execute">
        <execute>steam steam://friends/status/offline</execute>
      </action>
    </item>
  </menu>
""")
print '  <menu id="steamGames" label="Games">'
GAMES=[]
for DIR in STEAMAPPS:
	# Make sure all DIR are in the same format
	if DIR[-1] != '/':
		DIR=DIR+'/'
	# Get the .acf's in that DIR
	SOMEGAMES = popen('ls "'+DIR+'"*.acf').readlines()
	# Read the .acf's and add the game's name and ID to a list
	for GAME in SOMEGAMES:
		ACF=open(GAME.replace('\n',''),'r').read()
		# Find the appid of the game
		ID=search('"appid".*"(.*)"',ACF).group(1)
		# Find the name of the game
		NAME=search('"name".*"(.*)"',ACF).group(1)
		GAMES.append([NAME,ID])
# Make an entry for each game (and alphabetize the list)
for GAME in sorted(GAMES):
	NAME,ID=GAME
	# Make the entry
	print '    <item label="'+NAME.replace('&','&amp;').replace("'","&apos;").replace("_","__")+'">'
	print '      <action name="Execute">'
	print "        <execute>steam steam://run/"+ID+"</execute>"
	print "      </action>"
	print "    </item>"

# End the menu
print("""  </menu>
</openbox_pipe_menu>""")
