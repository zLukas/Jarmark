#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def main():
    module_args = dict(
        ssh_keys_dir=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    ssh_keys_dir = module.params['ssh_keys_dir']
    result = {"changed": False, "created_users": []}

    if not os.path.exists(ssh_keys_dir):
        module.fail_json(msg=f"Local directory '{ssh_keys_dir}' does not exist", **result)

    key_files = [f for f in os.listdir(ssh_keys_dir) if f.endswith('.pub')]
    if not key_files:
        module.exit_json(msg="No public keys found in directory", **result)

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

        ssh_dir = f"/home/{username}/.ssh"
        authorized_keys_path = os.path.join(ssh_dir, "authorized_keys")

        module.run_command(['mkdir', '-p', ssh_dir])
        module.run_command(['chown', f"{username}:{username}", ssh_dir])
        module.run_command(['chmod', '700', ssh_dir])

        # Write the key
        module.run_command(f"echo '{public_key}' > {authorized_keys_path}", use_unsafe_shell=True)
        module.run_command(['chown', f"{username}:{username}", authorized_keys_path])
        module.run_command(['chmod', '600', authorized_keys_path])

    module.exit_json(msg="Users created successfully", **result)

if __name__ == '__main__':
    main()
