=============================
ClickTale for Django Projects
=============================

A simple Django application to integrate ClickTale into Django projects.

Installation
============

Just install ``django-clicktale`` via ``pip``::

    $ pip install django-clicktale

After ``django-clicktale`` is installed, ``clicktale`` application needs
to be added to your ``INSTALLED_APPS`` in ``settings.py``:
    INSTALLED_APPS=(
        ...
        'clicktale',
        ...
    )

Usage
=====

s

Settings
========

There are a few settings that needs to be set. If the bellow settings
are not set, the clicktale tracking code will not be generated.

CLICKTALE_PROJECT_ID (integer)
  This is the id of the project created in Clicktale

CLICKTALE_RECORDING_RATIO (float)
  The recording ratio. For more information the `Clicktale wiki page`_
  can be consulted.

CLICKTALE_PARTITION_ID (string)
  This value is generated when creating a new tracking code in Clicktale
  interface. Eg: 'www14'

CLICKTALE_AJAX_ENABLED (boolean)
  If this is enabled, Clicktale will track ajax request. This kind of
  tracking is available only for Enterprise customer, so if you don't
  have an enterprise account set this to False. More info about this
  issue can be found in `Clicktale Ajax wiki`_ page.

.. _`Clicktale wiki page`: http://wiki.clicktale.com/Article/Recording_Ratio
.. _`Clicktale Ajax wiki`: http://wiki.clicktale.com/Article/Ajax
