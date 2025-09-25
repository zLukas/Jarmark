from api.client import login



def list(config: dict):
    g = login(config['token'])
    repo = g.get_repo(f"{config['owner']}/{config['repo']}")
    secrets = repo.get_secrets()
    for secret in secrets:
        print(f"Name: {secret.name}, Created at: {secret.created_at}, Updated at: {secret.updated_at}")