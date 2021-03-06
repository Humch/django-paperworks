import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-paperworks',
    version='0.0.6',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='a Django app to store and to sort personal paperworks',
    long_description=README,
    url='https://github.com/Humch/django-paperworks',
    author='Fabien Schlegel',
    author_email='fabienschlegel@yahoo.fr',
    install_requires=[
        'Wand',
        'Pillow',
        'python-magic',
        'django-auxiliare'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)