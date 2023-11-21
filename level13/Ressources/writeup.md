At the home directory there is a binary file.

I used gihdra to decompile it and understand it easily :

int main(int argc, const char **argv, const char **envp)
{
  __uid_t v3; // eax
  char *v4; // eax

  if ( getuid() != 4242 )
  {
    v3 = getuid();
    printf("UID %d started us but we we expect %d\n", v3, 4242);
    exit(1);
  }
  v4 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
  return printf("your token is %s\n", v4);
}

The program is verifying the uid of the user and then it encode and display the flag.
I used gdb to jump directly to the encoding part and skip the identification.

> jump *(main + 63)

and then i displayed the string pointed by the return register eax

> print (char *)($eax)