# 0x08. Networking basics #1

_Foundations > System engineering & DevOps > Networking_

By Sylvain Kalache, co-founder at Holberton School

Author [Carlos Andres Polania](https://twitter.com/timberdev)

## Learning Objectives
-   What is localhost/127.0.0.1
-   What is 0.0.0.0
-   What is  `/etc/hosts`
-   How to display your machine’s active network interfaces

## Tasks
### 0. Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

-   `localhost`  resolves to  `127.0.0.2`
-   `facebook.com`  resolves to  `8.8.8.8`.
-   The checker is running on Docker, so make sure to read  [this](https://intranet.hbtn.io/rltoken/8PP1z09aHTqgTjyvET6-hg "this")

### 1. Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

### 2. Port listening on localhost
Write a Bash script that listens on port `98` on `localhost`.