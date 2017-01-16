#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  SteamFriendsPipe.testing.py
#  
#  Copyright 2016 keaton <linux.keaton@gmail.com>
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
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Find your Steam ID by going to steamrep.com, entering your username,
# then copying the "steamID64" here.

ID = ""

from requests import get
from bs4 import BeautifulSoup as BS
import asyncio

# Get your list of friends
MyFriends=get("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=986110846FF5B222E6FA4B4FDBD552AE&steamid="+ID+"&relationship=friend&format=xml")
soup = BS(MyFriends.content,"html.parser")
offlineFriends=[]
onlineFriends=[]
# Just to make the next section more readable
friendLink="http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=986110846FF5B222E6FA4B4FDBD552AE&steamids="

# I don't fully understand how this works, but it does.
# It should download 5 of your friends' statuses concurrently.
# As they finish, the next one in line starts until you're out of friends
async def getFriends():
	# Make a loop?
	loop = asyncio.get_event_loop()
	# This I get. Make an array of "Future" objects
	# None is for designating an executor (which we don't need, hence None)
	# get is the function it uses
	# next portion is the arguments for said function
	# and we do this for each of your Steam friends
	pages = [ loop.run_in_executor( None, get, friendLink+friend.string+"&format=xml")
			for friend in soup.find_all('steamid') ]
	# I think this just stops the script while we wait for downloading to finish
	for response in await asyncio.gather(*pages):
		pass
	# Return that array
	return pages
# Make a loop (again?)?
yourFriends = asyncio.get_event_loop()
# Run that loop until it finishes and return the list of "Futures"
pages = yourFriends.run_until_complete(getFriends())
for page in pages:
	# Turn the "Future" into a response object
	page = page.result()
	# Parse it
	summary = BS(page.content,"html.parser")
	userid = summary.response.players.player.steamid.string
	username = summary.response.players.player.personaname.string
	publicStatus = summary.response.players.player.personastate.string
	if publicStatus=='0':
		offlineFriends.append([username,userid])
	else:
		onlineFriends.append([username,userid])
# Make the menu
print("<openbox_pipe_menu>")
print("""  <menu id="status" label="Set status">
    <item label="Online">
      <action name="execute">
        <execute>steam steam://friends/status/online</execute>
      </action>
    </item>
    <item label="Busy">
      <action name="execute">
        <execute>steam steam://friends/status/busy</execute>
      </action>
    </item>
    <item label="Offline">
      <action name="execute">
        <execute>steam steam://friends/status/offline</execute>
      </action>
    </item>
  </menu>""")

# Only show these submenus if friends exist in them
# (i.e. is all friends are offline, don't show the Online section
if len(onlineFriends) != 0:
	print('  <separator label="Online"/>')
	for username,userid in sorted(onlineFriends):
		print("""  <item label='"""+username.replace('&','&amp;').replace("'","&apos;").replace("_","__")+"""'>
    <action name='Execute'>
      <execute>steam steam://friends/message/"""+userid+"""</execute>
    </action>
  </item>""")
if len(offlineFriends) != 0:
	print('  <separator label="Offline"/>')
	for username,userid in sorted(offlineFriends):
		print("""  <item label='"""+username.replace('&','&amp;').replace("'","&apos;").replace("_","__")+"""'>
    <action name='Execute'>
      <execute>steam steam://friends/message/"""+userid+"""</execute>
    </action>
  </item>""")
print("</openbox_pipe_menu>")
