%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	DataObject
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an SQL builder, object interface to database tables
Summary(pl):	%{_pearname} - SQL builder, obiektowy interfejs do tabel bazodanowych
Name:		php-pear-%{_pearname}
Version:	1.8.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	770c44d243066340d639b063235dcc02
URL:		http://pear.php.net/package/DB_DataObject/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-DB >= 1.7.0
Requires:	php-pear-Date >= 1.4.3
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

%description -l pl
G³ówna klasa zosta³a stworzona tak, by byæ rozszerzaln± dla ka¿dej
tabeli, wiêc mo¿na umie¶ciæ logikê danych w klasach danych. Do³±czony
jest generator do tworzenia plików konfiguracyjnych i klas bazowych.
DataObject pe³ni 2 zadania:
- tworzy zapytania SQL bazuj±c na zmiennych obiektowych i metodach
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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
