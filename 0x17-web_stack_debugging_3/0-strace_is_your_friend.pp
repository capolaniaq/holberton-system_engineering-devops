# fix 500 server error
exec { 'fix-phpp':
  command  => 'sed -i s/.phpp/.php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path     => 'usr/bin/:/bin/',
}
