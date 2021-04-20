from setuptools import setup

setup(
    name='RtrcSplitCsv',
    version='0.1.0',
    author='Jeff Knight',
    author_email='jknight@arteric.com',
    packages=['package_name', 'package_name.test'],
    scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/RtrcSplitCsv/',
    license='LICENSE.txt',
    description='RTRC package that splits a csv into DataFrame data and a configs dict.',
    long_description=open('README.txt').read(),
    install_requires=[
        'pandas'
    ],
)
