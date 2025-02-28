from abc import ABC, abstractmethod
from news_letter_observer import NewsLetterObserver


class Subject(ABC):
    @abstractmethod
    def register_observer(self, news_letter_observer: NewsLetterObserver):
        pass

    @abstractmethod
    def remove_observer(self, news_letter_observer: NewsLetterObserver):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
