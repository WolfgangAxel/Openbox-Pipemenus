# SteamPipe
A pipe menu to handle directly launching a Steam game or just opening Steam. Optional `SteamFriendsPipe` will also check which friends are online and allow you to log in and open the message window. Both require Python3

## Requirements
* Steam
* BS4 (`SteamFriendsPipe` only)

## Instructions
If you have Steam games installed in a directory other than `~/.steam/steam/steamapps`, underneath the first block of comments is the array STEAMAPPS. Add all directories as outlined in the example in the comment, and they will be added to the search.

If you are using `SteamFriendsPipe`, you will need to add your Steam ID to the script. Check the file for detailed instructions.
