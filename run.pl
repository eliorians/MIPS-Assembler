#!/usr/bin/perl

#This script runs on student.  If you run it on cs, you'll need
#to change the path to perl above.

@canfiles = ( "addArray",  "arrayCopy", "decrement",  "iterate", "iterate2", "loop10times", 
              "negbranch",  "arrayCopy",  "fibo",   "loadsFPAddsStores",   "multiply",
              "branch1",    "fiboLoop",           "loadsFPDivsStores",   "powers",
              "branch2",    "loadsDaddiStores",   "loadsFPMultsStores",  "vectorDiv",
              "daddiu",     "loadsDaddiuStores",  "loadsStores1",       "vectorSub",
              "dump",       "loadsDaddsStores",   "loadsStores2",
              "factorial",  "loadsDsubsStores",   "matrixMult");


$candir = "/u/css/classes/5483/111/MA/";

$dir = "Tests/";

if (! -e $dir)
{
   print "need to create a Tests directory first\n";
   exit();
}
system "rm -f Tests/*";                                                                                

$pass = 0;

for ($i = 0; $i <= $#canfiles; $i++){
   $prefix = $canfiles[$i];
   $input = $prefix.".asm";
   $output = $prefix.".hex";
   $caninput = $candir.$prefix.".asm";
   $canoutput = $candir.$prefix.".hex";
   system "cp $caninput .";
   print "Testing $input. ";

#  change the command in quotes below if the name of your executable isn't ma
#  For example, "java Assembler $input"
   system "ma $input";

   #print "Comparing $output and $canoutput\n";
   system "/u/css/classes/5483/111/MA/mydiff $output $canoutput 8 > $prefix.problems";
   if (system "test -s $output") {
         #didn't create an output file
         print " Failed.\n";
   } elsif (! system "test -s $prefix.problems"){
         #print "problems found in $output, keeping all temp files.\n";
         print " Failed.\n";
         system "mv $input Tests/";
         system "mv $output Tests/";
         system "mv $prefix.problems Tests/";
   } else {
         #print "No problems found removing all temp files.\n";
         system "rm -rf $output $input $prefix.problems";
         print " Passed.\n";
         $pass = $pass + 1;
   }
}

$total = $#canfiles + 1;
print "\n$pass out of $total passed.\n";
if ($pass != $total) {
   print "See Tests directory for failed tests\n";
}


