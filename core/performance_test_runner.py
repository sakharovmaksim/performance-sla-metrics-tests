import logging
import subprocess
from pathlib import Path

from core.helpers.ammo_generator import AmmoGenerator
from core.helpers.config_generator import ConfigGenerator
from core.helpers.test_result_data import TestResultData


def run_performance_test(config_template_file_path: Path, ammo_template_file_path: Path) -> int:
    """Return status code of test run process"""
    generated_ammo_file_path = AmmoGenerator(ammo_template_file_path=ammo_template_file_path).generate()
    generated_config_file_path = ConfigGenerator(config_template_file_path=config_template_file_path,
                                                 generated_ammo_file_path=generated_ammo_file_path).generate()

    generated_config_file_name = str(generated_config_file_path.name)

    # Root path is parent dir of script!
    root_path: Path = Path().parent

    command_list = ['docker', 'run', '--rm',
                    '-v', f"{root_path.absolute()}:/var/loadtest",
                    '--net', 'host', 'direvius/yandex-tank', '-c', f"{generated_config_file_name}",
                    '-o', 'tank.artifacts_dir=run_logs']
    logging.info(f"Executing bash script in python subprocess {str(command_list)}")

    with subprocess.Popen(command_list, stdout=subprocess.PIPE, universal_newlines=True) as process:
        # Logging stdout from subprocess in console. universal_newlines=True needle
        for line in process.stdout:
            print(line, end='')

    test_result_data = TestResultData()
    logging.info(f"Yandex Tank testing process finished with status {test_result_data.exit_code}")

    return test_result_data.exit_code
