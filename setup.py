from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customnavbar/__init__.py
from customnavbar import __version__ as version

setup(
	name="customnavbar",
	version=version,
	description="Navbar",
	author="Hak3em",
	author_email="abdoamer19@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
