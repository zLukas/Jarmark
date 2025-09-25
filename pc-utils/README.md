# pc-utils
useful hacks for Mac/Lunix/Windows development

## Kill docker desktop(MacOS/Linux)
`$ kill $(ps aux | grep docker | awk '{print $2}')` (MacOs)  
` $ kill -9 $(ps aux | grep docker | awk '{print $2}')`(Linux)  


## Enable ssh git bash  (Windows) 
`> eval "$(ssh-agent.exe)"`  
`> ssh-add path/to/.ssh/id_rsa`  
`> git clone <url>`


## remove old ssh key (Linux)
`ssh-keygen -f "/home/<user/.ssh/known_hosts" -R "<ip>"`  

## set default ssh key used by windows ssh service:
`ps > set_default_ssh_key.ps1 <path_to_file> `  
script must be run with administrator privileges and ps script execution must be enabled.

## enable ssh_agent in linux
`$ eval "$(ssh-agent -s)"`  
`$ ssh-add ~/.ssh/<priv_key>`
