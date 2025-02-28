from abc import ABC, abstractmethod


class NewsLetterObserver(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    def get_email(self):
        pass
