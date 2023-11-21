At the home of user level03 there is a executable file.

I used gihdra to disasamble it, and found that it use geteuid() and seteuid() and then call system().
It's uid is flag03 so i can have the uid of flag03 for the command gived to system()

Inside the system call there is "/usr/bin/env echo Exploit me"

The trick is to add another directory to the path, so i can write my own program "echo".

I added /tmp: to the Environement variable PATH.
And i created this program at /tmp/echo :

#!/bin/sh
getflag

After executing the program level03 it gave me the flag
