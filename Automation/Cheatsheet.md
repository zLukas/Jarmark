# Bash oneliners:

## Rename file extension in current directory  
`$ for FILE in *.log; do mv -- "$FILE" "${FILE%.log}.json; done`

## Reformat json document  
`$ for FILE in *.json; do jq . "$FILE" > pretty_"${FILE}"; done`

## find all merge confict in files  
`$ for f in $( find . -name *.yaml); do grep "<<<<<<< HEAD" -Hn $f ;done`


# Ansible 
## execute single command on every host
```   
$ ANSIBLE_CMD="ansible all -i inventory.ini --private-key ~/.ssh/<key> -m shell -a "
$ $ANSIBLE_CMD "<commands>"

```

# Cloud
## aws decode sts message:
aws sts decode-authorization-message --encoded-message <message> | jq '.DecodedMessage' | sed 's/^\"//g;s/\"$//g;s/\\//g' | jq


# Github cli
## run workflow manually
gh workflow run name.yaml --ref=branch