# !/bin/bash -e
#install fish shell and oh-my-fish framework
sudo apt install fish -y
curl -L https://get.oh-my.fish | fish
omf install bobthefish
chsh -s /usr/bin/fish
echo "exec fish" >> ~/.bashrc