#!/bin/bash

"""
  Esse arquivo faz a instalação
  de forma automática em sistemas
  Debian 8.x/Ubuntu 16.x 

  Modificado em 17 de novembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Atualizando seus repositórios
export DEBIAN_FRONTEND="noninteractive"
sudo apt-get update

# Remover Docker instalado anteriormente
sudo apt-get purge lxc-docker*
sudo apt-get purge docker.io*

# Add Docker repo
sudo apt-get install -y apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

cat > /etc/apt/sources.list.d/docker.list <<'EOF'
deb https://apt.dockerproject.org/repo debian-jessie main
EOF
sudo apt-get update

# Instalando o Docker
sudo apt-get install -y docker-engine
sudo service docker start
sudo docker run hello-world

# Configurando as permissões do grupo de usuários do Docker
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart

# Definir o Docker para auto-startup na inicialização
sudo systemctl enable docker
