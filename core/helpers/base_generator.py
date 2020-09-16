from abc import ABC, abstractmethod
from pathlib import Path

from core import env


class BaseGenerator(ABC):
    def __init__(self):
        self.base_url = env.get_base_url()

    @abstractmethod
    def generate(self) -> Path:
        pass
