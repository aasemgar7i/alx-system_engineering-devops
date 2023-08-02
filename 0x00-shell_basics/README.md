(0)"echo $PWD" is print the path name of the current directory.
(1)"echo "$(ls -1)"" Display the content list of your current directory in 1 line.
(2)"cd ~" changes the working directory to /root with command source ./file-name.
(3)"echo "$(ls -l)" Display the content of current directory in long format
(4)"echo "$(ls -la)" Display the content of current directory in long format with hidden files too
(5)"echo "$(ls -lan)" Display the content of current directory in long format with hidden files and with user and group IDs
(6)"mkdir /tmp/my_first_directory" Make directory in /tmp
(7)"mv /tmp/betty /tmp/my_first_directory" Move "betty" file from /tmp/ directory to my_first_directory directory at /tmp/
(8)"rm /tmp/my_first_directory/betty" Remove file "betty" from "my_first_directory" at /tmp
(9)"rm -r /tmp/my_first_directory" Remove "my_first_directory" directory from /tmp
(10)"cd -" This command back to last directory were in
(11)"ls -la .. . /boot" List all file in current directory and in parent of working one and in /boot directory
(12)"file /tmp/iamafile" It show the file type of file "iamafile" at /tmp
(13)"ln -s /bin/ls __ls__" Make a shortcut to /bin/ls by making symbolic link named __ls__
(14)"cp -u *.html ../" Copy all new html file in current directory to parent directory
(15)"mv [[:upper:]]* /tmp/u" Move Files starting with uppercase to /tmp/u directory
(16)"rm -f *~" Delete cash file of Emacs
(17)"mkdir -p welcome/to/school/" Make directory with -p recursively
(18)"ls -vamp" Nice tool 