import yaml

# relative path
file_path = '../capstone/config.yaml'
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

