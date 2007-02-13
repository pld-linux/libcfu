Summary:	A library of useful tools when developing multi-threaded software
Summary(pl.UTF-8):	Biblioteka nardzędzi przydatnych podczas tworzenia oprogramowania wielowątkowego
Name:		libcfu
Version:	0.02
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcfu/%{name}-%{version}.tar.bz2
# Source0-md5:	5e9e1a474119c8340509323f81c4c527
Patch0:		%{name}-shared.patch
URL:		http://www.sourceforge.net/projects/libcfu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libcfu.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libcfu.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README examples/
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_infodir}/libcfu.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
