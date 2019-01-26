%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-cli-nspkg
%define version 3.0.2
%define unmangled_version 3.0.2
%define unmangled_version 3.0.2
%define release 1

Summary: Microsoft Azure CLI Namespace Package
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-cli-nspkg
Version: %{version}
Release: %{release}
Source0: azure-cli-nspkg-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-cli-nspkg-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <azpycli@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-cli


%description
Microsoft Azure CLI Namespace Package
=====================================

This is the Microsoft Azure CLI namespace package.

This package is not intended to be installed directly by the end user.

It provides the necessary files for other packages to extend the azure cli namespaces.


.. :changelog:

Release History
===============

3.0.2
+++++
* minor fixes

3.0.1
+++++
* minor fixes

3.0.0 (2016-04-28)
++++++++++++++++++

* New nspkg structure.

2.0.0 (2016-02-27)
++++++++++++++++++

* GA release.

0.1.2 (2016-01-30)
++++++++++++++++++

* Support Python 3.6.

0.1.1 (2016-01-17)
++++++++++++++++++

* Stable release (no code changes since previous version).

0.1.0b11 (2016-12-12)
+++++++++++++++++++++

* Preview release.



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-cli-nspkg-%{unmangled_version} -n azure-cli-nspkg-%{unmangled_version}
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