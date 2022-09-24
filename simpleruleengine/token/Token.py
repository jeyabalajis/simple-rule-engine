from abc import ABC, abstractmethod


class Token(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_token_dict_structure(self) -> dict:
        return dict(name=self.name, type=type(self).__name__)

    @abstractmethod
    def get_token_value(self, token_dict: dict):
        if self.name not in token_dict:
            raise ValueError("{} not in token_dict".format(self.name))
        return token_dict.get(self.name)
