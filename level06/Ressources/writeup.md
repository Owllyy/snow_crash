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


