import logging
from pathlib import Path

from core.exception.pt_exception import PTException
from core.helpers.base_generator import BaseGenerator


class AmmoGenerator(BaseGenerator):
    def __init__(self, ammo_template_file_path: Path):
        super().__init__()
        self.__ammo_template_file_path: Path = ammo_template_file_path

    def generate(self) -> Path:
        """Return new generated ammo file Path"""
        ammo_template_file_path = self.__ammo_template_file_path

        if not ammo_template_file_path.exists():
            raise PTException('Ammo template file do not exists! Please, create it')

        with open(ammo_template_file_path, 'r') as file:
            file_data = file.read()

        file_data = file_data.replace("[Host: GENERATED]", f"[Host: {self.target_host_url}]")

        prepared_ammo_file_name = ammo_template_file_path.name.replace('.txt', '')
        generated_ammo_file_path = Path(f"{prepared_ammo_file_name}_generated.txt")
        with open(generated_ammo_file_path, 'w') as file:
            file.write(file_data)

        if not generated_ammo_file_path.exists():
            raise PTException('Ammo generated file do not exists! Performance tests can not run without it')

        logging.info(f"Ammo file successfully generated to {generated_ammo_file_path.absolute()}")
        return generated_ammo_file_path
