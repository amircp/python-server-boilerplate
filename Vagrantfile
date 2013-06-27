# Generic Server
#
# Options for generic server
#

require_relative "provision/vagrant/plugins/provisioners/fabric/plugin.rb"
require 'json'
@cfg = JSON.parse(File.read('settings.cfg'))

Vagrant.configure("2") do |config|
    config.vm.box = "debian-70"
    config.vm.box_url = "http://static.nls.io/debian-70.box"

    config.vm.guest = :linux
    config.vm.provision :fabric do |fab|
        fab.tasks = [@cfg["enviroments"]["development"]["PROVISIONER_COMMAND"]]
    end
    config.vm.network :private_network, ip: @cfg["enviroments"]["development"]["IP"]
    config.vm.synced_folder "src/", @cfg["enviroments"]["development"]["SRC_MOUNT_DIR"]
    #config.vm.network :forwarded_port, host: 8000, guest: 8000
end
