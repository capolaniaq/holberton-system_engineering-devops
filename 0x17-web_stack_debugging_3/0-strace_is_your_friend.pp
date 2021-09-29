# fix 500 server error
exec { 'fixing-wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => 'usr/bin/:/bin/',
}
