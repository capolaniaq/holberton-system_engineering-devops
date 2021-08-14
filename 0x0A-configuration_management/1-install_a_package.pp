#file to install puppet-lint

exec {'puppet-lint':
  command => 'sudo gem install puppet-lint -v 2.1.1',
  path    => '/usr/local/bin/:/bin/',
}
