from pathlib import Path
from subprocess import Popen, PIPE
from typing import Optional
from .path_utils import which
from .process_utils import run_process_and_log

class GitError(Exception):
    stderr: str
    returncode: int
    def __init__(self, command: str, stderr: str, returncode: int):
        super().__init__(f'git {command} command exited with code {returncode}')
        self.stderr = stderr
        self.returncode = returncode

class Git():
    __path: Path
    def __init__(self, path: Path) -> None:
        self.__path = path

    def clone(self, repository: str, target: Path) -> None:
        stdout, stderr, returncode = run_process_and_log(
            [str(self.__path), 'clone', repository, str(target)],
            prefix='GIT',
        )
        if returncode != 0:
            raise GitError('clone', stderr, returncode)

def get_git() -> Optional[Git]:
    maybe_git_path = which('git')
    if maybe_git_path is not None:
        return Git(maybe_git_path)
    else:
        return None
