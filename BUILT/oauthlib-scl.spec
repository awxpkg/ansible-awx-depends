%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name oauthlib
%define version 3.0.1
%define unmangled_version 3.0.1
%define unmangled_version 3.0.1
%define release 1

Summary: A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}oauthlib
Version: %{version}
Release: %{release}
Source0: oauthlib-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/oauthlib-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ib Lundgren <ib.lundgren@gmail.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/oauthlib/oauthlib


%description
OAuthLib - Python Framework for OAuth1 & OAuth2
===============================================

*A generic, spec-compliant, thorough implementation of the OAuth request-signing
logic for Python 2.7 and 3.4+.*

.. image:: https://travis-ci.org/oauthlib/oauthlib.svg?branch=master
  :target: https://travis-ci.org/oauthlib/oauthlib
  :alt: Travis
.. image:: https://coveralls.io/repos/oauthlib/oauthlib/badge.svg?branch=master
  :target: https://coveralls.io/r/oauthlib/oauthlib
  :alt: Coveralls
.. image:: https://img.shields.io/pypi/pyversions/oauthlib.svg
  :target: https://pypi.org/project/oauthlib/
  :alt: Download from PyPI
.. image:: https://img.shields.io/pypi/l/oauthlib.svg
  :target: https://pypi.org/project/oauthlib/
  :alt: License
.. image:: https://app.fossa.io/api/projects/git%2Bgithub.com%2Foauthlib%2Foauthlib.svg?type=shield
   :target: https://app.fossa.io/projects/git%2Bgithub.com%2Foauthlib%2Foauthlib?ref=badge_shield
   :alt: FOSSA Status
.. image:: https://img.shields.io/readthedocs/oauthlib.svg
  :target: https://oauthlib.readthedocs.io/en/latest/index.html
  :alt: Read the Docs
.. image:: https://badges.gitter.im/oauthlib/oauthlib.svg
  :target: https://gitter.im/oauthlib/Lobby
  :alt: Chat on Gitter

OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for handling OAuth requests, but they all suffer from one or
both of the following:

1. They predate the `OAuth 1.0 spec`_, AKA RFC 5849.
2. They predate the `OAuth 2.0 spec`_, AKA RFC 6749.
3. They assume the usage of a specific HTTP request library.

.. _`OAuth 1.0 spec`: https://tools.ietf.org/html/rfc5849
.. _`OAuth 2.0 spec`: https://tools.ietf.org/html/rfc6749

OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without
assuming a specific HTTP request object or web framework. Use it to graft OAuth
client support onto your favorite HTTP library, or provide support onto your
favourite web framework. If you're a maintainer of such a library, write a thin
veneer on top of OAuthLib and get OAuth support for very little effort.


Documentation
--------------

Full documentation is available on `Read the Docs`_. All contributions are very
welcome! The documentation is still quite sparse, please open an issue for what
you'd like to know, or discuss it in our `Gitter community`_, or even better, send a
pull request!

.. _`Gitter community`: https://gitter.im/oauthlib/Lobby
.. _`Read the Docs`: https://oauthlib.readthedocs.io/en/latest/index.html

Interested in making OAuth requests?
------------------------------------

Then you might be more interested in using `requests`_ which has OAuthLib
powered OAuth support provided by the `requests-oauthlib`_ library.

.. _`requests`: https://github.com/requests/requests
.. _`requests-oauthlib`: https://github.com/requests/requests-oauthlib

Which web frameworks are supported?
-----------------------------------

The following packages provide OAuth support using OAuthLib.

- For Django there is `django-oauth-toolkit`_, which includes `Django REST framework`_ support.
- For Flask there is `flask-oauthlib`_ and `Flask-Dance`_.
- For Pyramid there is `pyramid-oauthlib`_.
- For Bottle there is `bottle-oauthlib`_.

If you have written an OAuthLib package that supports your favorite framework,
please open a Pull Request, updating the documentation.

.. _`django-oauth-toolkit`: https://github.com/evonove/django-oauth-toolkit
.. _`flask-oauthlib`: https://github.com/lepture/flask-oauthlib
.. _`Django REST framework`: http://django-rest-framework.org
.. _`Flask-Dance`: https://github.com/singingwolfboy/flask-dance
.. _`pyramid-oauthlib`: https://github.com/tilgovi/pyramid-oauthlib
.. _`bottle-oauthlib`: https://github.com/thomsonreuters/bottle-oauthlib

Using OAuthLib? Please get in touch!
------------------------------------
Patching OAuth support onto an http request framework? Creating an OAuth
provider extension for a web framework? Simply using OAuthLib to Get Things Done
or to learn?

No matter which we'd love to hear from you in our `Gitter community`_ or if you have
anything in particular you would like to have, change or comment on don't
hesitate for a second to send a pull request or open an issue. We might be quite
busy and therefore slow to reply but we love feedback!

Chances are you have run into something annoying that you wish there was
documentation for, if you wish to gain eternal fame and glory, and a drink if we
have the pleasure to run into eachother, please send a docs pull request =)

.. _`Gitter community`: https://gitter.im/oauthlib/Lobby

License
-------

OAuthLib is yours to use and abuse according to the terms of the BSD license.
Check the LICENSE file for full details.

Credits
-------

OAuthLib has been started and maintained several years by Idan Gazit and other
amazing `AUTHORS`_. Thanks to their wonderful work, the open-source `community`_
creation has been possible and the project can stay active and reactive to users
requests.


.. _`AUTHORS`: https://github.com/oauthlib/oauthlib/blob/master/AUTHORS
.. _`community`: https://github.com/oauthlib/

Changelog
---------

*OAuthLib is in active development, with the core of both OAuth1 and OAuth2
completed, for providers as well as clients.* See `supported features`_ for
details.

.. _`supported features`: https://oauthlib.readthedocs.io/en/latest/feature_matrix.html

For a full changelog see ``CHANGELOG.rst``.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n oauthlib-%{unmangled_version} -n oauthlib-%{unmangled_version}
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
