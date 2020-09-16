import logging
from pathlib import Path

from core.exception.pt_exception import PTException
from core.helpers.base_generator import BaseGenerator


class ConfigGenerator(BaseGenerator):
    def __init__(self, config_template_file_path: Path, generated_ammo_file_path: Path):
        super().__init__()
        self.__config_template_file_path: Path = config_template_file_path
        self.__generated_ammo_file_path: Path = generated_ammo_file_path

    def generate(self) -> Path:
        """Return new generated config file Path"""
        config_template_file_path = self.__config_template_file_path

        if not config_template_file_path.exists():
            raise PTException('Config template file do not exists! Please, create it')

        with open(config_template_file_path, 'r') as file:
            file_data = file.read()

        file_data = file_data.replace("address: GENERATED", f"address: {self.base_url}:443")
        file_data = file_data.replace("ammofile: GENERATED", f"ammofile: {self.__generated_ammo_file_path.absolute()}")
        file_data = file_data.replace("token_file: GENERATED", f"token_file: {Path('token.txt').absolute()}")

        prepared_config_file_name = config_template_file_path.name.replace('.yaml', '')
        file_data = file_data.replace("job_name: GENERATED", f"job_name: {prepared_config_file_name}")

        generated_config_file_path = Path(f"{prepared_config_file_name}_generated.yaml")
        with open(generated_config_file_path, 'w') as file:
            file.write(file_data)

        if not generated_config_file_path.exists():
            raise PTException('Config generated file do not exists! Performance tests can not run without it')

        logging.info(f"Config successfully generated to {generated_config_file_path.absolute()}")
        return generated_config_file_path
