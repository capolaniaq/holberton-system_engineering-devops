#kill the killmenow

exec {
  command => 'pkill -f killmenow'
  path => '/bin/',
}
