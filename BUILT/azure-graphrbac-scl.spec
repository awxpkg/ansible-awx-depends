%define scl rh-python36
%{?scl:%scl_package %{name}}
%{!?scl:%global pkg_name %{name}}

%define name azure-graphrbac
%define version 0.40.0
%define unmangled_version 0.40.0
%define unmangled_version 0.40.0
%define release 1

Summary: Microsoft Azure Graph RBAC Client Library for Python
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
Name: %{?scl_prefix}azure-graphrbac
Version: %{version}
Release: %{release}
Source0: azure-graphrbac-%{unmangled_version}.zip
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/azure-graphrbac-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Microsoft Corporation <azpysdkhelp@microsoft.com>
Packager: Martin Juhl <m@rtinjuhl.dk>
Url: https://github.com/Azure/azure-sdk-for-python


%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure Graph RBAC Client Library.

Azure Resource Manager (ARM) is the next generation of management APIs that
replace the old Azure Service Management (ASM).

This package has been tested with Python 2.7, 3.4, 3.5 and 3.6.

For the older Azure Service Management (ASM) libraries, see
`azure-servicemanagement-legacy <https://pypi.python.org/pypi/azure-servicemanagement-legacy>`__ library.

For a more complete set of Azure libraries, see the `azure <https://pypi.python.org/pypi/azure>`__ bundle package.


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

For code examples, see `GraphRBAC
<https://docs.microsoft.com/python/api/overview/azure/activedirectory>`__
on docs.microsoft.com.


Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the
`Issues <https://github.com/Azure/azure-sdk-for-python/issues>`__
section of the project.


.. :changelog:

Release History
===============

0.40.0 (2018-02-05)
+++++++++++++++++++

**Disclaimer**

To prepare future versions, all Model creation should use keyword only arguments.

**Breaking changes**

- ApplicationCreateParameters changed __init__ signature, breaks if positional arguments was used.
- ApplicationUpdateParameters changed __init__ signature, breaks if positional arguments was used.
- CheckGroupMembershipParameters changed __init__ signature, breaks if positional arguments was used.
- GetObjectsParameters changed __init__ signature, breaks if positional arguments was used.
- GroupAddMemberParameters changed __init__ signature, breaks if positional arguments was used.
- GroupCreateParameters changed __init__ signature, breaks if positional arguments was used.
- GroupGetMemberGroupsParameters changed __init__ signature, breaks if positional arguments was used.
- ServicePrincipalCreateParameters changed __init__ signature, breaks if positional arguments was used.
- UserCreateParameters changed __init__ signature, breaks if positional arguments was used.
- UserGetMemberGroupsParameters changed __init__ signature, breaks if positional arguments was used.
- UserUpdateParameters changed __init__ signature, breaks if positional arguments was used.
- groups.is_member_of now takes an instance of CheckGroupMembershipParameters, and not group_id, member_id parameters
- groups.add_member now have an optional parameter "additional_properties", breaks if positional arguments was used.
- groups.create now takes an instance of GroupCreateParameters, and not display_name, mail_nickname parameters
- groups.get_member_groups now have an optional parameter "additional_properties", breaks if positional arguments was used.
- service_principals.get_member_groups now have an optional parameter "additional_properties", breaks if positional arguments was used.

**Features**

- Enable additional_properties on all Models. to dynamically harvest new properties.
- Better hierarchy resolution and new generic Model like AADObject. This adds several new attribute to a lot of models.
- Operation groups now have a "models" attribute.
- Add applications.list_owners
- Add applications.add_owner
- Add service_principals.list_owners

0.33.0 (2017-11-01)
+++++++++++++++++++

**Features**

- add "required_resource_access" when applicable

**Bugfixes**

- Get/Delete of Users now encode for you if you provide the UPN.

0.32.0 (2017-09-22)
+++++++++++++++++++

**Features**

- Add Application.oauth2_allow_implicit_flow (create, update, get)
- Add to User: immutable_id, given_name, surname, user_type, account_enabled
- Add to UserCreate: given_name, surname, user_type, mail
- Add to UserUpdate: immutable_id, given_name, surname, user_type, user_principal_name

**Bugfixes**

- Renamed User.signInName to an array User.signInNames

0.31.0 (2017-08-09)
+++++++++++++++++++

- Add domains operation group
- Add usage locations to user
- Add several new attributes to AADObject

0.30.0 (2017-04-20)
+++++++++++++++++++

* ApiVersion is now 1.6 for the whole package
* This wheel package is now built with the azure wheel extension

0.30.0rc6 (2016-09-14)
++++++++++++++++++++++

**Bugfixes**

* 'list' methods returned only 100 entries (#653)

0.30.0rc5 (2016-06-23)
++++++++++++++++++++++

* Initial preview release



%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n azure-graphrbac-%{unmangled_version} -n azure-graphrbac-%{unmangled_version}
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
