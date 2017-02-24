#!/usr/bin/env python3
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

from sys import argv
args = [arg for arg in argv]

if ("-h" or "--help") in args:
    print("Unofficial HorribleSubs OpenBox Pipemenu\n"
    "Usage: python3 "+__file__+" [OPTIONS]\n"
    "Options:\n"
    "  -h/--help    This help\n"
    "  -d DIR       Specify a download directory\n"
    "  -l LIMIT     Limit to a certain number of menu items\n"
    )
    exit()

if "-l" in args:
    limit = eval(args[args.index('-l')+1])
else:
    limit = 300 ## Arbitrary number

from os.path import exists,expanduser
## Check args for directory, check if it exists
## Default to ~/Videos or just ~ if other not specified or doesn't exist
myAnimeFolder = False
if "-d" in args:
    argdir = args[args.index('-d')+1]
    if exists(expanduser(argdir)):
        myAnimeFolder = expanduser(argdir)
if not myAnimeFolder:
    if exists(expanduser("~/Videos")):
        myAnimeFolder = expanduser("~/Videos")
    else:
        myAnimeFolder = expanduser("~")

## Normalize folder
if myAnimeFolder[-1] == '/':
    myAnimeFolder = myAnimeFolder[:-1]

from re import match
from requests import get
from bs4 import BeautifulSoup as BS

### Definitions

def buildShowList(soup):
    List={}
    for item in soup.find_all('item'):
        DL = []
        Entry = match('(?i)\[HorribleSubs\] (.* )+\[(.{4,5})\]',item.title.string)
        try: ## Tries to grab show title
            title = Entry.group(1)
            qual = Entry.group(2)
        except: ## Probably a NotHorribleSubs torrent
            try:
                Entry = match('(?i)\[(.*)\] (.* )+\[(.{4,5)\]',item.title.string)
                title = Entry.group(2)+'['+Entry.group(1)+'] '
                qual = Entry.group(3)
            except: ## If it still isn't matching, something is wrong with it.
                continue
        ## Get the download link
        link = item.link.string
        ## Add it to the dictionary, or not.
        try:
            List[title].append([qual,link])
        except:
            if len(List) >= limit:
                break
            List[title] = [[qual,link]]
    return List

def XMLFriendly(s):
    return s.replace('&','&amp;').replace("'","&apos;").replace("_","__")



if exists(myAnimeFolder+"/WatchList"):
    with open(myAnimeFolder+"/WatchList","r") as WL:
        watchList = WL.read().splitlines()
else:
    watchList = []

### Begin piping

## Search Nyaa.se for the recent HS torrents
page = get("https://www.nyaa.se/?page=rss&cats=1_0&term=%5BHorribleSubs%5D")
soup = BS(page.content,'html.parser')
## Create a dictionary with arrays of qualities and download links separated by show title
currEps = buildShowList(soup)
for show in currEps:
    if show[-1] == ' ':
        currEps[show[:-1]] = currEps.pop(show)
print("<openbox_pipe_menu>")
print("  <item label='HorribleSubs.info'>\n"
      "    <action name='Execute'>\n"
      "      <execute>x-www-browser www.horriblesubs.info</execute>\n"
      "    </action>\n"
      "  </item>\n"
      "  <menu id='DLTO' label='Downloading to...'>\n"
      "    <separator label='"+myAnimeFolder+"'/>\n"
      "  </menu>\n"
      "  <separator/>")
for show in sorted(currEps, key=lambda l: l.lower()): ## alphabetizes the menu
    ## set the download folder to be myAnimeFolder/the title of the show
    try:
        folder = XMLFriendly(myAnimeFolder+"/"+match("(.*)( - | \(.*\))",show).group(1))
    except:
        folder = XMLFriendly(myAnimeFolder+"/"+show)
    ## make a submenu for the available qualities
    title = folder.replace(myAnimeFolder+"/","")
    if title in watchList:
        print("  <menu id='"+XMLFriendly(show)+"' label='WL! --> "+XMLFriendly(show)+"'>")
        print("    <item label='Remove from Watch List'>")
        print("      <action name='Execute'>")
        print("        <execute>sh -c \"sed -i '/"+title+"/d' "+myAnimeFolder+"/WatchList\"</execute>")
    else:
        print("  <menu id='"+XMLFriendly(show)+"' label='"+XMLFriendly(show)+"'>")
        print("    <item label='Add to Watch List'>")
        print("      <action name='Execute'>")
        print("        <execute>sh -c \"echo "+title+" >> "+myAnimeFolder+"/WatchList\"</execute>")
    print("      </action>")
    print("    </item>")
    print("    <separator/>")
    for qual,link in sorted(currEps[show], key=lambda qt: eval(qt[0][:-1])):
        ## If it already is downloaded, say so
        if exists(folder+"/[HorribleSubs] "+show+" ["+qual+"].mkv"):
            print("    <separator label='Already downloaded "+qual+"'/>")
            continue
        ## otherwise, make the menu item for each quality
        print("    <item label='"+qual+"'>")
        print("      <action name='Execute'>")
        ##                The menu commands do the following:
        ## attempt to make a folder in myAnimeFolder; cd into it;
        ## start the bittorrent download using the curses interface
        print('        <execute>x-terminal-emulator --command=\'mkdir "'+folder+'";'
              'cd "'+folder+'"&amp;&amp;'
              'btdownloadcurses --max_uploads 0 "'+XMLFriendly(link)+'"\'</execute>"')
        print("      </action>")
        print("    </item>")
    print("  </menu>")
print("</openbox_pipe_menu>")
