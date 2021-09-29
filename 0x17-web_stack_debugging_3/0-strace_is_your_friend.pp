# server error 500
exec { 'fixing-pphp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => 'usr/bin/:/bin/'
}
