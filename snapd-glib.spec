Name:		snapd-glib
Version:	1.70
Release:	1
Summary:	snapd-glib is a library to allow GLib based applications access to snapd, the daemon that controls Snaps.
License:	LGPL-3.0
URL:		https://github.com/snapcore/snapd-glib
Source0:	https://github.com/snapcore/snapd-glib/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:  meson
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(vapigen)


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


%files
