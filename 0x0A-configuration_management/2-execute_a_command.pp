#kill the killmenow

exec { 'killmenow':
  command  => '/usr/bin/pkill -f killmenow',
  provider => 'shell',
}
