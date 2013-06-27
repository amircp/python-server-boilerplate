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

- Add or edit cuisine/fabric scripts in __provision/recipes__.
- Add or edit config files in __provision/config__.
- The main provisioning function is __setup_hosts__ in __fabfile.py__, you can edit this function or add more.
- You can add more enviroments in __provision/enviroments.py__.
- Edit __settings.json__ for add staging or production hosts/private_keys. Also you can edit options for vagrant or add new options for your commands.
- The development enviroment is only for vagrant.
- Example of the __settings.cfg__:

        {
            "enviroments": {
                "development": {
                        "IP" : "192.168.13.37",
                        "USERNAME" : "vagrant",
                        "VAGRANT_PRIVATE_KEY_PATH": "/Users/alvarolizama/.vagrant.d/insecure_private_key",
                        "PROVISIONER_COMMAND" : "setup_host",
                        "SRC_MOUNT_DIR" : "/home/vagrant/src"
                },
                "staging": {
                        "USERNAME": "",
                        "HOSTS" : [
                        ],
                        "PRIVATE_KEY_PATH" : ""
                },
                "production": {
                        "USERNAME": "root",            
                        "HOSTS" : [
                            "192.168.13.37:22"
                        ],
                        "PRIVATE_KEY_PATH" : "/Users/alvarolizama/.ssh/work.pem"
                }
            }
        }

##### Run vagrant #####

- If you need port redirect for vagrant edit the __Vagrantfile__.
- Run __vagrant up__ for exec setup_host command in vagrant box.
- Run __vagrant ssh__ for enter in to vagrant box.

##### Run other commands in enviroments #####

- For run a command of the __fabfile.py__ in vagrant just type __fab development <command>__.
- For run a command of the __fabfile.py__ in staging just type __fab staging <command>__.
- For run a command of the __fabfile.py__ in production just type __fab production <command>__.

##### Test your app in vagrant #####

- Put your source code in __src__, vagrant mount it in __/home/vagrant/src__.


#### Include recipes ####

- Setup (Edit this recipe for change the default user)
    - Install VIM
    - Install nano
    - Install tmux
    - Install some util libs
    - Config tmux for vagrant user

- Python
    - Install python and python development files
    - Install pip
    - Install virtualenvs
    
- Nginx
    - Install nginx
    - Create user for apps
    - Create dir for apps and logs

- Uwsgi
    - Install Uwsgi

- Postgres
    - Install postgres
    - Create user    
    - Create database
    - Grant permissions 

- Gitolite 
    - Install gitolite
    - Create user for git
    - Config gitolite 
    
