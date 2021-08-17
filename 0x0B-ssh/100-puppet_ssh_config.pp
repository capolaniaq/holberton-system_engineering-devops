# create file holberton in a folder tmp, with these requeriments above

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}