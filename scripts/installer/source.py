from abc import ABC, abstractmethod
from pathlib import Path
from .path_utils import working_directory
from .git import get_git, Git

class Source(ABC):
    @abstractmethod
    def checkout(self, path: Path) -> None:
        pass

class GitSource(Source):
    __url: str
    def __init__(self, url: str) -> None:
        self.__url = url

    def checkout(self, path: Path) -> None:
        parent = path.parent
        parent.mkdir(parents=True, exist_ok=True)
        git = get_git()
        if git is None:
            return
        git.clone(self.__url, path)
