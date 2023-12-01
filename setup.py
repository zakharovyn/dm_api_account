from distutils.core import setup

REQUIRES = [
    'requests',
    'allure-pytest'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/zakharovyn/dm_api_account.git',
    license='MIT',
    author='yanzakharov',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account: apis, models'
)
