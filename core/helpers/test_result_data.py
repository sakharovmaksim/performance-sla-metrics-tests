import logging
import shutil
import yaml

from pathlib import Path
from typing import Dict


class TestResultData:
    def __init__(self):
        self.__logs_dir_path: Path = Path().parent / "logs"
        self.__report_file_path: Path = self.__logs_dir_path / "run_logs" / "finish_status.yaml"
        self.__json_data: Dict = dict()

    @property
    def overload_url(self) -> str:
        """Return example: 'https://overload.yandex.net/294770'"""
        return self.__report_data.get('lunapark_url', '')

    @property
    def exit_code(self) -> int:
        """Return example: 0"""
        return self.__report_data.get('exit_code', 1)

    def log_overload_url(self):
        if self.overload_url:
            logging.warning(f"--- Test overload analytics in: {self.overload_url} ---")

    def delete_test_logs_dir(self):
        """Remove logs dir"""
        logging.info(f"Deleting test logs dir: {self.__logs_dir_path.absolute()}")
        shutil.rmtree(self.__logs_dir_path)

    @property
    def __report_data(self) -> dict:
        if not self.__json_data:
            with open(self.__report_file_path, 'r') as json_file:
                self.__json_data = yaml.safe_load(json_file)
        return self.__json_data
