-----------Shell Variables---------
(1)"alias ls="rm *"" Creates an alias
(2)"echo "hello $USER" Prints `hello user`, where user is the current Linux user
(3)"export PATH=$PATH:/action" last directory the shell looks into when looking for a program 
(4)"echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1))" counts the number of directories in the PATH
(5)"printenv"  lists environment variables.
(6)"set" lists all local variables and environment variables, and functions.
(7)"BEST="School"" creates a new local variable.
(8)"export BEST="School"" creates a new global variable.
(9)"echo $(($TRUEKNOWLEDGE + 128))" prints the result of the addition of 128 with the value stored in the environment variable
(10)"echo $(($POWER / $DIVIDE))" prints the result of POWER divided by DIVIDE
(11)"echo $((BREATH**$LOVE))" displays the result of BREATH to the power LOVE
(12)"echo $((2#$BINARY))" converts a number from base 2 to base 10.
(13)"echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"" prints all possible combinations of two letters, except oo.
(14)"printf "%.2f" $NUM | sort" prints a number with two decimal places
(15)"printf '%x\n' $DECIMAL" converts a number from base 10 to base 16.
(16)"tr 'A-Za-z' 'N-ZA-Mn-za-m'" encodes and decodes text using the rot13 encryption
(17)"perl -lne 'print if $. % 2 ==1'" prints every other line from the input,
(18)"echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')"  adds the two numbers stored in the environment variables WATER and STIR and prints the result.
