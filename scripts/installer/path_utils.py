import os
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional

@contextmanager
def working_directory(path: Path) -> Iterator[None]:
    "Changes working directory and return to previous on exit."
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)

def which(exe: str) -> Optional[Path]:
    for exe_dir in os.get_exec_path():
        exe_path = Path(exe_dir) / exe
        if exe_path.exists():
            return exe_path
    return None
