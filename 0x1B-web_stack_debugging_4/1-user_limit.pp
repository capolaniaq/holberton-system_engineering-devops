# change the limits in users
exec { 'hard--soft':
  environment => ['hard_old=nofile 5',
  				'hard_new=nofile 30000',
				'soft_old=nofile 4',
				'soft_new=nofile 10000'],
  command     => 'sudo sed -i "s/$hard_old/$hard_new/" /etc/security/limits.conf; sudo sed -i "s/$soft_old/$soft_new/" /etc/security/limits.conf',
  path        => ['/usr/bin', '/bin'],
}