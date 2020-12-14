import logging
import re


class TargetHostData:
    def __init__(self, target_full_url: str):
        self.__full_url = target_full_url

    @property
    def full_url(self) -> str:
        """Return example: 'https://ya.ru'"""
        logging.info(f"Got full target host url '{self.__full_url}'")
        return self.__full_url

    @property
    def url_without_scheme(self) -> str:
        """Return example: 'ya.ru'"""
        result = re.sub(r"http\w://", '', self.__full_url)
        logging.info(f"Got target host url without scheme '{result}'")
        return result
