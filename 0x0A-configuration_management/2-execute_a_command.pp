#kill the killmenow

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  path => '/bin/',
}
