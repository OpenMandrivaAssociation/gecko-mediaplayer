%define name	gecko-mediaplayer
%define version	0.5.1
%define rel	1

Summary:	GNOME MPlayer browser plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2
URL:		http://dekorte.homeip.net/download/gecko-mediaplayer/
Source:		http://dekorte.homeip.net/download/gecko-mediaplayer/%name-%version.tar.gz
Group:		Networking/WWW
BuildRoot:	%_tmppath/%name-root
Requires:	gnome-mplayer = %version
BuildRequires:	mozilla-firefox-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libx11-devel
BuildRequires:	libGConf2-devel

%description
Gecko Media Player is a browser plugin that uses GNOME MPlayer to
play media in a browser. It should work with all browsers on
Unix-ish systems(Linux, BSD, Solaris) and use the NS4 API (Mozilla,
Firefox, Opera, etc.).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

mv %buildroot%_docdir/%name installed-docs
rm installed-docs/{INSTALL,COPYING}

# zero length docs
find installed-docs -size 0 | xargs rm

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc installed-docs/*
%_libdir/mozilla/plugins/%{name}*.so
%_libdir/mozilla/plugins/%{name}*.xpt
