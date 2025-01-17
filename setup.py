import pathlib

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

from get_latest_version import get_latest_version_number

setup(
    name="flitton_fib_py",
    version=get_latest_version_number(),
    author="Maxwell Flitton",
    author_email="maxwell@gmail.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxwellflitton/flitton-fib-py",
    install_requires=[
        "PyYAML>=4.1.2",
        "dill>=0.2.8"
    ],
    extras_require={
     'server': ["Flask>=1.0.0"]
    },
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'fib-number = flitton_fib_py.cmd.fib_numb:fib_numb',
        ],
    },
    python_requires='>=3',
    tests_require=['pytest'],
)
