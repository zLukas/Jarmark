from argparse import ArgumentParser
from os import path
import configparser
import os

DEFAULT_CONFIG_PATH = os.path.expanduser("~/.gha/config.ini")
def parse_args() -> dict:
    parser = ArgumentParser(description="GHA Secret Manager")

    parser.add_argument(
        "-c",
        "--config-file",
        type=str,
        required=True,
        help="Path to the configuration file (env var GHA_SECRET_MANAGER_CONFIG_FILE), defaults to ~/.gha/config.ini ",
    )
    parser.add_argument(
        "-a",
        "--action",
        choices=["list", "check", "cleanup"],
        type=str,
        help="""(Required) Action to perform:
                       <list> - list all secrets,
                       <check> - whether secrets are used in workflows,
                       <cleanup> - remove unused secrets
                """
    )
    args = parser.parse_args()

    if not args.config_file:
        if os.environ.get("GHA_SECRET_MANAGER_CONFIG_FILE"):
            args.config_file = os.environ.get("GHA_SECRET_MANAGER_CONFIG_FILE")
        elif path.isfile(DEFAULT_CONFIG_PATH):
            args.config_file = DEFAULT_CONFIG_PATH
    if not path.isfile(args.config_file):
        parser.error(f"Config file '{args.config_file}' does not exist.")
    if args.action is None:
        parser.error("You must specify an action, run --help for more information.")
    return vars(args)



def parse_config_file(config_file: str) -> dict:
    config = configparser.ConfigParser()
    if not path.isfile(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' does not exist.")

    config.read(config_file)

    repo = config.get('default', 'repo', fallback=None)
    owner = config.get('default', 'owner', fallback=None)
    token = config.get('default', 'token', fallback=None)
    if not token:
        token = os.environ.get("GH_TOKEN")
    if not repo or not owner or not token:
        raise ValueError("Config file must set 'repo', 'owner', and 'token' in the [defaults] section.")
    return {
        'repo': repo,
        'owner': owner,
        'token': token
    }
