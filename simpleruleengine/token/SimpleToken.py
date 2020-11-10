from abc import ABC, abstractmethod


class SimpleToken(ABC):

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
