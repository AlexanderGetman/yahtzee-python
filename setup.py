from setuptools import setup, find_packages

setup(
    name='pyahtzee',
    version='0.4.7',
    packages=['pyahtzee'],
    entry_points={
      'console_scripts': [
        'pyahtzee=pyahtzee.game:game',
      ],
    }  
)