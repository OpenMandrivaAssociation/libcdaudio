%define major	1
%define libname	%mklibname cdaudio %{major}
%define devname	%mklibname cdaudio -d

Summary:	A library for controlling CD-ROM devices
Name:		libcdaudio
Version:	0.99.12
Release:	24
Group:		Sound
License:	LGPLv2+
Url:		http://libcdaudio.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-config
Patch0:		%{name}-0.99.10.config.patch
Patch1:		%{name}-0.99-CAN-2005-0706.patch
Patch2:		%{name}-0.99.12-buffovfl.patch

%description
libcdaudio is a library for controlling CD-ROM devices

%package -n	%{libname}
Summary:	A library for controlling CD-ROM devices
Group:		System/Libraries

%description -n	%{libname}
libcdaudio is a library for controlling CD-ROM devices

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	cdaudio-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep
%setup -q
%apply_patches

cp %{SOURCE1} cdserver

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}/%{_sysconfdir}
install -m 644 cdserver %{buildroot}/%{_sysconfdir}

%multiarch_binaries %{buildroot}%{_bindir}/libcdaudio-config

%files -n %{libname}
%{_sysconfdir}/cdserver
%{_libdir}/libcdaudio.so.%{major}*

%files -n %{devname}
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/libcdaudio-config
%{multiarch_bindir}/libcdaudio-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/libcdaudio.pc

