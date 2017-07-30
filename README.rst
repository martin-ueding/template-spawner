.. Copyright © 2013-2014, 2016-2017 Martin Ueding <dev@martin-ueding.de>

################
template-spawner
################

If you have your templates in ``~/Vorlagen``, then this script ``spawn`` will
just copy the given template into your current working directory. You can
abbreviate as long as the name is unique.

I have a ``python.py`` and a ``python3.py`` in my templates directory. So the
``spawn py`` fails, but ``spawn python3`` succeeds::

    $ spawn py
    $ ls
    $ spawn python3
    $ ls
    python3.py

The filename of the template is used by default. You can specify a target file
name (like ``document.tex``) as well::

    $ spawn art document.tex
    $ ls
    document.tex
