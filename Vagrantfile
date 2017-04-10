# -*- mode: ruby -*-
# vi: set ft=ruby :

remi = ["php56", "php70", "php71"]

composer = <<-SHELL
  EXPECTED_SIGNATURE=$(curl https://composer.github.io/installer.sig)
  php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
  ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');")

  if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]
  then
    >&2 echo 'ERROR: Invalid installer signature'
    rm composer-setup.php
    exit 1
  fi

  php composer-setup.php --quiet
  rm composer-setup.php
  mv composer.phar /usr/bin/composer
SHELL

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: <<-SHELL
    if ! yum info remi-release
    then
      curl -O http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
      yum -y install ./remi-release-7.rpm
    fi
  SHELL

  remi.each do |repo|
    config.vm.define "#{repo}" do |i|
      i.vm.provision "shell", inline: <<-SHELL
        yum-config-manager --enable remi-#{repo}
        yum -y install php php-xml php-mbstring php-pecl-zip
        if ! composer
        then
          #{composer}
        fi
      SHELL
    end
  end
end
