import logging
from pathlib import Path
from typing import Optional


class OverloadServiceHelper:
    def __init__(self):
        self.__jobno_file_path: Path = Path('jobno_file.txt')
        self.__job_id: Optional[int] = None
        self.create_overload_job_id()

    @property
    def overload_job_id(self) -> Optional[int]:
        """Return example: 294770"""
        return self.__job_id

    def create_overload_job_id(self):
        job_id: Optional[int] = None

        if self.__jobno_file_path.exists():
            with open(self.__jobno_file_path) as file:
                job_id = int(file.readline())
        self.__job_id = job_id

    def get_overload_job_url(self) -> Optional[str]:
        """Return example: 'https://overload.yandex.net/294770'"""
        job_url: Optional[str] = None

        job_id = self.overload_job_id
        if job_id:
            job_url = f"https://overload.yandex.net/{job_id}"
        return job_url

    def log_overload_job_url(self):
        job_url = self.get_overload_job_url()
        if job_url:
            logging.warning(f"--- Test overload analytics in: {job_url} ---")
