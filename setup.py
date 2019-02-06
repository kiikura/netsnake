from setuptools import setup

setup(
    name="netsnake",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "netsnake = app:main"
        ]
    }
)