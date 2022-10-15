from abc import ABC, abstractmethod

class Describable(ABC):

    @abstractmethod
    def describe(self):
        pass
