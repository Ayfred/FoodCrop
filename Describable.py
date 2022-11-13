from abc import ABC, abstractmethod
class Describable(ABC):

    ## Méthode abstraite describe
    @abstractmethod
    def describe(self):
        pass
