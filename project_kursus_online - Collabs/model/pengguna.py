
from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def login(self, password):
        pass

class Admin(Pengguna):
    def login(self, password):
        return f"Admin {self.username} logged in with admin privileges."

class Instruktur(Pengguna):
    def login(self, password):
        return f"Instruktur {self.username} logged in and can manage modules."

class Siswa(Pengguna):
    def login(self, password):
        return f"Siswa {self.username} logged in and can enroll in courses."
