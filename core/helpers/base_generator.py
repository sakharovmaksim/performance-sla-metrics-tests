from abc import ABC, abstractmethod
from pathlib import Path

from core import env


class BaseGenerator(ABC):
    def __init__(self):
        self.target_host_url = env.get_target_host_data().url_without_scheme

    @abstractmethod
    def generate(self) -> Path:
        pass
