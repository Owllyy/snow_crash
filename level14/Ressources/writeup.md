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

> jump *(main + 63)

and then i displayed the string pointed by the return register eax

> print (char *)($eax)