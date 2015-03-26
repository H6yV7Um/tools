sudo useradd -s /bin/bash -m -p $(openssl passwd -1 "123") $1
sudo gpasswd -a $1 docker
