# fix 500 server error
exec { 'wordpress error':
  command => 'sed -i 's/phpp/php/' /var/www/html/wp-settings.ph',
  path    => /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
