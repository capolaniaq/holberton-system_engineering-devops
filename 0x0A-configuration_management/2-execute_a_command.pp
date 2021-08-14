#kill the killmenow

exec {
  command => '/usr/bin/pkill -f killmenow'
  provider => 'shell',
}
