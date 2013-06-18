# Generic Server
#
# Options for generic server
#

require_relative "provisioning/vagrant/plugins/provisioners/fabric/plugin.rb"

Vagrant.configure("2") do |config|
  config.vm.box = 'precise32'
  config.vm.box_url = 'http://files.vagrantup.com/precise32.box'
  config.vm.guest = :linux
  #config.vm.synced_folder "src/", "/home/apps/www"
  config.vm.provision :fabric do |fab|
    fab.tasks = ["configure_host:devel=True"]
  end
end
