"""An envelope for effortlessly accessing system and distribution information."""

import platform
import distro

def os_windows() -> bool:
    "True if os is Windows."
    return platform.system() == 'Windows'

def os_linux() -> bool:
    "True if os is Linux."
    return platform.system() == 'Linux'

def distro_arch() -> bool:
    "True if distro is arch linux."
    return distro.id() == 'arch'

def distro_debian() -> bool:
    "True if distro is debian."
    return distro.id() == 'debian'
