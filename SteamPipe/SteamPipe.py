#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Default is ['~/.steam/steam/steamapps/']
# Add another steamapps folder by adding a comma just before the ] and pasting the directory with quotes around it
# ex. ['~/.steam/steam/steamapps/','/media/MyExternalHardDrive/Steam/steamapps/']
STEAMAPPS = ['~/.steam/steam/steamapps/']

### Menu building begins

from os import popen
from re import search

# Add Steam button to the top of the list, followd by separator
print("""<openbox_pipe_menu>"
  <item label='Steam'>
    <action name='Execute'>
      <execute>steam</execute>
    </action>
  </item>
  <separator/>""")
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
	print '  <item label="'+NAME.replace('&','&amp;')+'">'
	print '    <action name="Execute">'
	print "      <execute>steam steam://run/"+ID+"</execute>"
	print "    </action>"
	print "  </item>"

# End the menu
print "</openbox_pipe_menu>"
