from pathlib import Path

from core import env


def get_project_dev_config_file_path(with_filename: str) -> Path:
    return Path(f"{env.get_tank_config_templates_dir_name()}/some_project_dev/{with_filename}")
