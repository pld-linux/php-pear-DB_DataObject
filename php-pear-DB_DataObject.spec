%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	DataObject
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an SQL builder, object interface to database tables
Summary(pl):	%{_pearname} - SQL builder, obiektowy interfejs do tabel bazodanowych
Name:		php-pear-%{_pearname}
Version:	1.7.13
Release:	1.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b468b5de56401ce70bc1d3b4f9bd6286
URL:		http://pear.php.net/package/DB_DataObject/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Validate.*)'

%description
The core class is designed to be extended for each of your tables so
that you put the data logic inside the data classes. Included is a
Generator to make your configuration files and your base classes.
DataObject performs 2 tasks:
- Builds SQL statements based on the objects vars and the builder
  methods,
- acts as a datastore for a table row.

In PEAR status of this package is: %{_status}.

%description -l pl
G��wna klasa zosta�a stworzona tak, by by� rozszerzaln� dla ka�dej
tabeli, wi�c mo�na umie�ci� logik� danych w klasach danych. Do��czony
jest generator do tworzenia plik�w konfiguracyjnych i klas bazowych.
DataObject pe�ni 2 zadania:
- tworzy zapytania SQL bazuj�c na zmiennych obiektowych i metodach
  tworzenia
- przechowuje dane z wiersza tabeli.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/example.ini
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
