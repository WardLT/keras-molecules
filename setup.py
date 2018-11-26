import os
import io

from setuptools import setup, find_packages


def read(fname):
    with io.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        return f.read()


setup(
    name='keras-molecules',
    version='0.1.0',
    author='Max Hodak',
    email='maxhodak@gmail.com',
    url='https://github.com/maxhodak/keras-molecules',
    packages=find_packages(),
    python_requires='>=3.5',
    license='MIT',
    description='Autoencoder network for learning a continuous representation of molecular structures',
    long_description=read('README.md')
)
