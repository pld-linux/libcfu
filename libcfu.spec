Summary:	A library of useful tools when developing multi-threaded software
Summary(pl.UTF-8):	Biblioteka nardzędzi przydatnych podczas tworzenia oprogramowania wielowątkowego
Name:		libcfu
Version:	0.03
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://downloads.sourceforge.net/libcfu/%{name}-%{version}.tar.bz2
# Source0-md5:	7b73fcea701f73d30f4644a84d371481
Patch0:		%{name}-shared.patch
Patch1:		%{name}-examples.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-types.patch
URL:		https://libcfu.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcfu is a library of tools that can be useful, particularly when
developing multi-threaded software. It currently includes a hash
table, a linked list, self-extending strings, a configuration file
parser, a simple timer, and a thread queue.

%description -l pl.UTF-8
Libcfu jest zestawem narzędzi, które mogą okazać się przydatne,
szczególnie podczas rozwijania oprogramowania wielowątkowego.
Aktualnie zawiera tablicę haszującą, listę dynamiczną, samorozwijające
się ciągi znaków, parser plików konfiguracyjnych, prosty zegar oraz
kolejkę wątków.

%package devel
Summary:	Header files for libcfu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcfu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcfu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcfu.

%package static
Summary:	Static libcfu library
Summary(pl.UTF-8):	Statyczna biblioteka libcfu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcfu library.

%description static -l pl.UTF-8
Statyczna biblioteka libcfu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README src/TODO
%attr(755,root,root) %{_libdir}/libcfu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcfu.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libcfu-config
%attr(755,root,root) %{_libdir}/libcfu.so
%{_libdir}/libcfu.la
%{_includedir}/cfu*.h
%{_infodir}/libcfu.info*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libcfu.a
