%define name	libcdaudio
%define version	0.99.12
%define release %mkrel 2
%define major	1
%define libname %mklibname cdaudio %major

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A library for controlling CD-ROM devices
License:	GPL
Group:		Sound
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-config.bz2
Patch0:		%{name}-0.99.10.config.patch
URL:		http://libcdaudio.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}
Provides:	%{name}%{major}
Obsoletes:	%{name}%{major}

%description
libcdaudio is a library for controlling CD-ROM devices

%package -n %libname
Group:		System/Libraries
Summary:	A library for controlling CD-ROM devices

%description -n %libname
libcdaudio is a library for controlling CD-ROM devices

%package -n %{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%release

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep
%setup -q
%patch
bzcat %{SOURCE1} > cdserver

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall
chmod 644 %{buildroot}%{_libdir}/libcdaudio.la

install -d -m 755 %{buildroot}/%{_sysconfdir}
install -m 644 cdserver %{buildroot}/%{_sysconfdir}

%multiarch_binaries %buildroot%_bindir/libcdaudio-config

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr (-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog
%{_sysconfdir}/cdserver
%{_libdir}/lib*.so.*

%files -n %libname-devel
%defattr (-,root,root)
%_bindir/libcdaudio-config
%multiarch %_bindir/*/libcdaudio-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/libcdaudio.pc


