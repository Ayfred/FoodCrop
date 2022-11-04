from abc import ABC, abstractmethod
## En cours de construction
class Describable(ABC):

    @abstractmethod
    def describe(self):
        pass
