Prerequisites
===============

You need to install the package libmagickwand-dev on Debian-like::

    $ apt-get install libmagickwand-dev

This requirements are automatically installed with pip and are include in the setup.py file

Wand => Wand is a ctypes-based simple ImageMagick binding for Python.

python-magic => This module uses ctypes to access the libmagic file type identification library.

Pillow => Pillow is the friendly PIL fork by Alex Clark and Contributors.


Installing
============

Install the apps with pip ::

    $ pip install django-paperworks

Configure your settings file
-------------------------------

Add django-paperworks to your installed_apps ::

    INSTALLED_APPS = [
        ...
        'paperworks',
    ]

Configure MEDIA_ROOT setting

If you want store files and thumbnails to a subfolder configure PAPERWORKS_MEDIA_ROOT variable

Configure your urls file
-----------------------------

Add django-paperworks to urls file ::

    from django.conf.urls import url, include
    from paperworks import urls
    ...
    urlpatterns = [
        ...
        url(r'^', include('paperworks.urls')),
    ]

