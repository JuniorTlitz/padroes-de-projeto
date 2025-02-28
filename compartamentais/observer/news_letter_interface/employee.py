from news_letter_observer import NewsLetterObserver
from subject import Subject


class Employee(NewsLetterObserver):
    def __init__(self, name: str, email: str, subject: Subject):
        self._name = name
        self._email = email
        self._subject = subject
        self._subject.register_observer(self)

    def update(self, message: str) -> None:
        return f"Email enviado para {self._email} com a mensagem: {message}"

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email
