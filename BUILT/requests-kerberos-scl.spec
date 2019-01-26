%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name requests-kerberos
%define version 0.12.0
%define unmangled_version 0.12.0
%define unmangled_version 0.12.0
%define release 1

Summary: A Kerberos authentication handler for python-requests
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}requests-kerberos
Version: %{version}
Release: %{release}
Source0: requests-kerberos-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/requests-kerberos-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ian Cordasco, Cory Benfield, Michael Komitee <graffatcolmingov@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/requests/requests-kerberos


%description
requests Kerberos/GSSAPI authentication library
===============================================

.. image:: https://travis-ci.org/requests/requests-kerberos.svg?branch=master
    :target: https://travis-ci.org/requests/requests-kerberos

.. image:: https://coveralls.io/repos/github/requests/requests-kerberos/badge.svg?branch=master
    :target: https://coveralls.io/github/requests/requests-kerberos?branch=master

Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication. Basic GET usage:


.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth
    >>> r = requests.get("http://example.org", auth=HTTPKerberosAuth())
    ...

The entire ``requests.api`` should be supported.

Authentication Failures
-----------------------

Client authentication failures will be communicated to the caller by returning
the 401 response.

Mutual Authentication
---------------------

REQUIRED
^^^^^^^^

By default, ``HTTPKerberosAuth`` will require mutual authentication from the
server, and if a server emits a non-error response which cannot be
authenticated, a ``requests_kerberos.errors.MutualAuthenticationError`` will
be raised. If a server emits an error which cannot be authenticated, it will
be returned to the user but with its contents and headers stripped. If the
response content is more important than the need for mutual auth on errors,
(eg, for certain WinRM calls) the stripping behavior can be suppressed by
setting ``sanitize_mutual_error_response=False``:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, REQUIRED
    >>> kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, sanitize_mutual_error_response=False)
    >>> r = requests.get("https://windows.example.org/wsman", auth=kerberos_auth)
    ...


OPTIONAL
^^^^^^^^

If you'd prefer to not require mutual authentication, you can set your
preference when constructing your ``HTTPKerberosAuth`` object:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, OPTIONAL
    >>> kerberos_auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
    >>> r = requests.get("http://example.org", auth=kerberos_auth)
    ...

This will cause ``requests_kerberos`` to attempt mutual authentication if the
server advertises that it supports it, and cause a failure if authentication
fails, but not if the server does not support it at all.

DISABLED
^^^^^^^^

While we don't recommend it, if you'd prefer to never attempt mutual
authentication, you can do that as well:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, DISABLED
    >>> kerberos_auth = HTTPKerberosAuth(mutual_authentication=DISABLED)
    >>> r = requests.get("http://example.org", auth=kerberos_auth)
    ...

Preemptive Authentication
-------------------------

``HTTPKerberosAuth`` can be forced to preemptively initiate the Kerberos
GSS exchange and present a Kerberos ticket on the initial request (and all
subsequent). By default, authentication only occurs after a
``401 Unauthorized`` response containing a Kerberos or Negotiate challenge
is received from the origin server. This can cause mutual authentication
failures for hosts that use a persistent connection (eg, Windows/WinRM), as
no Kerberos challenges are sent after the initial auth handshake. This
behavior can be altered by setting  ``force_preemptive=True``:

.. code-block:: python
    
    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, REQUIRED
    >>> kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, force_preemptive=True)
    >>> r = requests.get("https://windows.example.org/wsman", auth=kerberos_auth)
    ...

Hostname Override
-----------------

If communicating with a host whose DNS name doesn't match its
kerberos hostname (eg, behind a content switch or load balancer),
the hostname used for the Kerberos GSS exchange can be overridden by
setting the ``hostname_override`` arg:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, REQUIRED
    >>> kerberos_auth = HTTPKerberosAuth(hostname_override="internalhost.local")
    >>> r = requests.get("https://externalhost.example.org/", auth=kerberos_auth)
    ...

Explicit Principal
------------------

``HTTPKerberosAuth`` normally uses the default principal (ie, the user for
whom you last ran ``kinit`` or ``kswitch``, or an SSO credential if
applicable). However, an explicit principal can be specified, which will
cause Kerberos to look for a matching credential cache for the named user.
This feature depends on OS support for collection-type credential caches,
as well as working principal support in PyKerberos (it is broken in many
builds). An explicit principal can be specified with the ``principal`` arg:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth, REQUIRED
    >>> kerberos_auth = HTTPKerberosAuth(principal="user@REALM")
    >>> r = requests.get("http://example.org", auth=kerberos_auth)
    ...

On Windows, WinKerberos is used instead of PyKerberos. WinKerberos allows the
use of arbitrary principals instead of a credential cache. Passwords can be
specified by following the form ``user@realm:password`` for ``principal``.

Delegation
----------

``requests_kerberos`` supports credential delegation (``GSS_C_DELEG_FLAG``).
To enable delegation of credentials to a server that requests delegation, pass
``delegate=True`` to ``HTTPKerberosAuth``:

.. code-block:: python

    >>> import requests
    >>> from requests_kerberos import HTTPKerberosAuth
    >>> r = requests.get("http://example.org", auth=HTTPKerberosAuth(delegate=True))
    ...

Be careful to only allow delegation to servers you trust as they will be able
to impersonate you using the delegated credentials.

Logging
-------

This library makes extensive use of Python's logging facilities.

Log messages are logged to the ``requests_kerberos`` and
``requests_kerberos.kerberos_`` named loggers.

If you are having difficulty we suggest you configure logging. Issues with the
underlying kerberos libraries will be made apparent. Additionally, copious debug
information is made available which may assist in troubleshooting if you
increase your log level all the way up to debug.


History
=======

0.12.0: 2017-12-20
------------------------

- Add support for channel binding tokens (assumes pykerberos support >= 1.2.1)
- Add support for kerberos message encryption (assumes pykerberos support >= 1.2.1)
- Misc CI/test fixes

0.11.0: 2016-11-02
------------------

- Switch dependency on Windows from kerberos-sspi/pywin32 to WinKerberos.
  This brings Custom Principal support to Windows users.

0.10.0: 2016-05-18
------------------

- Make it possible to receive errors without having their contents and headers
  stripped.
- Resolve a bug caused by passing the ``principal`` keyword argument to
  kerberos-sspi on Windows.

0.9.0: 2016-05-06
-----------------

- Support for principal, hostname, and realm override.

- Added support for mutual auth.

0.8.0: 2016-01-07
-----------------

- Support for Kerberos delegation.

- Fixed problems declaring kerberos-sspi on Windows installs.

0.7.0: 2015-05-04
-----------------

- Added Windows native authentication support by adding kerberos-sspi as an
  alternative backend.

- Prevent infinite recursion when a server returns 401 to an authorization
  attempt.

- Reduce the logging during successful responses.

0.6.1: 2014-11-14
-----------------

- Fix HTTPKerberosAuth not to treat non-file as a file

- Prevent infinite recursion when GSSErrors occurs

0.6: 2014-11-04
---------------

- Handle mutual authentication (see pull request 36_)

  All users should upgrade immediately. This has been reported to
  oss-security_ and we are awaiting a proper CVE identifier.

  **Update**: We were issued CVE-2014-8650

- Distribute as a wheel.

.. _36: https://github.com/requests/requests-kerberos/pull/36
.. _oss-security: http://www.openwall.com/lists/oss-security/

0.5: 2014-05-14
---------------

- Allow non-HTTP service principals with HTTPKerberosAuth using a new optional
  argument ``service``.

- Fix bug in ``setup.py`` on distributions where the ``compiler`` module is
  not available.

- Add test dependencies to ``setup.py`` so ``python setup.py test`` will work.

0.4: 2013-10-26
---------------

- Minor updates in the README
- Change requirements to depend on requests above 1.1.0

0.3: 2013-06-02
---------------

- Work with servers operating on non-standard ports

0.2: 2013-03-26
---------------

- Not documented

0.1: Never released
-------------------

- Initial Release



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n requests-kerberos-%{unmangled_version} -n requests-kerberos-%{unmangled_version}
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
