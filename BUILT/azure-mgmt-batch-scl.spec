%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-mgmt-batch
%define version 4.1.0
%define unmangled_version 4.1.0
%define unmangled_version 4.1.0
%define release 1

Summary: Microsoft Azure Batch Management Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-mgmt-batch
Version: %{version}
Release: %{release}
Source0: azure-mgmt-batch-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-mgmt-batch-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <ptvshelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Batch Management Client Library.

This package has been tested with Python 2.7, 3.3, 3.4 and 3.5.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first:

.. code:: shell

    pip uninstall azure


Usage
=====

For code examples, see `the Batch samples repo  
<https://github.com/Azure/azure-batch-samples/tree/master/Python>`__
on GitHub.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

4.1.0 (2017-07-24)
++++++++++++++++++

- New operation to check the availability and validity of a Batch account name.

4.0.0 (2017-05-10)
++++++++++++++++++

- New operation to list the operations available for the Microsoft.Batch provider, includes new `Operation` and `OperationDisplay` models.
- Renamed `AddApplicationParameters` to `ApplicationCreateParameters`.
- Renamed `UpdateApplicationParameters` to `ApplicationUpdateParameters`.
- Removed `core_quota` attribute from `BatchAccount` object, now replaced by separate `dedicated_core_quota` and `low_priority_core_quota`.
- `BatchAccountKeys` object now has additional `account_name` attribute.

3.0.1 (2017-04-19)
++++++++++++++++++

- This wheel package is now built with the azure wheel extension

3.0.0 (2017-03-07)
++++++++++++++++++

- Updated `BatchAccount` model - support for pool allocation in the user's subscription.
- Updated `BatchAccount` model - support for referencing an Azure Key Vault for accounts created with a pool allocation mode of UserSubscription.
- Updated `BatchAccount` model - properties are now read only.
- Updated `ApplicationPackage` model - properties are now read only.
- Updated `BatchAccountKeys` model - properties are now read only.
- Updated `BatchLocationQuota` model - properties are now read only.

2.0.0 (2016-10-04)
++++++++++++++++++

- Renamed `AccountResource` to `BatchAccount`.
- Renamed `AccountOperations` to `BatchAccountOperations`. The `IBatchManagementClient.Account` property was also renamed to `IBatchManagementClient.BatchAccount`.
- Split `Application` and `ApplicationPackage` operations up into two separate operation groups. 
- Updated `Application` and `ApplicationPackage` methods to use the standard `Create`, `Delete`, `Update` syntax. For example creating an `Application` is done via `ApplicationOperations.Create`.
- Renamed `SubscriptionOperations` to `LocationOperations` and changed `SubscriptionOperations.GetSubscriptionQuotas` to be `LocationOperations.GetQuotas`.
- This version targets REST API version 2015-12-01.

1.0.0 (2016-08-09)
++++++++++++++++++

- Initial Release



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-mgmt-batch-%{unmangled_version} -n azure-mgmt-batch-%{unmangled_version}
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
