import yaml
from pathlib import Path
from .package import Package, MesonPackage, NonePackage
from .source import Source, GitSource
from . import distrib

def read_package_file(package_file: Path) -> Package:
    with open(package_file, 'r') as file:
        data = yaml.safe_load(file)
    return get_package(data)

def get_package(package_data) -> Package:
    package_name = package_data['name']
    if distrib.os_linux() and 'linux' in package_data.keys():
        linux_data = package_data['linux']
        if 'all' in linux_data.keys():
            all_data = linux_data['all']
            if 'meson' in all_data.keys():
                meson_data = all_data['meson']
                return get_meson_package(package_name, meson_data)
    else:
        return NonePackage(package_name)

def get_meson_package(name: str, package_data) -> Package:
    if 'git' in package_data.keys():
        source = GitSource(package_data['git'])
    else:
        return NonePackage(name)
    return MesonPackage(name, source)
