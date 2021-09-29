# fix 500 server error
exec { 'fix-phpp':
  command  => "sed -i -e 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path     => 'usr/bin/:/bin/'
}
