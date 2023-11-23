At the home directory there is nothing.
No file was created by user or group "level14" or "flag14"

After a lot of try i used gihdra to decompile the command getflag itself:

ive found that the command is using ft_des and a string literal to show the flag.
Im searching the flag for the last flagXX user so i tried to directly jump at the last ft_des()
and skip all verification

...

else {
  if (_Var5 != 0xbc6) goto LAB_08048e06;
  pcVar7 = ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|");
  fputs(pcVar7,pFVar8);
}

...

I will use the same method as the exercise 13
At first i step in some intial instruction to let the memory being set.
I stop before the instruction wich is calling ptrace
And then jump to the code above, skiping the verification.

This part in gdb is located at *(main + 1183)

> jump *(main + 1883)

and then the program display the password :

  7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ