#HorribleSubsPipe
This is mostly recycled code from my HSTorr.py script. It will populate a menu with the recent HorribleSubs torrents from nyaa.se and use `transmission-cli` to download them. All downloads will be sorted into folders based off of the name of the show inside of the download directory (defaults to ~/Videos)

## Requirements
* Python
 * BeautifulSoup (bs4)
 * requests
* transmission-cli

## Instructions
The script will default to downloading to your ~/Videos folder. If this doesn't exist, or if you would rather it default to a different directory, after the first comment block is the string variable `myAnimeFolder`. Paste the full path of your desired download directory inbetween the single quotes to change the default download directory.

There are a few weird bugs with transmission-cli that cause some torrents to quit immediately, but after a second or third attempt it will download just fine. I have no idea what's happening, how it's happening, or why it's happening. It seems like clearing out the `resume` and `torrents` folders can help, if they aren't already empty.

Unfortunately, transmission-cli only allows for one download at a time. Considering this menu will likely only be used for currently airing shows, it shouldn't be too painful to just keep an eye out for when they're done.

I might look into other cli torrent packages, but it's pretty low-priority.
