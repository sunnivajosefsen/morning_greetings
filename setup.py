from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A package to automate sending Good Morning messages",
    author="Sunniva Josefsen",
    author_email="sunniva.josefsen@hotmail.com",
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',  # Point to the main function in main.py
        ],
    },
)
