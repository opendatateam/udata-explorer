from setuptools import setup, find_packages

setup(
    name='udata-explorer',
    version='0.1',
    description="Explore udata instances' data",
    url='https://github.com/opendatateam/udata-explorer',
    author='Alexandre Bulté',
    author_email='alexandre@bulte.net',
    license='Apache Software License',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'pandas >= 0.20',
        'requests >= 2.18'
    ],
)
