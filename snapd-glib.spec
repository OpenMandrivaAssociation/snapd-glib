%define api 1
%define devname %mklibname -d snapd-glib

Name:		snapd-glib
Version:	1.70
Release:	1
Summary:	snapd-glib is a library to allow GLib based applications access to snapd, the daemon that controls Snaps.
License:	LGPL-3.0
URL:		https://github.com/snapcore/snapd-glib
Source0:	https://github.com/snapcore/snapd-glib/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem: meson
BuildRequires: meson
BuildRequires: gettext
BuildRequires: gi-docgen
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6QmlCore)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(vapigen)


%description
snapd-glib is a library to allow GLib based applications access to snapd, the daemon that controls Snaps. 
A snapd-qt library is provided that wraps snapd-glib for Qt based applications. The following languages / platforms are supported:
- C
- C++
- Vala
- Python (using GObject introspection)
- Javacript (using GObject introspection)
- Qt
- QML

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{name} = %{EVRD}

%description -n %{devname}
This package provides the files for developing applications
that use %{name} to communicate with snapd.



%files
%{_libdir}/libsnapd-glib-2.so.%{api}*
%{_libdir}/girepository-1.0/Snapd-2.typelib

%files -n snapd-qt
%{_libdir}/libsnapd-qt-%{api}.so.*

%files -n snapd-qt-qml
%{_qt6_qmldir}/Snapd%{api}/

%files -n %{devname}
%doc %{_datadir}/doc/snapd-glib/
%{_includedir}/snapd-glib-2/
%{_includedir}/snapd-qt-2/
%{_libdir}/cmake/Snapd2/
%{_libdir}/libsnapd-glib-2.so
%{_libdir}/libsnapd-qt-2.so
%{_libdir}/pkgconfig/snapd-glib-2.pc
%{_libdir}/pkgconfig/snapd-qt-2.pc
%{_datadr}/gir-1.0/Snapd-2.gir
%{_datadr}/vala/vapi/snapd-glib-2.deps
%{_datadr}/vala/vapi/snapd-glib-2.vapi

%files tests
%{_libexecdir}/installed-tests/snapd-glib-2/
%{_datadr}/installed-tests/snapd-glib-2/

