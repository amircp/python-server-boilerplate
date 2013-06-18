# Boilerplate for base servers #
##### Provisioning with fabric/cuisine on remote hosts and vagrant boxes #####

#### Requeriments ####

- Vagrant 

Download vagrant: http://www.vagrantup.com/

- Cuisine

Install cuisine:

	sudo pip install cuisine


#### How to use ####

- Add cuisine/fabric scripts  in __provisioning/recipes__ and edit __provisioning/\_\_init\_\_.py__ for call scripts.
- Edit __Vagrantfile__.
- Run __vagrant up__ for testing in vagrant
- Edit __fabfile.py__.
- Run __fab <enviroment> configure_host__ for provisioning or deploy in a remote host

