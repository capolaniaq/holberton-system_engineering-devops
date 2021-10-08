# change the limits in users
exec { 'hard--soft':
  environment => ['h_old=nofile 5', 'h_new=nofile 30000', 's_old=nofile 4','s_new=nofile 10000','dir=/etc/security/limits.conf'],
  command     => 'sudo sed -i "s/$h_old/$h_new/" $dir; sudo sed -i "s/$s_old/$s_new/" $dir',
  path        => ['/usr/bin', '/bin'],
}