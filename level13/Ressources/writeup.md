In the home directory, there is a binary file.

I used Ghidra to decompile it and understand it easily:

```c
int main(int argc, const char **argv, const char **envp)
{
  __uid_t v3; // eax
  char *v4; // eax

  if (getuid() != 4242)
  {
    v3 = getuid();
    printf("UID %d started us but we expect %d\n", v3, 4242);
    exit(1);
  }
  v4 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
  return printf("your token is %s\n", v4);
}
```

The program verifies the UID of the user and then encodes and displays the flag.

You used GDB to jump directly to the encoding part and skip the identification.

You let the memory be initialized:

```bash
> si
> si
```

And then jumped:

```bash
> jump *(main + 63)
```

Finally, you displayed the string pointed to by the return register EAX:

```bash
> print (char *)($eax)
```

This allowed you to retrieve the encoded flag without going through the UID verification process.