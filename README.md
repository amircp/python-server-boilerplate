### Boilerplate for python web development servers ###
##### Provisioning with fabric/cuisine on remote hosts and vagrant boxes #####


#### Requeriments ####

- Vagrant 

Download vagrant: http://www.vagrantup.com/

- Cuisine

Install cuisine:

	sudo pip install cuisine


#### How to use ####

- Add or edit cuisine/fabric scripts in __provision/recipes__ and edit __provision/\_\_init\_\_.py__ for call recipes (see source code).
- Edit __Vagrantfile__.
- Run __vagrant up__ for testing in vagrant.
- Edit __fabfile.py__ and add remote ip addresses for server enviroments.
- Run __fab <enviroment> configure_host__ for provisioning in a remote host.
- You can add more functions for deploy or remote tasks in __fabfile.py__.

#### Include recipes ####

- Setup (Edit recipe to change the default user)
    - Install VIM
    - Install nano
    - Install tmux
    - Install some util libs
    - Create login user
    - Config sudo
    - Config tmux for login user

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

- GIT 
    - Install GIT
    - Install gitolite
    - Create user for git
