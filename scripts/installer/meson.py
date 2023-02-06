from pathlib import Path
from subprocess import Popen, PIPE
from typing import Optional
from .path_utils import which
from .process_utils import run_process_and_log
import shlex

class MesonError(Exception):
    stderr: str
    returncode: int
    def __init__(self, command: str, stderr: str, returncode: int):
        super().__init__(f'meson {command} command exited with code {returncode}')
        self.stderr = stderr
        self.returncode = returncode

class Meson():
    __path: Path
    def __init__(self, path: Path) -> None:
        self.__path = path

    def setup(self, project: Path, target: Path) -> None:
        stdout, stderr, returncode = run_process_and_log(
            [str(self.__path), 'setup', str(target)],
            cwd=project,
            prefix='MESON',
        )
        if returncode != 0:
            raise MesonError('setup', stderr, returncode)

    def compile(self, project: Path, target: Path) -> None:
        stdout, stderr, returncode = run_process_and_log(
            [str(self.__path), 'compile', '-C', str(target)],
            cwd=project,
            prefix='MESON',
        )
        if returncode != 0:
            raise MesonError('compile', stderr, returncode)


def get_meson() -> Optional[Meson]:
    maybe_meson_path = which('meson')
    if maybe_meson_path is not None:
        return Meson(maybe_meson_path)
    else:
        return None
