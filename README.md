### Boilerplate for python web development servers with debian 7.0 ###
##### Provisioning with fabric/cuisine on remote hosts and vagrant boxes #####


#### Requeriments ####

- Vagrant 

Download vagrant: http://www.vagrantup.com/

- Cuisine

Install cuisine:

	sudo pip install cuisine


#### How to use ####

##### Setup provisioning #####

- Add or edit cuisine/fabric scripts in __provision/recipes__ and edit __provision/\_\_init\_\_.py__ for call recipes (see source code).
- Add or edit config files in __provision/config__.
- Edit __Vagrantfile__.
    - You can add or change the command to execute for provisioning in __fab.tasks = ["configure_host"]__.
    - You can change the vbox ip in __config.vm.network :private_network, ip: "192.168.50.4"__vagrant.
    - You can comment/uncomment others options.

##### Run vagrant #####

- Run __vagrant up__ for exec configure_host command in vagrant box.
- Run __vagrant ssh__ for enter in to vagrant box.

##### Setup for remote hosts #####

- Edit __fabfile.py__ and add remote ip addresses for server enviroments.

##### Commands for remote hosts #####

- Run __fab <enviroment> configure_host__ for provisioning in a remote host.
- Run __fab <enviroment> update_host__ for update packages database in a remote host.
- Run __fab <enviroment> upgrade_host__ for upgrade packages in a remote host.
- Run __fab__ for see all commands.

- You can use the remote host commands using an ip for the vagrant box(See Vagrantfile and fabfile.py).

##### Create new commands for remote hosts #####

- You can add more functions for deploy or remote tasks in __fabfile.py__.

##### Test your app in vagrant #####

- You can put your source code in __src__, vagrant mount it in __/home/vagrant/app__.
- You must create a recipe for config your app.


#### Include recipes ####

- Setup (Edit this recipe for change the default user)
    - Install VIM
    - Install nano
    - Install tmux
    - Install some util libs
    - Create default user
    - Config sudo
    - Config tmux for default user and vagrant user

- Python
    - Install python and python development files
    - Install pip
    - Install virtualenvs
    - Config virtualenvwrapper for vagrant
    
- Nginx
    - Install nginx

- Uwsgi
    - Install Uwsgi

- Postgres
    - Install postgres
    - Create user (Only for remote hosts)    
    - Create database (Only for remote hosts)

- GIT 
    - Install GIT
    - Install gitolite
    - Create user for git
    - Config gitolite (Only for remote hosts)
    
