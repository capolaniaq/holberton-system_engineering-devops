# 0x10. HTTPS SSL
By Sylvain Kalache, co-founder at Holberton School

Author Carlos Andres Polania (capolaniaq@correo.udistrital.edu.co)

## Learning Objectives

-   What is HTTPS SSL 2 main roles
-   What is the purpose encrypting traffic
-   What SSL termination means
## Tasks
### 0. World wide web
Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

### 1. HAproxy SSL termination

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.