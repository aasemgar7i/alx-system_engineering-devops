___________Shell, I/O Redirections and filters_______

(1)"echo "Hello, World" Print what inside "" to termnal output
(2)"echo "\"(Ôo)'"" print special char 
(3)"cat /etc/passwd /etc/hosts" show files in this two dirs
(4)"tail /etc/passwd" show last 10 lines of file
(5)"head /etc/passwd" show first 10 lines of file
(6)"head -n 3 iacta | tail -n 1"  displays only the third line of the file 
(7)"echo" and put \ before every special characters
(8)"tail -n 1 iacta >> iacta" duplicate the last line
(9)"find . -type f -name "*.js" -delete" find and delete all .js files
(10)"find . -type d -not -name "." | wc -l" counts the number of directories and sub-directories
(11)"ls -t1 | head -n 10" displays the 10 newest files 
(12)"sort | uniq -u" prints only words that appear exactly once.
(13)"grep -i "root" /etc/passwd" Display lines containing the pattern “root” from the file
(14)"grep -i "bin" /etc/passwd | wc -l" Display the number of lines that contain the pattern “bin” in the file 
(15)"grep -i -A 3 "root" /etc/passwd" Display lines containing the pattern “root” and 3 lines after them in the file 
(16)"grep -i -v "bin" /etc/passwd" Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
(17)"grep -i "^[a-z]" /etc/ssh/sshd_config" Display all lines of the file /etc/ssh/sshd_config starting with a letter.
(18)"tr "A" "Z" | tr "c" "e"" Replace all characters A and c from input to Z and e respectively.
(19)"tr -d "cC" removes all letters c and C from input.
(20)"rev" reverse th result
(21)"cut -d ":" -f1,6 /etc/passwd | sort" displays all users and their home directories, sorted by users.
(22)"find . -empty | rev | cut -d '/' -f 1 | rev" finds all empty files and directories in the current directory and all sub-directories
(23)"find -type f -name "*.gif" | rev | cut -d "/" -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f" lists all the files with a .gif extension 
(24)"cut -c 1 | paste -s -d ''" Acrostic
(25)"tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev" The biggest fan
