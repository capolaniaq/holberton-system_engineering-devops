# 0x0A. Configuration management

_Foundations > System engineering & DevOps > CI/CD_

By Sylvain Kalache, co-founder at Holberton School


Author [Carlos Polania](https://twitter.com/timberdev) (capolaniaq@correo.udistrital.edu.co)

## Tasks
Using Puppet, create a file in  `/tmp`.

Requirements:

-   File path is  `/tmp/holberton`
-   File permission is  `0744`
-   File owner is  `www-data`
-   File group is  `www-data`
-   File contains  `I love Puppet`

### 1. Install a package
Using Puppet, install  `puppet-lint`.

Requirements:

-   Install  `puppet-lint`
-   Version must be  `2.1.1`

### 2. Execute a command
Using Puppet, create a manifest that kills a process named  `killmenow`.

Requirements:

-   Must use the  `exec`  Puppet resource
-   Must use  `pkill`

Example:

Terminal #0 - starting my process


