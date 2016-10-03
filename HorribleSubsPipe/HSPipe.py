#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  HSPipe.py
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

# The default is to use the ~/Videos folder. To specify a different
# folder, paste the full path to your anime folder in between the ''s
# Note: leave off the trailing / (~/Videos not ~/Videos/)

myAnimeFolder=''

## Importing

if myAnimeFolder == '':
	from os.path import expanduser
	myAnimeFolder=expanduser('~')+'/Videos'

from re import match
import requests
from lxml import html

### Definitions

def buildShowList(array):
	List = []
	for listing in array:
		show=[]
		## Match the show title and the quality as per HS's naming conventions
		Entry = match('(?i)\[HorribleSubs\] (.* )+\[(.{4,5})\]',listing.text_content())
		try: ## Tries to grab show title
			title = Entry.group(1)
			quals = Entry.group(2)
		except: ## Probably a NotHorribleSubs torrent
			try:
				Entry = match('(?i)\[(.*)\] (.* )+\[(.{4,5)\]',listing.text_content())
				title = Entry.group(2)+'['+Entry.group(1)+'] '
				quals = Entry.group(3)
			except: ## If it still isn't matching, something is wrong with it.
				continue
		## Search List for the show (consolidates the different qualities)
		if [title] not in (x[0] for x in List):
			show.append([title])
			new=True
		else:
			## find the index of the title in List
			index = [n for n,(i,s) in enumerate(List) if i == [title]]
			new=False
		## create the download link as per nyaa.se's url conventions
		link=listing.attrib['href'].replace("//","").replace("view","download")
		if new:
			show.append([[quals,link]])
			List.append(show)
		else:
			List[index[0]][1].append([quals,link])
	return List

### Begin piping

## Search Nyaa.se for the recent HS torrents
page = requests.get("http://www.nyaa.se/?page=search&cats=1_0&filter=0&term=%5BHorribleSubs%5D")
page = html.fromstring(page.content)
torrs = page.xpath('//td[@class="tlistname"]/a')
## Create an array in the format of [ [show name], [ [ quality, link], [ quality, link]... ] ]...
currEps = buildShowList(torrs)
print "<openbox_pipe_menu>"
for ep in sorted(currEps,key=lambda nm: nm[0]): ## alphabetizes the menu
	## set the download folder to be myAnimeFolder/the title of the show
	try:
		folder = myAnimeFolder+"/"+match("(.*)( - | \(.*\))",ep[0][0]).group(1).replace('&','&amp;').replace("'","&apos;")
	except:
		if ep[0][0][-1] == ' ':
			ep[0][0] = ep[0][0][:-1]
			folder = ep[0][0].replace('&','&amp;').replace("'","&apos;")
		else:
			print "  <separator label='Error with "+ep[0][0].replace('&','&amp;').replace("'","&apos;")+"' />"
			continue
	## make a submenu for the available qualities
	print "  <menu id='"+ep[0][0].replace(' ','').replace('&','&amp;').replace("'","&apos;")+"' label='"+ep[0][0].replace('&','&amp;').replace("'","&apos;")+"'>"
	for qual,link in sorted(ep[1], key=lambda qt: eval(qt[0][:-1])):
		## make the menu item for each quality
		print "    <item label='"+qual.replace('&','&amp;')+"'>"
		print "      <action name='Execute'>"
		##                The menu commands do the following:
		## attempt to make a folder in myAnimeDownloads; wget the .torrent
		## file; start transmission-cli downloading; when finished downloading,
		## remove the .torrent file, then remove all torrents from the queue
		print '        <execute>x-terminal-emulator --command=\'mkdir "'+folder+'"; wget --output-document="'+folder+'/thisShow.torrent" "'+link.replace('&','&amp;')+'"&amp;&amp; transmission-cli --uplimit=0 -D --download-dir="'+folder+'" "'+folder+'/thisShow.torrent"&amp;&amp; rm "'+folder+'/thisShow.torrent"&amp;&amp; rm ~/.config/transmission/torrents/*\'</execute>"'
		print "      </action>"
		print "    </item>"
	print "  </menu>"
print "</openbox_pipe_menu>"
