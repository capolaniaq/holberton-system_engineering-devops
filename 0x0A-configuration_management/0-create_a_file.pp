# create file holberton in a folder tmp, with these requeriments above

$str = 'I love Puppet'

file {'holberton':
  path => '/tmp/holberton',
  mode => '0744',
  owner => 'www-data',
  group => 'www-data',
  content => $str,
}
