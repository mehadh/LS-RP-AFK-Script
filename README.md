# LS-RP-AFK-Script
This is a simple Python script that allows for players to avoid detection while AFKing on LS-RP.

Created sometime in 2019(?), this script follows the following process:
1. Do the command /admins in game. This should list the names of the administrators online, or, if none are online, it should print "There's no administrators online."
2. Copy the SA-MP Chatlog.txt to a new file (to avoid any issues with reading/writing)
3. Parse this chatlog for the last line.
4. If the last line is not "There's no administrator's online", check again, and if it still isn't that, then quit the game.
5. If the last line IS "There's no administrator's online", it's safe to AFK, and thus, the bot moves around a little and types /time before then sleeping for another 20 minutes.

Using this script, I have never been banned from LS-RP for AFK botting. By quitting when administrators are online, you evade their attention.
I intended to expand on this to auto re-join when admins leave and such, but I've lost interest in LS-RP, so unfortunately I have not updated the script to that point.
