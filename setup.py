from setuptools import setup

setup(
    name='ondemand',
    version='1.0.0',
    description='Simple client for Barchart OnDemand REST APIs',
    author="Mike Ehrenberg",
    author_email="solutions@barchart.com",
    url='https://www.barchartondemand.com/api',
    install_requires=[
        'requests>=2.3.0'
    ],
    license='LICENSE.txt',
    packages=['ondemand'])
