import logging
import subprocess
from pathlib import Path

from core.helpers.ammo_generator import AmmoGenerator
from core.helpers.config_generator import ConfigGenerator


def run_performance_test(config_template_file_path: Path, ammo_template_file_path: Path) -> int:
    """Return status code of test run process"""
    generated_ammo_file_path = AmmoGenerator(ammo_template_file_path=ammo_template_file_path).generate()
    generated_config_file_path = ConfigGenerator(config_template_file_path=config_template_file_path,
                                                 generated_ammo_file_path=generated_ammo_file_path).generate()

    # Full path to config file
    generated_config_file = str(generated_config_file_path.absolute())

    command_list = ['yandex-tank', '-c', generated_config_file, '-o', 'tank.artifacts_dir=run_logs']
    logging.info(f"Executing bash script in python subprocess {str(command_list)}")

    with subprocess.Popen(command_list, stdout=subprocess.PIPE, universal_newlines=True) as process:
        # Logging stdout from subprocess in console. universal_newlines=True needle
        for line in process.stdout:
            print(line, end='')

    return_code = process.returncode
    logging.info(f"Yandex Tank testing process finished with {return_code=}")
    return return_code
