from setuptools import find_packages
from setuptools import setup


setup(
    name='alice-precommit',
    description='Pre-commit hooks created by Alice Biometrics',
    url='https://github.com/alicebiometrics/alice-precommit',

    author='Alice Biometrics',
    entry_points={
    'console_scripts': [
        'jwt-checker = hooks.jwt_checker:main'
    ]
},

    packages=find_packages()
)