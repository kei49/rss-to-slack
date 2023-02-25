import os

def setup_dir_for_file_path(file_path: str):
    create_dir_if_not_exists('/'.join(file_path.split('/')[:-1]))


def create_dir_if_not_exists(path):
    os.makedirs(path, exist_ok=True)