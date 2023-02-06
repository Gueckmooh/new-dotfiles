from .source import Source, GitSource
from pathlib import Path
from .package_factory import read_package_file

if __name__ == "__main__":
    pkg = read_package_file(Path('/home/brignone/.local/share/chezmoi/scripts/termite.yaml'))
    path = Path('/tmp/toto/termite')
    pkg.checkout(path)
    pkg.build(path)
