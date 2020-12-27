# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vm.box_check_update = false

  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 443, host: 8443, host_ip: "127.0.0.1"

  config.vm.define "devops1"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    # Installing packages
    apt-get update
    apt-get install -y apache2 certbot python-certbot-apache\
    libapache2-mod-wsgi-py3 python3 python3-pip

    # Getting python ready-to-work
    pip3 install flask
    chown -R www-data:www-data /vagrant/python

    # Updating configuration
    rm -rf /etc/apache2/sites-available
    rm -rf /etc/apache2/sites-enabled
    mkdir -p /etc/apache2/sites-enabled
    cp -r /vagrant/config/apache /etc/apache2/sites-available
    a2ensite simple-site.conf wsgi-site.conf
    systemctl restart apache2

    # Getting certificates, adding SSL and redirects from HTTP to HTTPS
    # It will not work because the following:
    # 1. This command has an interactive interface, use this command inside VB
    # 2. Sites on this container are in .local domain, I can't try it on real.
    #     But if you want, change domains in config/apache/simple-site.conf and
    #     config/apache/wsgi-site.conf files to someone with valid public
    #     suffix and start the following command
    # certbot --apache
  SHELL

end
