# 0x14. MySQL

By Sylvain Kalache, co-founder at Holberton School

Author Carlos Andres Polania (capolaniaq@correo.udistrital.edu.co)

### General

-   What is the main role of a database
-   What is a database replica
-   What is the purpose of a database replica
-   Why database backups need to be stored in different physical locations
-   What operation should you regularly perform to make sure that your database backup strategy actually works


## Tasks

### 0. Install MySQL

First things first, let’s get MySQL installed on **both** your web-01 and web-02 servers.

### 1. Let us in!

In order for us to verify that your servers are properly configured, we need you to create a user and password for **both** MySQL databases which will allow the checker access to them.


### 2. If only you could see what I've seen with your eyes


In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

### 3. Quite an experience to live in fear, isn't it?

Before you get started with your primary-replica synchronization, you need one more thing in place. On your **primary** MySQL server (web-01), create a new user for the replica server.

### 4. Setup a Primary-Replica infrastructure using MySQL

Having a replica member on for your MySQL database has 2 advantages:

-   Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
-   Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed


### 5. MySQL backup

Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.