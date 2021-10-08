# server error 500
exec { 'limit higher':
  environment => ['old=ULIMIT="-n 15"', 'new=ULIMIT="-n 65535"'],
  command     => 'sed -i s/old/new/g /etc/default/nginx; sudo service nginx restart',
  path        => 'usr/bin/:/bin/',
  returns     => [0, 1]
}