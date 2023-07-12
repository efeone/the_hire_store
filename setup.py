from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ths/__init__.py
from ths import __version__ as version

setup(
	name="ths",
	version=version,
	description="A complete Rental Management system",
	author="efeone",
	author_email="info@efeone.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
