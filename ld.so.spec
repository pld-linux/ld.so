Summary:	Shared library configuration tool and old dynamic loader
Summary(pl):	Stary loader dynamiczny - do uruchamiania program�w z libc5 
Summary(de):	Der alter dynamischer Loader fuer libc5
Summary(fr):	Outil de configuration de la biblioth�que partag�e et \
Summary(fr):	ancien chargeur dynamique
Summary(tr):	Ortak kitapl�k yap�land�rma arac� ve dinamik y�kleyici
Name:		ld.so
Version:	1.9.9
Release:	7
Copyright:	BSD
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://sunsite.unc.edu:/pub/Linux/GCC/%{name}-%{version}.tar.gz
Prereq:		basesystem
Exclusivearch:  sparc %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the shared library configuration tool, ldconfig, which
is required by many packages. It also includes the shared library loader
and dynamic loader for Linux libc 5.

%description -l pl
W pakiecie znajduj� si� narz�dzia do konfiguracji bibliotek dynamicznych libc5
oraz stary loader dynamiczny - r�wnie� pod libc5.

%description -l de
Dieses Paket enth�lt das Shared-Library-Konfigurations-Tool, ldconfig, 
welches f�r viele Pakete notwendig ist. Es enth�lt au�erdem den Shared-Library-
Loader und den dynamischen Loader f�r Linux libc 5.

%description -l fr
Ce package contient l'utilitaire de configuration pour les librairies
dynamiques, ldconfig, requis par de nombreux packages. Il contient aussi
le chargeur pour les libraries partag�es et dynamiques de la libc 5.

%description -l tr
Bu paket, pek �ok paketin gereksinim duydu�u ortak kitapl�klar� yap�land�rma
arac�n� ve libc-5 i�in ortak kitapl�k dinamik y�kleyicisini i�erir.

%prep
%setup -q

%build
# Don't compile it in any case ! ;) 
(cd d-link; make CC="/bin/false" 2>/dev/null)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,%{_mandir}/man{3,8}}

PREFIX=$RPM_BUILD_ROOT sh instldso.sh --force

rm -f $RPM_BUILD_ROOT%{_bindir}/ldd $RPM_BUILD_ROOT/sbin/ldconfig
rm -f $RPM_BUILD_ROOT%{_infodir}/ld.so.info
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/ldconfig.8

# ideally, these would come from GNU libc, but this is the best we can do
install man/dlopen.3 $RPM_BUILD_ROOT%{_mandir}/man3

echo .so dlopen.3 > $RPM_BUILD_ROOT%{_mandir}/man3/dlsym.3
echo .so dlopen.3 > $RPM_BUILD_ROOT%{_mandir}/man3/dlerror.3
echo .so dlopen.3 > $RPM_BUILD_ROOT%{_mandir}/man3/dlclose.3

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[138]/*
gzip -9nf README

%post 	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) /lib/ld.*
%attr(755,root,root) /lib/ld-*
%attr(755,root,root) /lib/lib*

%{_mandir}/man[138]/*
