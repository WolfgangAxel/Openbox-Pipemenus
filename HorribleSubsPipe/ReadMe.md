#HorribleSubsPipe
This is mostly recycled code from my HSTorr.py script. It will populate a menu with the recent HorribleSubs torrents from nyaa.se and use `transmission-cli` to download them. All downloads will be sorted into folders based off of the name of the show inside of the download directory

## Requirements
* Python 3
 * BeautifulSoup (bs4)
 * requests
* transmission-cli

## Instructions
The script has 3 arguments: `-h` for help, `-d` to specify a download directory, and `-l` to specify a limit for how many shows to put in the menu. The default download directory is either `~/Videos` or `~` if `~/Videos` doesn't exist, and the default limit is all recent listings.

Example usage:

`python3 ~/bin/HSPipe.py -d ~/Videos/Anime -l 10` will show 10 of the most recent releases, and all downloads will direct into your `~/Videos/Anime` folder.

`python3 ~/bin/HSPipe.py` will show all new releases in the menu and download to either `~/Videos` (or `~`)

## Caveats

There are a few weird bugs with transmission-cli that cause some torrents to quit immediately, but after a second or third attempt it will download just fine. I have no idea what's happening, how it's happening, or why it's happening. It seems like clearing out the `resume` and `torrents` folders can help, if they aren't already empty. (Note: clearing the folders is now a part of the script, so this should not be an issue. I'm leaving it here for posterity's sake)

Unfortunately, transmission-cli only allows for one download at a time. Considering this menu will likely only be used for currently airing shows, it shouldn't be too painful to just keep an eye out for when they're done.

I might look into other cli torrent packages, but it's pretty low-priority.
