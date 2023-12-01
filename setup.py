from distutils.core import setup
from setuptools import setup, find_packages

REQUIRES = [
    'requests',
    'allure-pytest'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/zakharovyn/dm_api_account.git',
    license='MIT',
    author='yanzakharov',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account: apis, models'
)
