%define major 1
%define libname %mklibname cdaudio %{major}
%define develname %mklibname cdaudio -d

Summary:	A library for controlling CD-ROM devices
Name:		libcdaudio
Version:	0.99.12
Release:	14
Group:		Sound
License:	LGPLv2+
URL:		http://libcdaudio.sourceforge.net/
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

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	cdaudio-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

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
%doc README NEWS AUTHORS ChangeLog
%{_sysconfdir}/cdserver
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_bindir}/libcdaudio-config
%{multiarch_bindir}/libcdaudio-config
%{_includedir}/*
%{_libdir}/lib*.so
%{_datadir}/aclocal/*
%{_libdir}/pkgconfig/libcdaudio.pc


%changelog
* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.99.12-11mdv2011.0
+ Revision: 660598
- update multiarch usage

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.12-10mdv2011.0
+ Revision: 602529
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.12-9mdv2010.1
+ Revision: 520759
- rebuilt for 2010.1

* Wed Aug 26 2009 Emmanuel Andry <eandry@mandriva.org> 0.99.12-8mdv2010.0
+ Revision: 421574
- apply libraries policy

* Wed Nov 19 2008 Frederik Himpe <fhimpe@mandriva.org> 0.99.12-7mdv2009.1
+ Revision: 304490
- Fix license, don't package wrong COPYING file
- Add patches to fix CVE-2005-0706 (from Gentoo) and CVE-2008-5030
  (from Fedora)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.99.12-6mdv2009.0
+ Revision: 222525
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.99.12-5mdv2008.1
+ Revision: 150486
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 02 2007 Anssi Hannula <anssi@mandriva.org> 0.99.12-4mdv2008.0
+ Revision: 77740
- readd devel provides
- make the devel package not obsolete itself

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99.12-3mdv2008.0
+ Revision: 76796
- new devel naming
- bunzip S1


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.99.12-2mdv2007.0
+ Revision: 108678
- Import libcdaudio

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.99.12-2mdv2007.1
- unpack the patch

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.99.12-2mdk
- Rebuild

* Wed Jul 20 2005 Götz Waschk <waschk@mandriva.org> 0.99.12-1mdk
- new URL
- New release 0.99.12

* Sat Jun 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.99.10-3mdk 
- use a central configuration file
- run libtoolize now
- source file is not versioned
- spec cleanup

* Mon Feb 07 2005 Götz Waschk <waschk@linux-mandrake.com> 0.99.10-2mdk
- multiarch

* Wed Apr 07 2004 Götz Waschk <waschk@linux-mandrake.com> 0.99.10-1mdk
- add pkgconfig file
- use mklibname
- autoconf2.5 macro
- don't run libtoolize
- new version

