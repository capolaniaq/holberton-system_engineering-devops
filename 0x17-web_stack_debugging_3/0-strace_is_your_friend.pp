# fix 500 server error
exec { 'fix-phpp':
  command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php',
  path     => ['/bin', '/usr/bin', '/usr/sbin']
}
# wordpress apache2 running again
exec { 'fixing-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}