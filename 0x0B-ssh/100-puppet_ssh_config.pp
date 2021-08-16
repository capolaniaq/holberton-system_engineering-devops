# create file holberton in a folder tmp, with these requeriments above

file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 35.185.27.173
     User root
     IdentityFile ~/.ssh/holberton',
  mode    => '7000',
}