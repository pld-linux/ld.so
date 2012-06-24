Summary:	Shared library configuration tool and old dynamic loader
Summary(de):	Der alter dynamischer Loader fuer libc5
Summary(es):	Cargador din�mico Linux
Summary(fr):	Outil de configuration de la biblioth�que partag�e et ancien chargeur dynamique
Summary(pl):	Stary loader dynamiczny - do uruchamiania program�w z libc5
Summary(pt_BR):	Carregador din�mico Linux
Summary(tr):	Ortak kitapl�k yap�land�rma arac� ve dinamik y�kleyici
Name:		ld.so
Version:	1.9.9
Release:	13
License:	BSD
Group:		Libraries
Source0:	ftp://sunsite.unc.edu/pub/Linux/GCC/%{name}-%{version}.tar.gz
# Source0-md5:	02ac850a6a267feed265fc74ded068b7
Patch0:		%{name}-install.patch
Requires:	basesystem
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib

%description
This package contains the shared library configuration tool, ldconfig,
which is required by many packages. It also includes the shared
library loader and dynamic loader for Linux libc 5.

%description -l de
Dieses Paket enth�lt das Shared-Library-Konfigurations-Tool, ldconfig,
welches f�r viele Pakete notwendig ist. Es enth�lt au�erdem den
Shared-Library- Loader und den dynamischen Loader f�r Linux libc 5.

%description -l es
Este paquete contiene el cargador din�mico para bibliotecas
compartidas.  Se requiere para todos los paquetes linkados
din�micamente.

%description -l fr
Ce package contient l'utilitaire de configuration pour les librairies
dynamiques, ldconfig, requis par de nombreux packages. Il contient
aussi le chargeur pour les libraries partag�es et dynamiques de la
libc 5.

%description -l pl
W pakiecie znajduj� si� narz�dzia do konfiguracji bibliotek
dynamicznych libc5 oraz stary loader dynamiczny - r�wnie� pod libc5.

%description -l pt_BR
Este pacote cont�m o carregador din�mico para bibliotecas
compartilhadas. � requerido para todos os pacotes linkados
dinamicamente.

%description -l tr
Bu paket, pek �ok paketin gereksinim duydu�u ortak kitapl�klar�
yap�land�rma arac�n� ve libc-5 i�in ortak kitapl�k dinamik
y�kleyicisini i�erir.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

PREFIX=$RPM_BUILD_ROOT \
MANDIR=%{_mandir} \
LIBDIR=%{_libdir} \
sh instldso.sh --force

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*
