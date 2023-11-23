In the home directory, there is nothing. No file was created by the user or group 'level14' or 'flag14.'

After numerous attempts, I used Ghidra to decompile the command 'getflag' itself:

I found that the command is using 'ft_des' and a string literal to show the flag. I am searching for the flag for the last 'flagXX' user, so I tried to directly jump to the last 'ft_des()' and skip all verifications.

```c
...
else {
  if (_Var5 != 0xbc6) goto LAB_08048e06;
  pcVar7 = ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|");
  fputs(pcVar7,pFVar8);
}
...
```

I will use the same method as in exercise 13. At first, I step in some initial instructions to let the memory be set. I stop before the instruction that is calling 'ptrace' and then jump to the code above, skipping the verification.

This part in GDB is located at *(main + 1183):

```bash
> jump *(main + 1183)
```

And then the program displays the password:

```
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```

This allows me to obtain the flag without going through the usual verification process.