# Using OpenCV with Docker

## Get Docker

### Delete docker
#sudo apt remove docker docker-engine docker.io containerd runc

### set repository (update apt package index etc.)
#sudo apt update </br>
#sudo apt-get install apt-transport-https ca-certificates curl gnupgagent software-properties-common

### Install Docker
#### official GPG Key
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#### set stable repositiry
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable"
#### install Docker Engine
#sudo apt update </b>
#sudo apt install docker-ce docker-ce-cli containerd.io </b>
#### Check Docker installation
#docker --version
or, # sudo docker run hello-world

### Install Docker Program 권한부여vkd
#### Install compose
#sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/dockercompose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#### authorization
#sudo chmod +x /usr/local/bin/docker-compos </b>
#### Check
#docker-compose --version

### root authorization 
#sudo usermod -aG docker [username ]
### docker build & run
#sudo docker build --tag <image>:<tag> </b>
#sudo docker run -it --name <container> <image>:<tag> </b>
  
### move host file to docker
#sudo docker cp <host file path> <container name> : <docker file path>

    
### docker commit and push
#sudo docker commit -m "Update install" <container> <image>:<tag>
#sudo docker run -it --name <container> <image>:<tag>

