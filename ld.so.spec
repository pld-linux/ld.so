Summary:	Shared library configuration tool and old dynamic loader
Summary(de.UTF-8):	Der alter dynamischer Loader fuer libc5
Summary(es.UTF-8):	Cargador dinámico Linux
Summary(fr.UTF-8):	Outil de configuration de la bibliothèque partagée et ancien chargeur dynamique
Summary(pl.UTF-8):	Stary loader dynamiczny - do uruchamiania programów z libc5
Summary(pt_BR.UTF-8):	Carregador dinâmico Linux
Summary(tr.UTF-8):	Ortak kitaplık yapılandırma aracı ve dinamik yükleyici
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

%description -l de.UTF-8
Dieses Paket enthält das Shared-Library-Konfigurations-Tool, ldconfig,
welches für viele Pakete notwendig ist. Es enthält außerdem den
Shared-Library- Loader und den dynamischen Loader für Linux libc 5.

%description -l es.UTF-8
Este paquete contiene el cargador dinámico para bibliotecas
compartidas.  Se requiere para todos los paquetes linkados
dinámicamente.

%description -l fr.UTF-8
Ce package contient l'utilitaire de configuration pour les librairies
dynamiques, ldconfig, requis par de nombreux packages. Il contient
aussi le chargeur pour les libraries partagées et dynamiques de la
libc 5.

%description -l pl.UTF-8
W pakiecie znajdują się narzędzia do konfiguracji bibliotek
dynamicznych libc5 oraz stary loader dynamiczny - również pod libc5.

%description -l pt_BR.UTF-8
Este pacote contém o carregador dinâmico para bibliotecas
compartilhadas. É requerido para todos os pacotes linkados
dinamicamente.

%description -l tr.UTF-8
Bu paket, pek çok paketin gereksinim duyduğu ortak kitaplıkları
yapılandırma aracını ve libc-5 için ortak kitaplık dinamik
yükleyicisini içerir.

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
