from abc import ABC, abstractmethod


class Operator(ABC):

    @abstractmethod
    def evaluate(self, value_to_evaluate):
        pass
