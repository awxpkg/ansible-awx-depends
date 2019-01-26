%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name selectors2
%define version 2.0.1
%define unmangled_version 2.0.1
%define unmangled_version 2.0.1
%define release 1

Summary: Back-ported, durable, and portable selectors
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}selectors2
Version: %{version}
Release: %{release}
Source0: selectors2-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/selectors2-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Seth Michael Larson <sethmichaellarson@protonmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://www.github.com/SethMichaelLarson/selectors2


%description
Selectors2
==========

.. image:: https://img.shields.io/travis/SethMichaelLarson/selectors2/master.svg?style=flat-square
    :target: https://travis-ci.org/SethMichaelLarson/selectors2
.. image:: https://img.shields.io/appveyor/ci/SethMichaelLarson/selectors2/master.svg?style=flat-square
    :target: https://ci.appveyor.com/project/SethMichaelLarson/selectors2
.. image:: https://img.shields.io/pypi/v/selectors2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/selectors2
.. image:: https://img.shields.io/badge/say-thanks-ff69b4.svg?style=flat-square
    :target: https://saythanks.io/to/SethMichaelLarson

Backported, durable, and portable selectors designed to replace
the standard library selectors module.

Features
--------

* Support for all major platforms. (Linux, Mac OS, Windows)
* Support for Python 2.6 or later and **Jython**.
* Support many different selectors
    * ``select.kqueue`` (BSD, Mac OS)
    * ``select.devpoll`` (Solaris)
    * ``select.epoll`` (Linux 2.5.44+)
    * ``select.poll`` (Linux, Mac OS)
    * ``select.select`` - (Linux, Mac OS, Windows)
* Support for `PEP 475 <https://www.python.org/dev/peps/pep-0475/>`_ (Retries system calls on interrupt)
* Support for modules which monkey-patch the standard library after import (like greenlet, gevent)
* Support for systems which define a selector being available but don't actually implement it. ()

About
-----

This module was originally written by me for the `urllib3 <https://github.com/shazow/urllib3>`_ project
(history in PR `#1001 <https://github.com/shazow/urllib3/pull/1001>`_) but it was decided that it would
be beneficial for everyone to have access to this work.

All the additional features that ``selectors2`` provides are real-world problems that have occurred
and been reported during the lifetime of its maintenance and use within ``urllib3``.

If this work is useful to you, `feel free to say thanks <https://saythanks.io/to/SethMichaelLarson>`_,
takes only a little time and really brightens my day! :cake:

Can this module be used in place of ``selectors``?
--------------------------------------------------

Yes! This module is a 1-to-1 drop-in replacement for ``selectors`` and
provides all selector types that would be available in ``selectors`` including
``DevpollSelector``, ``KqueueSelector``, ``EpollSelector``, ``PollSelector``, and ``SelectSelector``.

What is different between `selectors2` and `selectors34`?
---------------------------------------------------------

This module is similar to ``selectors34`` in that it supports Python 2.6 - 3.3
but differs in that this module also implements PEP 475 for the backported selectors.
This allows similar behaviour between Python 3.5+ selectors and selectors from before PEP 475.
In ``selectors34``, an interrupted system call would result in an incorrect return of no events, which
for some use cases is not an acceptable behavior.

I will also add here that ``selectors2`` also makes large improvements on the test suite surrounding it
providing 100% test coverage for each selector.  The test suite is also more robust and tests durability
of the selectors in many different situations that aren't tested in ``selectors34``.

What types of objects are supported?
------------------------------------

At this current time ``selectors2`` only support the ``SelectSelector`` for Windows which cannot select on non-socket objects.
On Linux and Mac OS, both sockets and pipes are supported (some other types may be supported as well, such as fifos or special file devices).

What if I have to support a platform without ``select.select``?
---------------------------------------------------------------

There are a few platforms that don't have a selector available, notably
Google AppEngine. When running on those platforms any call to ``DefaultSelector()``
will raise a ``RuntimeError`` explaining that there are no selectors available.

License
-------

This module is dual-licensed under MIT and PSF License.

Installation
------------

``$ python -m pip install selectors2``

Usage
-----
.. code-block:: python

    import sys
    import selectors2 as selectors

    # Use DefaultSelector, it picks the best
    # selector available for your platform! :)
    s = selectors.DefaultSelector()

    import socket

    # We're going to use Google as an example.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("www.google.com", 80))

    # Register the file to be watched for write availibility.
    s.register(sock, selectors.EVENT_WRITE)

    # Give a timeout in seconds or no
    # timeout to block until an event happens.
    events = s.select(timeout=1.0)

    # Loop over all events that happened.
    for key, event in events:
        if event & selectors.EVENT_WRITE:
            key.fileobj.send(b'HEAD / HTTP/1.1\r\n\r\n')

    # Change what event you're waiting for.
    s.modify(sock, selectors.EVENT_READ)

    # Timeout of None let's the selector wait as long as it needs to.
    events = s.select(timeout=None)
    for key, event in events:
        if event & selectors.EVENT_READ:
            data = key.fileobj.recv(4096)
            print(data)

    # Stop watching the socket.
    s.unregister(sock)
    sock.close()


Changelog
=========

Release 2.0.1 (August 17, 2017)
-------------------------------

* [BUGFIX] Timeouts would not be properly recalculated after receiving an EINTR error.

Release 2.0.0 (May 30, 2017)
----------------------------

* [FEATURE] Add support for Jython with ``JythonSelectSelector``.
* [FEATURE] Add support for ``/dev/devpoll`` with ``DevpollSelector``.
* [CHANGE] Raises a ``RuntimeError`` instead of ``ValueError`` if there is no selector available.
* [CHANGE] No longer wraps exceptions in ``SelectorError``, raises original exception including
  in timeout situations.
* [BUGFIX] Detect defects in a system that defines a selector but does not implement it.
* [BUGFIX] Can now detect a change in the ``select`` module after import such as when
  ``gevent.monkey.monkey_patch()`` is called before importing ``selectors2``.

Release 1.1.1 (February 6, 2017)
--------------------------------

* [BUGFIX] Platforms that define ``select.kqueue`` would not have ``KqueueSelector`` as the ``DefaultSelector``.

Release 1.1.0 (January 17, 2017)
--------------------------------

* [FEATURE] Make system calls faster for Python versions that support PEP 475.
* [FEATURE] Wheels are now universal.

Release 1.0.0 (November 3, 2016)
--------------------------------

* Initial implementation of ``selectors2``.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n selectors2-%{unmangled_version} -n selectors2-%{unmangled_version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf $RPM_BUILD_ROOT
%{?scl:EOF}


%files -f INSTALLED_FILES
%defattr(-,root,root)
