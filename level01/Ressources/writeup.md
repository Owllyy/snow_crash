By checking the file /etc/passwd i found something interesting.

In this file you can find every user and some information about them :
username:password:user_id:group_id:user_id_info:home_dir:command_shell

In the case of user flag01, the crypted password is visible in this file:
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash -> 42hDRfypTqqnw

For the others, the crypted password is marked as "x" and located to the innaccessible file /etc/shadow
flag02:x:3002:3002::/home/flag/flag02:/bin/bash

The password is encrypted using the encryption of the system "crypt" (SHA-256 or SHA-512 since glibc 2.7)

I used JohnTheRipper to decrypt the password find in the file :
    echo "42hDRfypTqqnw" > pass && john pass

It give us abcdefg and im able to connect to user flag01