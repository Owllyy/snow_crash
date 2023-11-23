```c
int main(int argc, const char **argv, const char **envp)
{
  int *v3; // eax
  char *v4; // eax
  const char *v6; // [esp+28h] [ebp-1028h]
  const char *v7; // [esp+2Ch] [ebp-1024h]
  int v8; // [esp+30h] [ebp-1020h]
  int v9; // [esp+34h] [ebp-101Ch]
  size_t v10; // [esp+38h] [ebp-1018h]
  char buf[4096]; // [esp+3Ch] [ebp-1014h] BYREF
  struct sockaddr addr; // [esp+103Ch] [ebp-14h] BYREF
  unsigned int v13; // [esp+104Ch] [ebp-4h]

  v13 = __readgsdword(0x14u);
  if ( argc <= 2 )
  {
    printf("%s file host\n\tsends file to host if you have access to it\n", *argv);
    exit(1);
  }
  v6 = argv[1];
  v7 = argv[2];
  if ( access(v6, 4) )
    return printf("You don't have access to %s\n", v6);
  printf("Connecting to %s:6969 .. ", v7);
  fflush(stdout);
  v8 = socket(2, 1, 0);
  *(_DWORD *)&addr.sa_data[6] = 0;
  *(_DWORD *)&addr.sa_data[10] = 0;
  addr.sa_family = 2;
  *(_DWORD *)&addr.sa_data[2] = inet_addr(v7);
  *(_WORD *)addr.sa_data = htons(0x1B39u);
  if ( connect(v8, &addr, 0x10u) == -1 )
  {
    printf("Unable to connect to host %s\n", v7);
    exit(1);
  }
  if ( write(v8, ".*( )*.\n", 8u) == -1 )
  {
    printf("Unable to write banner to host %s\n", v7);
    exit(1);
  }
  printf("Connected!\nSending file .. ");
  fflush(stdout);
  v9 = open(v6, 0);
  if ( v9 == -1 )
  {
    puts("Damn. Unable to open file");
    exit(1);
  }
  v10 = read(v9, buf, 0x1000u);
  if ( v10 == -1 )
  {
    v3 = __errno_location();
    v4 = strerror(*v3);
    printf("Unable to read from file: %s\n", v4);
    exit(1);
  }
  write(v8, buf, v10);
  return puts("wrote file!");
}
```