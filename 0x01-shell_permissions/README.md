________________Shell Permission___________
11;rgb:0000/0000/0000(0)"su betty" Change current user to betty user by super user command
(1)"whosmi" Show the current user
(2)"groups" show groupe for current user
(3)"chown betty hello" Change the owner of the file hello to user betty
(4)"touch hello" Create the file hello
(5)"chmod u+x hello" add execute premission to file hello
(6)"chmod u+x,g+x,o+r hello" adds execute permission to the owner and the group owner, and read permission to other users
(7)"chmod a+x hello" adds execution permission to the owner, the group owner and the other users, to the file hello
(8)"chmod 007 hello" Make permissin for other users only
(9)"chmod 753 hello" Give Read Write Execute permission to Owner and Read Execute to Group and Write Execute to Others
(10)"chmod 664" adds execute permission to all subdirectories of the current directory
(11)"mkdir -m 751 my_dir"creates a directory called my_dir with permissions 751
(12