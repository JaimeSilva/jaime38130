from distutils.core import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jaime38130',
    packages=['jaime38130'],
    version='0.6',
    license='MIT',
    description='I needed colors',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jaime Silva',
    author_email='jaimedcsilva@hotmail.com',
    url='https://github.com/JaimeSilva/jaime38130.git',
    download_url='https://github.com/JaimeSilva/jaime38130/archive/refs/tags/v_06.tar.gz',
    keywords=['SOME', 'MEANINGFULL', 'COLORS'],
    install_requires=[
        'colorama',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
)
