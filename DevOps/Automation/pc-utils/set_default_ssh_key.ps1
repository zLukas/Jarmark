ssh_key=$args[0]

if ( Test-Path ssh_key -PathType Leaf)
{
    Get-Service ssh-agent | Set-Service -StartupType Manual
    Start-Service ssh-agent
    ssh-add $args[0]
}
else
{
    echo "$ssh_key not exist"
}