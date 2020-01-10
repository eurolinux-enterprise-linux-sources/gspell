%global glib2_version 2.44
%global gtk3_version 3.20

Name:           gspell
Version:        1.2.3
Release:        1%{?dist}
Summary:        Spell-checking library for GTK+

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/gspell
Source0:        https://download.gnome.org/sources/%{name}/1.2/%{name}-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  vala

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       iso-codes

%description
gspell provides a flexible API to implement the spell checking
in a GTK+ application.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

%find_lang gspell-1


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f gspell-1.lang
%license COPYING
%{_libdir}/girepository-1.0/
%{_libdir}/libgspell-1.so.1*

%files devel
%{_includedir}/gspell-1/
%{_libdir}/libgspell-1.so
%{_libdir}/pkgconfig/gspell-1.pc
%{_datadir}/gir-1.0/
%{_datadir}/vala/

%files doc
%{_datadir}/gtk-doc/


%changelog
* Fri Feb 24 2017 Kalev Lember <klember@redhat.com> - 1.2.3-1
- Update to 1.2.3
- Resolves: #1388481

* Fri Dec 16 2016 Kalev Lember <klember@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed Nov 23 2016 Kalev Lember <klember@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 1.2.0-2
- BR vala instead of obsolete vala-tools subpackage

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Sun Aug 14 2016 Kalev Lember <klember@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Sun Jul 17 2016 Kalev Lember <klember@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Sun Jul 10 2016 Kalev Lember <klember@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Fri Jun 10 2016 Kalev Lember <klember@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 0.2.4-1
- Update to 0.2.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 0.2.2-1
- Update to 0.2.2
- This update relicensed gspell from GPLv2+ to LGPLv2+

* Mon Dec 07 2015 Kalev Lember <klember@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Sun Dec 06 2015 Kalev Lember <klember@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Thu Oct 15 2015 Kalev Lember <klember@redhat.com> - 0.1.0-1
- Initial Fedora packaging (#1271944)
