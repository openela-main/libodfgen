%global apiversion 0.1

Name: libodfgen
Version: 0.1.6
Release: 11%{?dist}
Summary: An ODF generator library

License: LGPLv2+ or MPLv2.0
URL: https://sourceforge.net/p/libwpd/wiki/libodfgen/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: pkgconfig(librevenge-0.0)

Patch0: 0001-tdf-101077-make-double-string-conversion-locale-agno.patch

%description
%{name} is a library for generating ODF documents. It is directly
pluggable into input filters based on librevenge. It is used in
libreoffice or calligra, for example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static --disable-werror --with-sharedptr=c++11
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README NEWS
%license COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.*
%doc docs/doxygen/html

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.1.6-10
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.6-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.6-5
- Rebuilt for Boost 1.63

* Fri Aug 12 2016 David Tardon <dtardon@redhat.com> - 0.1.6-4
- Resolves: tdf#101077 make double->str conv. locale-agnostic

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.6-2
- Rebuilt for Boost 1.60

* Wed Dec 30 2015 David Tardon <dtardon@redhat.com> - 0.1.6-1
- new upstream release

* Mon Nov 02 2015 David Tardon <dtardon@redhat.com> - 0.1.5-2
- Resolves: rhbz#1277049 libodfgen-0.1.5-1 is not built with $RPM_OPT_FLAGS

* Fri Oct 30 2015 David Tardon <dtardon@redhat.com> - 0.1.5-1
- new upstream release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.1.4-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1.4-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 David Tardon <dtardon@redhat.com> - 0.1.4-1
- new upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.1.3-2
- Rebuild for boost 1.57.0

* Fri Jan 02 2015 David Tardon <dtardon@redhat.com> - 0.1.3-1
- new upstream release

* Mon Nov 24 2014 David Tardon <dtardon@redhat.com> - 0.1.2-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 David Tardon <dtardon@redhat.com> - 0.1.1-1
- new upstream release

* Mon May 26 2014 David Tardon <dtardon@redhat.com> - 0.1.0-1
- new upstream release

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.0.4-2
- rebuild for boost 1.55.0

* Wed Dec 04 2013 David Tardon <dtardon@redhat.com> - 0.0.4-1
- new release

* Tue Dec 03 2013 David Tardon <dtardon@redhat.com> - 0.0.3-2
- rhbz#1000893 do not pull in unneeded packages

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> - 0.0.3-1
- new release

* Mon Sep 09 2013 David Tardon <dtardon@redhat.com> - 0.0.2-3
- do not build in C++11 mode

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new release

* Wed May 08 2013 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new release

* Fri May 03 2013 David Tardon <dtardon@redhat.com> - 0.0.0-1
- initial import
