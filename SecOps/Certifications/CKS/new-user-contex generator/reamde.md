# CKS exercise

create a system that has 3 namespaces
* public 
* private 

requisities:
* pods in private namespace have Read access to public namespace resources
* pods/jobs in private namespace can create/modify/delete (only) deployments in public namespace
* pods in public have no access to any resources in private namespace


each namespace is accessible only via specific context:
* public-ctx
* private-ctx
ś



