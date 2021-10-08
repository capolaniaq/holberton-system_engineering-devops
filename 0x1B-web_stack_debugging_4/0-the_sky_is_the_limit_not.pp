# Modified number of request at momment
exec { 'fix--default-nginx':
  environment => ['old=ULIMIT="-n 15"','new=ULIMIT="-n 65535"'],
  command     => 'sudo sed -i "s/$old/$new/" /etc/default/nginx; sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}