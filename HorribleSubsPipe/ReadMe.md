#HorribleSubsPipe
[See it in action here.](http://imgur.com/a/D32GG)

Originally stemmed from my random-projects/HSTorr.py script. It will populate a menu with the recent HorribleSubs torrents from nyaa.se and use `btdownloadcurses` (bittorrent) to download them. All downloads will be sorted into folders based off of the name of the show inside of a sepcified download directory

## Requirements
* Python 3
 * BeautifulSoup (bs4)
 * requests
* bittorrent (`btdownloadcurses` executable)

## Instructions
The script has 3 arguments: `-h` for help, `-d` to specify a download directory, and `-l` to specify a limit for how many shows to put in the menu. The default download directory is either `~/Videos` or `~` if `~/Videos` doesn't exist, and the default limit is all recent listings.

Example usage:

Setting the pipemenu command to `python3 ~/bin/HSPipe.py -d ~/Videos/Anime -l 10` will show 10 of the most recent releases in the menu, and all downloads will direct into your `~/Videos/Anime` folder.

Setting the pipemenu command to `python3 ~/bin/HSPipe.py` will show all new releases in the menu, and download to either `~/Videos` or `~`

### Helpful tip

Ever since the migration to bittorrent over transmission-cli, multiple downloads can be ran at once. Rather than wait for the script to scrape nyaa.se 3 or 4 times while grabbing the new episodes for the day, holding `crtl` while clicking on a menu item will execute the menu item without closing the menu. This would allow you to initialize all the downloads you wish to start with only one scrape, which is ideal for both you and nyaa.se's servers. This is a lesser-known feature of OpenBox itself, so use this in all of your menus, not just this one!

## WatchList

The menu also supports the use of a WatchList to help distinguish the new releases you care about. The list is a plain text file stored in the specified download directory. If a show in that list has a new release, it will be prefaced in the menu with `WL! --> `. Shows can be added and removed from the list through the menu.
