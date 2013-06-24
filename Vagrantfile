# Generic Server
#
# Options for generic server
#

require_relative "provision/vagrant/plugins/provisioners/fabric/plugin.rb"

Vagrant.configure("2") do |config|
    config.vm.box = "debian-70"
    config.vm.box_url = "http://static.nls.io/debian-70.box"

    config.vm.guest = :linux
    config.vm.provision :fabric do |fab|
        fab.tasks = ["configure_host"]
    end

    ##
    ## Comment/Uncomment options 
    ##
  
    #config.vm.network :forwarded_port, host: 8000, guest: 8000
    config.vm.network :private_network, ip: "192.168.50.1"
    #config.vm.synced_folder "src/", "/home/vagrant/app"
end
