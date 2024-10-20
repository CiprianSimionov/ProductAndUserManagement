"""interfata abstracta cu metodele create,read,update si delete"""
#punctul 1 miniproiect
from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, entry_id):
        pass

    @abstractmethod
    def update(self, entry_id, new_data):
        pass

    @abstractmethod
    def delete(self, entry_id):
        pass

