At the home directory there is a token file and a program :

the content of token is readable by this user : f4kmm6p|=�p�n��DB�Du{��
It does not correspond to the pass of flag09 and seems to be alterated because of the non displayable character.

The program is taking a string and is displaying the result on the standard output :

	> ./level09 aaaaaa
	> abcdef

It's easy to see the modification and it dosn't need further investigation.
It simply, for each character fo the string, add the index of the character to the value of this character.

This program is enough to decode the token :

```c
#include <unistd.h>
int main(int ac, char **av) {
	int c;
	int i = 0;

	for (av[1][i]; i++) {
		c = av[1][i] - i;
		write(1, &c, 1);
	}
}
```
