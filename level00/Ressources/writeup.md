I started by searching information about the user flag00.
I used the command find with the option -user to find file created by flag00. (find / -user "flag00" -print 2>/dev/null)

I found the file /usr/sbin/john wich contain "cdiiddwpgswtgt"

The string was not enough to connect as user flag00, so i tried to decrypt it with the simplest crypting algorithm Rot13.
I found an easy version at https://www.dcode.fr/caesar-cipher that is trying every shift from 0 to 25.

The 11th shift give the string "nottoohardhere" 

It was enough to connect as flag00.