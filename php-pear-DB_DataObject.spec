%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	DataObject
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an SQL builder, object interface to database tables
Summary(pl.UTF-8):	%{_pearname} - SQL builder, obiektowy interfejs do tabel bazodanowych
Name:		php-pear-%{_pearname}
Version:	1.9.5
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c8bc3c1644ed54498c9bbb62f82109e1
Patch0:		DB_DataObject-PLD.patch
URL:		http://pear.php.net/package/DB_DataObject/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(overload)
Requires:	php-common >= 3:4.3
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-DB >= 1.7.0
Requires:	php-pear-Date >= 1.4.3
Suggests:	php-pear-MDB2
Suggests:	php-pear-Validate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Validate.*)' 'pear(MDB2.*)'

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. Included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
- Builds SQL statements based on the objects vars and the builder
  methods,
- acts as a datastore for a table row.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Główna klasa została stworzona tak, by być rozszerzalną dla każdej
tabeli, więc można umieścić logikę danych w klasach danych. Dołączony
jest generator do tworzenia plików konfiguracyjnych i klas bazowych.
DataObject pełni 2 zadania:
- tworzy zapytania SQL bazując na zmiennych obiektowych i metodach
  tworzenia
- przechowuje dane z wiersza tabeli.

Ta klasa ma w PEAR status: %{_status}.

%package cli
Summary:	CLI interface for DB_DataObject
Summary(pl.UTF-8):	Interfejs linii poleceń dla DB_DataObject
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}

%description cli
CLI interface for DB_DataObject generator.

%description cli -l pl.UTF-8
Interfejs linii poleceń dla generatora DB_DataObject.

%prep
%pear_package_setup
mv ./%{php_pear_dir}/DB/DataObject/createTables.php DB_DataObject_createTables
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install DB_DataObject_createTables $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Cast.php
%{php_pear_dir}/%{_class}/%{_subclass}/Generator.php
%{php_pear_dir}/%{_class}/%{_subclass}/Error.php

%files cli
%defattr(644,root,root,755)
%doc docs/%{_pearname}/docs/example.ini
%attr(755,root,root) %{_bindir}/DB_DataObject_createTables
