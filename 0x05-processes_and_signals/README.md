# 0x05. Processes and signals

_Foundations > System engineering & DevOps > Bash_
By Sylvain Kalache, co-founder at Holberton School
Author  [Carlos Andres Polania](https://twitter.com/timberdev) (capolaniaq@correo.udistrital.edu.co)

## Learning Objectives
-   What is a PID
-   What is a process
-   How to find a process’ PID
-   How to kill a process
-   What is a signal
-   What are the 2 signals that cannot be ignored

## Tasks
### 0. What is my PID
Write a Bash script that displays its own PID.

### 1. List your processes
Write a Bash script that displays a list of currently running processes.

Requirements:

-   Must show all processes, for all users, including those which might not have a TTY
-   Display in a user-oriented format
-   Show process hierarchy

### 2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

### 3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

### 4. To infinity and beyond
Write a Bash script that displays `To infinity and beyond` indefinitely.

### 5. Don't stop me now!
We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this

### 6. Stop me if you can
Write a Bash script that stops `4-to_infinity_and_beyond` process.
### 7. Highlander
Write a Bash script that displays:

-   `To infinity and beyond`  indefinitely
-   With a  `sleep 2`  in between each iteration
-   `I am invincible!!!`  when receiving a  `SIGTERM`  signal

### 8. Beheaded process

Write a Bash script that kills the process `7-highlander`.

