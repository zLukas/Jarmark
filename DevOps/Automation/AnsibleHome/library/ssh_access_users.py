#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os



def parse_params() -> AnsibleModule:
    """
    Parses and returns the AnsibleModule with the required parameters for the ssh_access_users module.
    Returns:
        AnsibleModule: An instance of AnsibleModule initialized with the required arguments.
    Raises:
        None
    The function defines the expected arguments for the module, specifically:
        - ssh_keys_dir (str): The directory containing SSH keys. This parameter is required.
    """
    
    module_args = dict(
        ssh_keys_dir=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    return AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )


def create_user_with_ssh_access(module: AnsibleModule, ssh_keys_dir: str,key_files: list, result: dict) -> None:
    """
    Creates users based on SSH public keys found in the specified directory and sets up their SSH access.
    Args:
        module (AnsibleModule): The Ansible module instance.
        ssh_keys_dir (str): The directory containing SSH public keys.
        key_files (list): List of public key files to process.
        result (dict): Dictionary to store the result of the operation.
    Returns:
        None
    """
    for key_file in key_files:
            username = os.path.splitext(key_file)[0]
            key_path = os.path.join(ssh_keys_dir, key_file)

            try:
                with open(key_path, 'r') as f:
                    public_key = f.read().strip()
            except Exception as e:
                module.fail_json(msg=f"Failed to read key {key_file}: {e}", **result)

            # Ensure user exists
            rc, _, _ = module.run_command(['id', username])
            if rc != 0:
                rc, out, err = module.run_command(['useradd', '-m', '-s', '/bin/bash', username])
                if rc != 0:
                    module.fail_json(msg=f"Failed to create user '{username}': {err}", **result)
                result['changed'] = True
                result['created_users'].append(username)

            ssh_dir = f"/home/{username}/.ssh"s
            authorized_keys_path = os.path.join(ssh_dir, "authorized_keys"

            module.run_command(['mkdir', '-p', ssh_dir])
            module.run_command(['chown', f"{username}:{username}", ssh_dir])
            module.run_command(['chmod', '700', ssh_dir])

            # Write the key
            module.run_command(f"echo '{public_key}' > {authorized_keys_path}", use_unsafe_shell=True)
            module.run_command(['chown', f"{username}:{username}", authorized_keys_path])
            module.run_command(['chmod', '600', authorized_keys_path])


def get_key_files(module: AnsibleModule, ssh_keys_dir: str) -> list:
    """
    Retrieves the list of public key files from the specified directory.
    Args:
        module (AnsibleModule): The Ansible module instance.
        ssh_keys_dir (str): The directory containing SSH public keys.
    Returns:
        list: A list of public key files found in the directory.
    Raises:
        None
    """
    if not os.path.exists(ssh_keys_dir):
        module.fail_json(msg=f"Local directory '{ssh_keys_dir}' does not exist", **result)

    key_files = [f for f in os.listdir(ssh_keys_dir) if f.endswith('.pub')]
    if not key_files:
        module.exit_json(msg="No public keys found in directory", **result)

def main():
    module = parse_params()

    ssh_keys_dir = module.params['ssh_keys_dir']
    result = {"changed": False, "created_users": []}

    key_files = get_key_files(module, ssh_keys_dir)

    create_user_with_ssh_access(module, key_files, result)

    module.exit_json(msg="Users created successfully", **result)

if __name__ == '__main__':
    main()
