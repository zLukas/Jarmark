from cmd import input
from api import secrets
from api import workflow
import yaml



if __name__ == "__main__":
    args = input.parse_args()
    print(args)
    secrets.list(input.parse_config_file(args['config_file']))
    workflow.list(input.parse_config_file(args['config_file']))
    data = workflow.get_source_files(input.parse_config_file(args['config_file']),"test_workflow.yaml" )
    print(yaml.dump(data, sort_keys=False))