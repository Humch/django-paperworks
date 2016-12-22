.. django-paperworks documentation master file, created by
   sphinx-quickstart on Thu Dec 22 17:58:34 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-paperworks's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Django Paperworks is a reusable application for Django to store personal paperworks as an EDM software.

Installation
**********************

Prerequisites
---------------

This requirements are automatically installed with pip and are include in the setup.py file

Wand => Wand is a ctypes-based simple ImageMagick binding for Python.
python-magic => This module uses ctypes to access the libmagic file type identification library.
Pillow => Pillow is the friendly PIL fork by Alex Clark and Contributors.

Installing
------------

Install the apps with pip ::

    $ pip install django-paperworks

Configure your settings file
-----------------------------

Add django-paperworks to your installed_apps ::

    INSTALLED_APPS = [
        ...
        'paperworks.apps.PaperworksConfig',
    ]

Configure MEDIA_ROOT setting

If you want store files and thumbnails to a subfolder configure PAPERWORKS_MEDIA_ROOT variable

Add django-paperworks to urls file ::

    from django.conf.urls import url, include
    from paperworks import urls
    ...
    urlpatterns = [
        ...
        url(r'^', include('paperworks.urls')),
    ]

