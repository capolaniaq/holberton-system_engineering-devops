# 0x0C. Web server

_Foundations > System engineering & DevOps > Web stack_

By Sylvain Kalache, co-founder at Holberton School


## Learning Objectives

### General

-   What is the main role of a web server
-   What is a child process
-   Why web servers usually have a parent process and child processes
-   What are the main HTTP requests

### DNS

-   What DNS stands for
-   What is DNS main role

### DNS Record Types

-   `A`
-   `CNAME`
-   `TXT`
-   `MX`

## Tasks

### 0. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server:

### 1. Install nginx web server

Web servers are the piece of software generating and serving HTML pages, let’s install one!

### 2. Setup a domain name

[.TECH Domains](https://intranet.hbtn.io/rltoken/yRrwiHrS15iQQZku72p0aQ ".TECH Domains")  is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your  [tools space](https://intranet.hbtn.io/rltoken/b-Y81kiPBFJ_6wxJaSmBgQ "tools space"). Feel free to drop a thank you tweet for  [.TECH Domains](https://intranet.hbtn.io/rltoken/d9XjYlM-CqTRHJEcaKpcVQ ".TECH Domains").

Provide the domain name in your answer file.

### 3. Redirection

Readme:

-   [Replace a line with multiple lines with sed](https://intranet.hbtn.io/rltoken/Afg1zCifjmIygL1se0ghhg "Replace a line with multiple lines with sed")

Configure your Nginx server so that  `/redirect_me`  is redirecting to another page.


### 4. Not found page 404

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.