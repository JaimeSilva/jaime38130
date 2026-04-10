from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='jaime38130',
    packages=['jaime38130'],
    version='1.2',
    license='MIT',
    description='A simple Python library to print colored text in the terminal using ANSI escape codes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jaime Silva',
    author_email='jaimedcsilva@hotmail.com',
    url='https://github.com/JaimeSilva/jaime38130.git',
    download_url='https://github.com/JaimeSilva/jaime38130/archive/refs/tags/v_11.tar.gz',
    keywords=['python', 'terminal', 'colors', 'ansi', 'cli'],
    install_requires=[
        'colorama',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)