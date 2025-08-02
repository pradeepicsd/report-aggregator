from abc import ABC, abstractmethod
from typing import List

class BaseProviderClient(ABC):

    @abstractmethod
    def list_reports(self) -> List[str]:
        pass

    @abstractmethod
    def download_report(self, key: str, dest_path: str) -> str:
        pass
