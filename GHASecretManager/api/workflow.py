from logging import config
from api.client import login


def list(config: dict):
    g = login(config['token'])
    repo = g.get_repo(f"{config['owner']}/{config['repo']}")
    workflows = repo.get_workflows()
    for wf in workflows:
        print(f"Name: {wf.name}, ID: {wf.id}, State: {wf.state}")

def get_usage_by_id(config: dict, workflow_id: int) -> list:
    g = login(config['token'])
    repo = g.get_repo(f"{config['owner']}/{config['repo']}")
    workflow = repo.get_workflow(workflow_id)
    usage = workflow.get_usage()
    return usage

def get_source_files(config: dict, workflow_id: int) -> list:
    g = login(config['token'])
    repo = g.get_repo(f"{config['owner']}/{config['repo']}")
    workflow = repo.get_workflow(workflow_id)
    content_file = repo.get_contents(f".github/workflows/{workflow.path}")
    return content_file.decoded_content.decode('utf-8').splitlines()