# create file holberton in a folder tmp, with these requeriments above


file {'holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
