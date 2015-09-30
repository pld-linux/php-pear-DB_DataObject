%define		status		stable
%define		pearname	DB_DataObject
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - an SQL builder, object interface to database tables
Summary(pl.UTF-8):	%{pearname} - SQL builder, obiektowy interfejs do tabel bazodanowych
Name:		php-pear-%{pearname}
Version:	1.11.4
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	96dfccacd74b5bd4ae14324802f9d436
Patch0:		DB_DataObject-PLD.patch
URL:		http://pear.php.net/package/DB_DataObject/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.3
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-DB >= 1.7.0
Requires:	php-pear-Date >= 1.4.3
Suggests:	php-pear-MDB2
Suggests:	php-pear-Validate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Validate.*) pear(MDB2.*)

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. Included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
- Builds SQL statements based on the objects vars and the builder
  methods,
- acts as a datastore for a table row.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Główna klasa została stworzona tak, by być rozszerzalną dla każdej
tabeli, więc można umieścić logikę danych w klasach danych. Dołączony
jest generator do tworzenia plików konfiguracyjnych i klas bazowych.
DataObject pełni 2 zadania:
- tworzy zapytania SQL bazując na zmiennych obiektowych i metodach
  tworzenia
- przechowuje dane z wiersza tabeli.

Ta klasa ma w PEAR status: %{status}.

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
install -p DB_DataObject_createTables $RPM_BUILD_ROOT%{_bindir}

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
%{php_pear_dir}/DB/*.php
%dir %{php_pear_dir}/DB/DataObject
%{php_pear_dir}/DB/DataObject/Cast.php
%{php_pear_dir}/DB/DataObject/Error.php
%{php_pear_dir}/DB/DataObject/Generator.php
%{php_pear_dir}/DB/DataObject/Links.php

%files cli
%defattr(644,root,root,755)
%doc docs/%{pearname}/docs/example.ini
%attr(755,root,root) %{_bindir}/DB_DataObject_createTables
