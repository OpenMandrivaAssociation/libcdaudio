%define major 1
%define libname %mklibname cdaudio %{major}

Summary:	A library for controlling CD-ROM devices
Name:		libcdaudio
Version:	0.99.12
Release:	%mkrel 5
Group:		Sound
License:	GPL
URL:		http://libcdaudio.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-config
Patch0:		%{name}-0.99.10.config.patch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
libcdaudio is a library for controlling CD-ROM devices

%package -n	%{libname}
Summary:	A library for controlling CD-ROM devices
Group:		System/Libraries

%description -n	%{libname}
libcdaudio is a library for controlling CD-ROM devices

%package -n	%{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	cdaudio-devel = %{version}-%{release}
Obsoletes:      cdaudio-devel

%description -n	%{libname}-devel
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep

%setup -q
%patch0

cp %{SOURCE1} cdserver

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr (-,root,root)
%doc README NEWS AUTHORS COPYING ChangeLog
%{_sysconfdir}/cdserver
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr (-,root,root)
%_bindir/libcdaudio-config
%multiarch %_bindir/*/libcdaudio-config
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/libcdaudio.pc
