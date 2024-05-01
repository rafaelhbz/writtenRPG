import importlib
import subprocess

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is installed.")
        return True
    except ImportError:
        print(f"{package_name} is not installed.")
        return False

def install_package(package_name):
    subprocess.check_call(["pip", "install", package_name])

def check_and_install_packages(package_list):
    missing_packages = [package for package in package_list if not check_package(package)]
    for package in missing_packages:
        install_package(package)
