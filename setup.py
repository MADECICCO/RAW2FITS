import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()




# Read requirements file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='RAW2FITS',
    version='0.1',
    author='Hadrien A. R. Devillepoix',
    author_email='hadriendvpx@gmail.com',
    description = ("Just another tool to convert consumer digital cameras RAW images to FITS."),
    packages=find_packages(),
    license='LICENSE',
    long_description=open('README.md').read(),
    install_requires=requirements
)
