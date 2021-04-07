from setuptools import setup, find_packages
from common.settings import __version__, __author__

setup(
    name='slay_the_spire_neural',
    version=__version__,
    description='Проект по обучнию нейронной сети по игре slay the spire и небольшая документация к ней',
    url='',
    author=__author__,
    packages=find_packages(),
    python_requires='>=3.6',
)
