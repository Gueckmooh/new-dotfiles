"""Define the Package class, which contains everything needed to install them."""

from abc import ABC, abstractmethod
from pathlib import Path
from .meson import get_meson, Meson, MesonError

from .source import Source


class PackageForbidden(Exception):
    """The error that is raised if a forbidden action if performed on the
    package."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class Package(ABC):
    """Abstract class that represents a package."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def is_installable(self) -> bool:
        pass

    @abstractmethod
    def build(self, path: Path) -> None:
        pass

    # @abstractmethod
    # def need_build(self) -> bool:
    #     pass

    # @abstractmethod
    # def install(self, path: Path) -> None:
    #     pass

    @abstractmethod
    def checkout(self, path: Path) -> None:
        pass

    # def build_and_install(self, path: Path) -> None:
    #     if self.need_build():
    #         self.build(path)
    #     self.install(path)


class MesonPackage(Package):

    __src: Source

    def __init__(self, name: str, src: Source) -> None:
        super().__init__(name)
        self.__src = src

    def checkout(self, path: Path) -> None:
        return self.__src.checkout(path)

    def build(self, path: Path) -> None:
        meson = get_meson()
        if meson is None:
            return
        try:
            meson.setup(path, Path('builddir'))
            meson.compile(path, Path('builddir'))
        except MesonError as e:
            print(e)
            print(e.stderr)
            exit(1)

    def is_installable(self) -> bool:
        return True


class NonePackage(Package):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def is_installable(self) -> bool:
        return False

    def build(self, path: Path) -> None:
        raise PackageForbidden(f'Package {self.name} cannot be built')

    def checkout(self, path: Path) -> None:
        raise PackageForbidden(f'Package {self.name} cannot be checked out')
