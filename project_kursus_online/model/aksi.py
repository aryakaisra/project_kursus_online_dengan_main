
from abc import ABC, abstractmethod

class AksiPengguna(ABC):
    @abstractmethod
    def lihat_dashboard(self):
        pass

    @abstractmethod
    def logout(self):
        pass
