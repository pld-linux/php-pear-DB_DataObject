%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       DataObject
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - An SQL Builder, Object Interface to Database Tables
Summary(pl):	%{_class}_%{_subclass} -
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
 - Builds SQL statements based on the objects vars and the builder
   methods,
 - acts as a datastore for a table row

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/example.ini
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
