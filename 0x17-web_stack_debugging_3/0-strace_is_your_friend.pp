# server error 500
exec { 'fixing-pphp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/bin/:/bin/'
}
