telnetsrv
=========

Modification of `telnetsrvlib`_.
 
This package is intended to be used as a library build to a mocking Telnet server that acts as a testing environment for
telnet client interactions coming from a software being developed.  

**DO NOT USE THIS IN PRODUCTION.** This software is provided AS IS with NO WARRANTY or support whatsoever.

Various features available on the source base of this package
(`telnetsrvlib`_) were intentionally removed to provide a clean, simpler way
of handling telnet client interactions - as made explicit above, this package is only intended to be used as a library
to build a testing tool. For a more complete, reliable set of functionalities, please use their version instead. The
modifications made can cause the software not work as intended or documented in their page. This version of the software
does not support SSH, Eventlets, the Green version of the handlers and other features.

Licensed under LGPL 3.0, please refer to the `LICENSE`_ file that accompanies this file.

Install
-------
Download the `dist source package`_ and install it directly using pip.

.. code:: bash

  pip install /path/to/telnetsrv-0.4.1.tar.gz

.. _telnetsrvlib: https://github.com/ianepperson/telnetsrvlib
.. _LICENSE: https://github.com/sergioamorim/telnetsrv/blob/master/LICENSE
.. _dist source package: https://github.com/sergioamorim/telnetsrv/blob/master/dist/telnetsrv-0.4.1.tar.gz
