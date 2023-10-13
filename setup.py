from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='grundfossensor',
    version='0.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    url='https://github.com/AndreasScharf/grundfossensor',
    author='Andreas Scharf',
    author_email='info@frappgmbh.de',
    license='MIT',
    packages=['grundfossensor'],

    classifiers=[
       
    ],
)
