from setuptools import setup

APP=['main.py']
OPTIONS = {}


setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requirements=['pyapp']
)